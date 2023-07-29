import random
from replit import clear
from game_data import data
from art import logo,vs

def ran_data(data):

  return random.choice(data);


def display_data(a):
  P_name=a["name"]
  P_followers=a["follower_count"]
  P_descrip=a["description"]
  P_country=a["country"]
  return P_name, P_descrip, P_country

def play_game():
  a=ran_data(data)
  b=ran_data(data)
  k=True
  score=0
  print(f"{logo}")
  while(k==True):
    print(f"Compare A: {display_data(a)}")
    print(f"{vs}")
    print(f"Against B: {display_data(b)}")
    choice=input("Who has more followers A or B? Type A or B.\t").lower()
    clear()
    print(f"{logo}")
    if(a["follower_count"]>b["follower_count"] and choice=='a'):
      score+=1
      a=b
      b=ran_data(data)
      print(f"You are right. Current score is {score}.")
    elif(a["follower_count"]<b["follower_count"] and choice=='b'):
      score+=1
      a=b
      b=ran_data(data)
      print(f"You are right. Current score is {score}.")
    elif(a["follower_count"]==b["follower_count"]):
      score+=1
      a=b
      b=ran_data(data)
      print(f"Its a Draw. Current Score is {score}.")
    else:
      k=False
      print(f"You lost. Final score:{score}.")
    
score=play_game()
