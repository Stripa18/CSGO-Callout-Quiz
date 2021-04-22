# First ever created and started on 03/04/2021
# Version 0.5, now the quiz will go on if you fail as a normal quiz will. At the end of the quiz, depending on your score, you will get a rank.
# Quiz based on the 2013 videogame Counter-Strike: Global Offensive made by Valve
# The videogame is a first-person shooter which has different maps, all of which has strategical spots players can be positioned in.
# Callouts are used to define these spots and to *call out* an enemy's position so that the team can attack and defeat that player.
# In the quiz, a spot will be described, and the user must enter the name of the callout in lowercase.
import time
score = 0
answer1 = ['shadows', 'shadow', 'dark']
answer2 = ['ticket', 'ticket booth']
answer3 = ['truck', 'van', 'car']
answer4 = ['tv', 'TV']
answer5 = ['jungle', 'Jungle', 'JUNGLE']
print("Welcome to the Callouts Quiz!")
time.sleep(1)
print("All answers must be entered in lowercase.")
time.sleep(2)
print("We are playing on Mirage.")
time.sleep(3)
print("After entering the A bombsite from ramp, to the left we have the other entrance which is in a higher ground, there is a ladder leading down, what is the name of the callout for the place that is under the ladder?")
if input() in answer1:
    print("That's correct!")
    score += 1
else:
    print("Incorrect!")
    score -= 1
time.sleep(1)
print("Next callout.")
time.sleep(2)
print("From the spawn of the Counter-Terrorist side, going to the right is a place where you can hide, take cover or peek to the A bombsite, what is the callout for this place?")
if input() in answer2:
    print("Correct! Good job.")
    score += 1
else:
    print("No! No!")
    score -= 1
time.sleep(1)
print("You're doing good. The next callout is...")
time.sleep(2)
print("In the B bombsite, in the top right corner when coming from the back, there is a vehicle right in front of apartments, Counter-Terrorist and Terrorist often hide there from the opposite team or CTs use It to go to apartments. How is that area called?")
if input() in answer3:
   print("Correct! Good job!")
   score += 1
else:
	print("Wrong...")
	score -= 1
time.sleep(2)
print("From the Terrorist spawn, If you go to B from the right instead of going through middle, you enter a building that connects Terrorist spawn and Side Alley, there is a spot to hide there in case you know an enemy is gonna come. How is that callout called?")
if input() in answer4:
    print("Wow! Nice knowledge. You are good at this!")
    score += 2
else:
    print("That is wrong.")
time.sleep(2)
print("Let's get on with the quiz.")
time.sleep(1)
print("This is an easy one.")
time.sleep(2)
print("Coming from Sniper's Nest/Window to the A bombsite, how is that callout called?")
if input() in answer5:
    print("Good!")
    score += 1
else:
    print("Come on, that was an easy one!")
# End of the quiz, there WILL be more questions and answers above though, this is just for the future.
time.sleep(1)
print("Good job on doing the quiz! Here is your final score...")
time.sleep(3)
print(score + " !")
if score <= 0:
    print("Yikes, you didn't do very well... You don't have a rank yet. Try again and practice more!")
