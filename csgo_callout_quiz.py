# First ever created and started on 03/04/2021
# Quiz based on the 2013 videogame Counter-Strike: Global Offensive made by Valve
# The videogame is a first-person shooter which has different maps, all of which has strategical spots players can be positioned in.
# Callouts are used to define these spots and to *call out* an enemy's position so that the team can attack and defeat that player.
# In the quiz, a spot will be described, and the user must enter the name of the callout in lowercase.
import time
score = 0
print("Welcome to the Callouts Quiz!")
time.sleep(1)
print("All answers must be entered in lowercase.")
time.sleep(2)
print("We are playing on Mirage.")
time.sleep(2)
print("After entering the A bombsite from ramp, to the left we have the other entrance which is in a higher ground, there is a ladder leading down, what is the name of the callout for the place that is under the ladder?")
if input() == "shadows":
    print("That's correct!")
    score += 1
    time.sleep(1)
    print("Next callout.")
    time.sleep(2)
    print("From the spawn of the Counter-Terrorist side, going to the right is a place where you can hide, take cover or peek to the A bombsite, what is the callout for this place?")
    if input() == "ticket":
        print("Correct! Good job.")
        score += 1
        time.sleep(1)
        print("You're doing good. The next callout is...")
        time.sleep(2)
        print("In the B bombsite, in the top right corner when coming from the back, there is a vehicle right in front of apartments, Counter-Terrorist and Terrorist often hide there from the opposite team or CTs use It to go to apartments. How is that area called?")
        if input() == "truck":
            print("Correct! Good job!")
            score += 1
        else:
            print("That is not the right answer. Try again.")
    else:
        print("Wrong. Try again.")
else:
    print("Incorrect! Try again.")
