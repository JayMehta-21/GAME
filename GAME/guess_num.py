import random as ran

com=ran.choice(range(500))

print("enetr a number from 0 to 500")

def compare():
    item=0
    # while(True):
    for i in range(0,501):
        user=int(input("enter your choice : "))
        if(user==com):
         print("congrat buddy !")
         item+=1
         break
        elif(user<com):
          print("enter a higher number")
          item+=1
          
        elif(user>com):
          print("eneter a lower number")
          item+=1
    print (f"you guess the correct number '{com}' in total of '{item}' guess")
    if(item>=10):
       print("you are a noob !")
    else:
       print("you are a proo !")
       
       
compare()

# print(f"com choose {com}")