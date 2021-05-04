# First ever created and started on 03/04/2021
# Version 0.5, now the quiz will go on if you fail as a normal quiz will. At the end of the quiz, depending on your score, you will get a rank.
# Quiz based on the 2013 videogame Counter-Strike: Global Offensive made by Valve
# The videogame is a first-person shooter which has different maps, all of which has strategical spots players can be positioned in.
# Callouts are used to define these spots and to *call out* an enemy's position so that the team can attack and defeat that player.
# In the quiz, a spot will be described, and the user must enter the name of the callout in lowercase.
# Callouts from https://totalcsgo.com/callouts/
import time
score = 0
show_tip_end = False
answer1 = ['shadows', 'shadow', 'dark', 'Shadows', 'SHADOWS', 'Shadow', 'SHADOW', 'Dark', 'DARK']
answer2 = ['ticket', 'ticket booth', 'Ticket', 'TICKET', 'Ticket booth', 'Ticket Booth', 'TICKET BOOTH']
answer3 = ['truck', 'van', 'car', 'Truck', 'TRUCK', 'Van', 'VAN', 'Car', 'CAR']
answer4 = ['tv', 'TV', 'Tv']
answer5 = ['jungle', 'Jungle', 'JUNGLE']
answer6 = ['sneaky', 'Sneaky', 'SNEAKY']
yes = ['yes', 'Yes', 'YES', 'ye', 'Ye', 'YE', 'Y', 'y', 'sure', 'Sure', 'SURE', 'Yep', 'yep', 'YEP']
no = ['no', 'No', 'NO', 'nop', 'Nop', 'NOP', 'nope', 'Nope', 'NOPE', 'nah', 'Nah', 'NAH', 'N', 'n']
answer7 = ['tetris', 'Tetris', 'TETRIS']
answer8 = ['triple box', 'triple_box', 'Triple box', 'Triple_box', 'TRIPLE_BOX', 'TRIPLE BOX', 'triple', 'Triple', 'TRIPLE', 'triple stack', 'triple_stack', 'Triple stack', 'Triple Stack', 'Triple_stack', 'Triple_Stack', 'TRIPLE STACK', 'TRIPLE_STACK']
answer9 = []
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
if score <= 0:
    print("You're doing poorly.. The next callout is...")
if score == 2:
    print("You are doing pretty good!")
if score >= 0:
    print("You're doing alright.")
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
    score -= 1
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
    score -= 1
time.sleep(2)
print("This is a harder one. When coming from CT Spawn to B, in Market/Shop, what is the position which is on top of the fridge agaisnt the wall?")
if input() in answer6:
    print("Great job! That is some nice knowledge in callouts.")
    score += 1
else:
    print("Wrong. That is okay though! People don't use this callout that much.")
    score -= 1
time.sleep(1)
print("If you wanna do better now, I'll be kind and give you a tip about the next callouts, BUT, you will lose a score point. Do you want it?")
if input() in yes:
    print("Alright! The tip is that the next callouts are on A or entering A. I will notify you when the callouts are not related to A.")
    score -= 1
    show_tip_end = True
if input() in no:
    print("Sure! Let's get on with the quiz then.")
time.sleep (3)
print("This is an easy and common one.")
time.sleep(2)
print("In front of A Ramp, there is a stack of boxes and square stone clusters which people can hide behind.")
time.sleep(1)
print("What's the callout called like?")
if input() in answer7:
    print("Correct.")
    score += 1
else:
    print("Incorrect! Bad, bad...")
    score -= 1
time.sleep(2)
print("This time, I will make It hard! I will not tell you where the callout is, rather how It looks.")
time.sleep(1)
print("Get ready.")
time.sleep(3)
print("A triple set of boxes players can hide behind and peek to enemies coming.")
if input() in answer8:
    print("I see you know the common callouts for people to be in well, that's good.")
    score += 1
else:
    print("Wrong. This is a common place for people to be in, It's in A. Come on. Let's continue.")
    score -= 1
time.sleep(2)
print("This is the hardest question! If you get this one right you will obtain triple the points!")
time.sleep(3)
print("An small alcove between two stacks of boxes, that is often left unchecked by Terorrists.")
if input() in answer9:
    time.sleep(1)
    print("Holy moly! You got It right...? I can't believe It! Wonderful, wonderful. You must have a good knowledge of the callouts. You have obtained triple the points. Let's continue.")
    score += 3
else:
    print("Oh, that's okay, don't worry about It. It was very hard to get It right unless you knew the bombsite.")
    score -= 1
# End of the quiz, there WILL be more questions and answers above though, this is just for the future.
time.sleep(1)
print("Good job on doing the quiz! Here is your final score...")
time.sleep(3)
print(score)
if score <= 0:
   print("Yikes, you didn't do very well... You don't have a rank yet. Try again and practice more!")
