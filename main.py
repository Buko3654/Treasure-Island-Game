print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
turn = input("You have reached a fork in the path. Which way would you like to go? L for left or R for right.\n")
if turn == "L":
  lake = input("You reach a large lake with an island in the center. Would you like to Swim to the island or Wait for a boat?\n")
  if lake == "Wait":
    door = input("You get to the island and see a large house with three doors. One door is Red, one Yellow, and one Blue. Which door would you like to enter?\n")
    if door == "Red":
      print("You enter the room that smells a bit smoky. After a few steps the door closes behind you and the room fills with fire. Game Over.")
    elif door == "Blue":
      print("You enter a room with open kennels. After a few steps the door closes behind you and you're eaten by beasts. Game Over.")
    elif door == "Yellow":
      print("You enter a room that's dim with the exception of a large pillar of light shining down in the center of the room. In the pillar, you see an old chest. You found the treasure! You Win!")
    else:
      print("The owner of the house finds you as you're messing with doors and hauls you off to the police for being a thief. Game Over.")
  else:
    print("You are attacked by an unbelievably angry trout. Game Over.")
else:
  print("You fall into a deep hole and can't climb out. Game Over.")
