 Code Guessing Game (Streamlit)
A simple and fun Code Guessing Game, converted from the original terminal-based
Python script into an interactive Streamlit web app. It now runs right in the
browser and can be deployed live via GitHub / Streamlit Community Cloud.
 How to Play
The app randomly picks a secret code (between 0 and 8).
You get a total of 5 attempts to guess the correct code.
After every wrong guess, you're shown how many attempts you've used and how
many are left.
If you guess the correct code, you win 
If you run out of attempts without guessing correctly, the game ends and the
correct code is revealed.
Click "Play Again" to start a new game.
 Local Setup
Clone the repository:
Bash
Create a virtual environment (optional but recommended):
Bash
Install dependencies:
Bash
Run the app:
Bash
Your browser should open automatically, or go to this URL manually:
Code
 Deploying Live on GitHub (Streamlit Community Cloud)
Push this code to your GitHub repository (game.py, requirements.txt,
and README.md all included).
Go to share.streamlit.io and sign in with your
GitHub account.
Click "New app".
Select your repository, branch, and main file (app.py).
Click Deploy — that's it! Within seconds your app will be live with a
public shareable link.
 Project Structure
Code
 Features
Interactive UI with attempt tracking
Guess history table
Win/Lose messages with emojis and balloon animation
One-click "Play Again" to restart the game
Fully deployable on Streamlit Community Cloud, free of cost
 License
Free to use, modify, and share for learning purposes.
