#breaking out of hearst castle
import time
import sys
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)

accumulator = 5
str(accumulator)
import time #This gives a time variable for waiting before each passage appears.


 
def setting():
  print ("") #This is the background story and sets up the game.
  print ('You wake up in the morning and find yourslf stuck in hearst castle. The big buildings and gold for ceiling are freaking you out, until a man walks in. He tells you there are only two ways to get out and you have to figure it out.')
  print ("")
  (accumulator)


def startgame(): #This is the first intro
  time.sleep(1)
  print("This is the Hearst Castle, Storyline game.")
  print("")
  time.sleep(1)
  print('Welcome, ready to play our game?')
  print("")
  time.sleep(1)
  print('(I should probably answer with \"Yes\")')
  print ("") 
  answer1 = input()
  if answer1 in {'Yes', 'yes', 'YES'}:
    setting()
  else: #This makes it that if they dont answer yes, it'll force them to say yes.
    print ("")
    print ('Can you read?')
    print ("")

startgame()
def p():


def Choice1(accumulator): #This is the first intro to a decision.
  time.sleep(1.5) 
  print ('emma: Hey! Hey! Wake Up! We\'re making an escape. Since I\'m stuck with you, you\'re coming with me.')
  print ("")
  time.sleep(1.5)
  print ( name + ': (Crap he looks dangerous, I should listen to him).')
  print ("")
  time.sleep(1.5)
  print ('What will you do? If you\'ll help him, answer Yes, if not say No.')
  print ("")

(accumulator)



def decisionrepeat1(accumulator): #this is the first choice, they can die at this point.
  decision1=input()
  if decision1 in {'Yes', 'yes', 'YES'}:
    print ("")
    print (name + ': Yeah, I\'ll help you I guess.')
    print ("")
    choseyes1(accumulator)
  elif decision1 in {'No', 'no', 'NO'}:
    print ("")
    time.sleep(1.5)
    print ('emma: i suggest you play and help me get out of here')
    print ("")
    time.sleep(1.5)
    print(Fore.RED) #this allows them to restart this choice again.
    print_slow ('You have died.')
    print("")
    print("")
    accumulator = accumulator - 1
    time.sleep(2)
    print_slow ("You have " + str(accumulator) + " lives left. Type restart to return to checkpoint.")
    print("")
    if accumulator == 0:
      print_slow("Nevermind. You have lost all your lives. Game Over. Please Try Again later.")

time.sleep(2)
exit()
   
   
