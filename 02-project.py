import random
import os
os.system('cls')

def game(com,you):
 if com == you :
  return None  
 
 elif com =='s': 
     if you == 'e':
         return False   
     elif you == 'p':
        return True
 
 elif com =='p': 
     if you == 's':
         return False 
     elif you == 'e':
        return True
 
 elif com =='e': 
     if you == 'p':
         return False
     elif you == 's':
        return True
    
print("Computer turn is done")
rn= random.randint(1,3)
if rn==1: 
 com = 's'
elif rn==2:
    com = 'p'
elif rn==3:
    com = 'e'

you =input("Now, it's your turn stone(s) paper(p) scissor(e) : ")

print(f"Computer choose : {com} ")
print(f"You choose : {you} ")

a = game(com,you)
if a == None :
    print("The game is tie ")
elif a :
    print("You win")
else :
    print("You lose")