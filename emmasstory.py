#My Python Story
import time
time.sleep(1)

def greeting():
    print("Hello...")
    time.sleep(1)
    response=input("Do you want to play a game? (yes/no) ")
    return response


def second_choice():
    time.sleep(1)
    print("Great...")
    time.sleep(1)
    response=input("there's a creepy box on your floor do you open it? (yes/no) ")
    return response
def haters():
    print("Lame...Bye Then! ")

def third_choice():
    time.sleep(3)
    print("Congratulations, you survived the first round! ")
    time.sleep(3)
    response=input("The box has something moving inside of it... do you want to throw it out or keep it? (throw it out/keep it) ")
    return response

def yes():("there is a little box inside...")


def throw():
    time.sleep(3)
    print("you won and killed the snake in the box!! THE END ")

def last_choice():
    time.sleep(3)
    print("Dont be an idiot... throw that box out")
    time.sleep(3)
    response=input("You've made it to the end of the game. ")
    return response

def shrimp():
    time.sleep(3)
    print("You have chosen the All-you-can-eat-shrimp for $4.99. Enjoy! ")

def hotpocket():
    time.sleep(3)
    print("You have chosen 100 Hot Pockets. Enjoy! ")
    
x = greeting()
if x== "yes":
    y = second_choice()
    if y== "throw":
        z = third_choice()
        if z== "open":
            a = last_choice()
            
