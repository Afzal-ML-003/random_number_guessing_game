import time
import random
safe_box_code = random.randrange(9)
max_attempts = 5


count_attempts = 0

print("\n              WELCOME CODE GUSSING GAME ")
while count_attempts < max_attempts:
   count_attempts += 1
   try:
       code = int(input("\nGuess Code:   "))
   except ValueError:
       print("\n Serf Number Enter kren,")
       count_attempts -= 1
       continue
   if code == safe_box_code:
       print("\nYahoo! Safe Unlocked!")
       break
   elif max_attempts > count_attempts and code != safe_box_code:
       print(f"\n  Wrong Code \n  Aap ne try kr li he ({count_attempts}) \n  Aap ki Try Bachi He ({max_attempts-count_attempts})")
       time.sleep(2)
        
   else:
       print(f"\nWrong Code! Aap ki Try Poori Ho Chuki Hen.\n\nSahi Code tha. ({safe_box_code}) Sea You Next Time By!")  
       
print("\n                     GAME OVER!")      
