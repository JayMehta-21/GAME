r="rock" 
p="paper"
s="sisser"


import random as ran

com=ran.choice([r,p,s])

print("choices are (rock,paper,sisser)")
user=input("enetr your choice : ")

def game(a,b):

    if(a==b):
        print("game draw")
    elif ( a==r and b==p ):
        print(f" user win the game")
    elif (r==p and b==s):
        print(f" user win the game")
    elif(r==s and b==r):
        print(f"user win the game")
    else:
        print(f"computer win the game")

game(com,user)

print(f"you choose {user}")
print(f"computer choose {com}")