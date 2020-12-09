import random
min_range = int(input("Enter min range"))
max_range = int(input("Enter max range"))
actual_number=random.randint(min_range,max_range)
print(actual_number)
player1_turns = 0
player2_turns = 0
flag = True
print("\t \t \tThe game starts now")
print(f"Please guess the number between {min_range} to {max_range}")
while(flag):
    player1 = input("Player1: ")
    player1_turns+=1
    if int(player1)>actual_number:
        print("YOu have guess greater number ")
    elif int(player1)<actual_number:
        print("You have guess less number")
    elif actual_number==int(player1):
        print("player1 guess the right number")
        print(f"Player1 guess the right number in {player1_turns} turns\n")
        actual_number2=random.randint(min_range,max_range)
        print("Now player2 guess the number")
        print("Player2 actual no." , actual_number2)
        while(flag):
            player2_turns+=1
            player2= input("Player2: ")
            if int(player2)>actual_number2:
                print("You have guess a greater number")
            elif int(player2)<actual_number2:
                print("You have guess a lesser number")
            elif actual_number2==int(player2):
              print("Player2 guess the right number")
              print(f"Player2 guess the right number in {player2_turns} turns\n")
              flag= False


if player1_turns<player2_turns:
    print("Player1 win")
elif player1_turns>player2_turns:
    print("Player2 win")
else:
    print("Game tie")