### a welcome message with a backstory
print("Welcome captain to the Stellar Phoenix!")
print("Your mission is to find the all-powerful tesseracts.")
print("Finding it will save humanity's energy crisis.")
print("You are in the middle of the Black Eye Galaxy.")
print("There are five abandoned ships in front of you.")
print("You can choose 'Starlight Voyager', 'Nebula Explorer', 'Celestial Odyssey',")
##Scenario Descriptions: Each ship choice leads to a unique scenario
##with descriptive text, adding depth to the game world and 
##engaging the player's imagination.
print("'Galactic Titan', and 'Infinity Serenity'.")
print("Now pick a ship to go to, captain, but be careful for danger lurks.")

# Create a variable to store the user's choice
### Prompt user for a choice
shipChoice = input("> ")

if shipChoice == "Starlight Voyager":
    print("You enter the Starlight Voyager.")
    print("As you walk in, you see a Zyglorbax roaming around the storage room.")
    print("Do you sneak around the Zyglorbax or leave the ship?")
    print("Type 'sneak' or 'leave'.")
    zyglorbaxChoice = input("> ")

    if zyglorbaxChoice == "sneak":
        print("You attempt to sneak to the storage room, but the Zyglorbax is alerted, ")
        print("due to a text notification on your phone, and it rips you to pieces.")
        print("You are now dead.")
    elif zyglorbaxChoice == "leave":
        print("You decide to not explore the Starlight Voyager.")
        print("You turn around and leave the spaceship safely.")
    else:
        print("Invalid choice. Please enter sneak or leave.")

elif shipChoice == "Nebula Explorer":
    print("You chose to go into the Nebula Explorer.")
    print("As you walk in, you see some supply crate on the table.")
    print("Do you want to open the crate?")
    print("Type 'yes' or 'no'.")
    caseChoice = input("> ")

    if caseChoice == "yes":
        print("You open the crate and find a pile of bones!")
    elif caseChoice == "no":
        print("You decide not to open the shiny case.")
        print("As you turn to leave, you hear a cracking sound coming from the corner.")
        print("A dark figure with glowing red eyes launches at you, knocking you unconscious.")
        print("You wake up in your bed. It was all a dream.")
    else:
        print("Invalid choice. Please enter yes or no.")

elif shipChoice == "Celestial Odyssey":
    print("You chose to go into the Celestial Odyssey.")
    print("As you walk in, you see the ship has Cryogenic Chambers")
    print("Do you want to open the Cryogenic Chambers?")
    cryChoice = input("> ")

    if cryChoice == "yes":
        print("You open the Cryogenic Chambers and find frozen expired food!")
    elif cryChoice == "no":
        print("You decide not to open the Cryogenic Chambers.")
        print("As you turn to leave, your arm itches, and you notice a spider bite.")
        print("You are now dead.")
    else:
        print("Invalid choice. Please enter yes or no.")

elif shipChoice == "Galactic Titan":
    print("You chose to go into the Galactic Titan.")
    print("As you walk in, you see other humans on the ship.")
    print("Do you want to interact with them?")
    interactChoice = input("> ")
    if interactChoice == "yes":
        print("You decide to interact with the humans.")
        print("You walk up them and ask about the tesseracts.")
        print("They tell you they have been searching for the tesseracts for years.")
        print("But, they also need it for there own people to they kill you.")
        print("You are now dead.")
      
    elif interactChoice == "no":
        print("You choose not to interact with the humans.")
        print("You turn around and go towards your ship.")
    else:
        print("Invalid choice. Please enter yes or no.")
elif shipChoice == "Infinity Serenity": 
        print("You chose to go into the Infinity Serenity.")
        print("As you walk in, you see a glowing blue orb.")
        print("Do you want to touch the orb?")
        touchChoice = input("> ")
        if touchChoice == "yes":
          print("You touch the orb and it turns into a cube.")
          print("You realise it is the tesseracts.")
          print("You have won and saved humanity!")
        elif touchChoice == "no" :
          print("You decide not to touch the orb.")
          print("As you leave, you hear a cracking sound coming from the corner.")
          print("The orb becomes unstable and blows up.")
          print("You are now dead.")
      
###Error Handling:included error handling for invalid user inputs, 
###prompting the player to enter a valid choice.
else:
    print("Invalid choice. Please enter a valid ship name.")
