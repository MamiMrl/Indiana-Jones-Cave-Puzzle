print("Welcome to Indiana Jones's Death Cave.\n")
print("Your mission is to find the Golden Liberty Statue.\n") 

input("You have entered inside of the Death Cave. Press any key to continue.\n")

pathway = input("You have a pathway in front of you you have two options: Right or Left?\n")

lowerCase_pathway = pathway.lower()

if lowerCase_pathway == "right":
    print("You have encountered with a giant ball coming towards you very fast!! You're Dead, Game Over.\n")
elif lowerCase_pathway == "left":
    print("Looks like you're on the safe path... Keep going.\n")

    jump_or_Ladder = input("You have two options in front of you: Jump to the other side or Use ladders to go down. Be careful... it's gonna be a long jump. Options: Jump or Ladder.\n")

    lower_Jump_Or_Ladder= jump_or_Ladder.lower()
    
    if lower_Jump_Or_Ladder == "ladder":
        print("The ladder was slippery and you are falling into a pit! You're Dead, Game Over.\n")
    elif lower_Jump_Or_Ladder == "jump":
        print("You made a Huge Jump, Great! You are safe. For now...\n")

        three_doors = input("You have three plates in front of you which will take you to an end. Select wisely... Options: Red, Blue or Yellow.\n")
        lower_three_doors = three_doors.lower()

        if lower_three_doors == "red":
            print("You have made a terrible choice and you have fallen into Lava Lake! You're Dead. Game Over.\n")
        elif lower_three_doors == "blue":
            print("You have made an unlucky choice and you have fallen into Lake with Crocodiles! You're Dead. Game Over.\n")
        elif lower_three_doors == "yellow":
            print('''
  (
(_)
###       .
(#c    __\|/__
 #\     wWWWw
 \ \-. (/. .\)
 /\ /`\/\   /\
 |\/   \_) (_|
 `\.' ; ; `' ;`\
   `\;  ;    .  ;/\
     `\;    ;  ;|  \
      ;   .'  ' ;  /
      |_.'   ;  | /)
      (     ''._;/`
      |    ' . ;
      |.-'   .:)
      |        |
      (  .'  : |
      |,-  .:: |
      | ,-'  .;|
     _/___,_.:_\_
    [I_I_I_I_I_I_]
    | __________ |
    | || |  | || |
   _| ||_|__|_|| |_
  /=--------------=\
 /                  \
|                    |
|____________________|
''')

            print("Congradulations you have made the right choice and you have found the Golden Statue of Liberty. You Rock!")

    else:
        print("Looks like you have confused, please use valid commands.")

else:
    print("Looks like you have confused, please use valid commands.")



