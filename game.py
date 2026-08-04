    
import streamlit as st
import random
import time

st.set_page_config(page_title="Code Guessing Game", page_icon="🔐", layout="centered")

MAX_ATTEMPTS = 8
MIN_CODE = 0
MAX_CODE = 9  # matches original random.randrange(9) -> 0 to 8

# ---------- Session State Init ----------
if "safe_box_code" not in st.session_state:
    st.session_state.safe_box_code = random.randrange(MAX_CODE)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "won" not in st.session_state:
    st.session_state.won = False
if "history" not in st.session_state:
    st.session_state.history = []


def reset_game():
    st.session_state.safe_box_code = random.randrange(MAX_CODE)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.won = False
    st.session_state.history = []


# ---------- Header ----------
st.markdown(
    "<h1 style='text-align:center;'>🔐 WELCOME CODE GUESSING GAME 🔐</h1>",
    unsafe_allow_html=True,
)
st.write(
    f"Guess the correct code between **{MIN_CODE}** and **{MAX_CODE - 1}**. "
    f"Aap ke pass total **{MAX_ATTEMPTS}** attempts hain."
)

remaining = MAX_ATTEMPTS - st.session_state.attempts
st.info(f"Attempts Used: **{st.session_state.attempts}** | Attempts Left: **{remaining}**")

# ---------- Game Logic ----------
if not st.session_state.game_over:
    with st.form("guess_form", clear_on_submit=True):
        guess = st.number_input(
            "Guess Code:", min_value=0, max_value=99, step=1, format="%d"
        )
        submitted = st.form_submit_button("Submit Guess")

    if submitted:
        st.session_state.attempts += 1
        code = int(guess)

        if code == st.session_state.safe_box_code:
            st.session_state.won = True
            st.session_state.game_over = True
            st.session_state.history.append((code, "✅ Correct"))
        elif st.session_state.attempts >= MAX_ATTEMPTS:
            st.session_state.game_over = True
            st.session_state.history.append((code, "❌ Wrong"))
        else:
            st.session_state.history.append((code, "❌ Wrong"))

        st.rerun()

else:
    if st.session_state.won:
        st.success(
            f"🎉 Yahoo! Safe Unlocked! Aap ne sahi code guess kr liya "
            f"({st.session_state.attempts} attempts men)."
        )
        st.balloons()
    else:
        st.error(
            f"💥 Wrong Code! Aap ki Try Poori Ho Chuki Hen.\n\n"
            f"Sahi Code tha: **{st.session_state.safe_box_code}**  \n"
            f"See You Next Time, Bye!"
        )

    if st.button("🔄 Play Again"):
        reset_game()
        st.rerun()

# ---------- Guess History ----------
if st.session_state.history:
    st.markdown("### 📜 Guess History")
    for i, (g, result) in enumerate(st.session_state.history, start=1):
        st.write(f"{i}. Guess: `{g}` → {result}")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
