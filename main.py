from multiprocessing.connection import wait
from time import sleep
from numpy.random import choice
from turtle import hideturtle



which_box = input("what box would you like to open; wonderland, medieval, breakfast, space, bot, safari, aquatic, dino,spooky, blizzard, spring, lovely, lucky ") #asks what box
how_many = int(input("how many boxes would you like to open ")) #asks how many boxes to open
how_long_between_boxes = float(input("how long would you like btween boxes, i.e. 1 would be 1 second, can not go below 0.1 ")) #how long between boxes
which_box = which_box.lower() #turns uppercase to lowwercase

if which_box == "wonderland": #which box you chose
        for _ in range(how_many): #loops how many boxes you chose
            character = ["Two of spades", "Eat Me", "Drink Me", "Alice", "Queen of Hearts", "Dormouse", "White Rabbit", "Cheshire Cat", "Caterpillar", "Mad Hatter", "King of Hearts"] #the different items you can get
            character = choice(
                character, 1, p=[0.152, 0.15, 0.15, 0.15, 0.15, 0.065, 0.065, 0.065, 0.025, 0.025, 0.003]) #how likely something is, 1 = 100% and 0.5 = 50%
            print(character) #prints what character whats chosen
            sleep(how_long_between_boxes) #waits the time you chose between boxes before repeating itself


if which_box == "medieval":
    for _ in range(how_many):
        character = ["Elf", "Witch", "Wizard", "Fairy", "Slime Monster", "Jester", "Dragon", "Queen", "Unicorn", "King"]
        character = choice(
            character, 1, p=[0.134, 0.134, 0.134, 0.134, 0.134, 0.09, 0.09, 0.09, 0.05, 0.01,])
        print(character)
        sleep(how_long_between_boxes)


if which_box == "breakfast":
    for _ in range(how_many):
        character = ["Toast", "Cerial", "Yogurt", "Breakfast Combo", "Orange Juice", "Milk", "Waffle", "Pancakes", "French Toast", "Pizza"]
        character = choice(
            character, 1, p=[0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.09, 0.09, 0.05, 0.02,])
        print(character)
        sleep(how_long_between_boxes)


if which_box == "space":
    for _ in range(how_many):
        character = ["Earth", "Meteor", "Stars", "Alien", "Planet", "UFO", "Spaceship", "Astronaut", "Colored Astronaut"]
        character = choice(
            character, 1, p=[0.1875, 0.1875, 0.1875, 0.1875, 0.1, 0.1, 0.045, 0.0045, 0.0005,])
        print(character)
        sleep(how_long_between_boxes)


if which_box == "bot":
    for _ in range(how_many):
        character = ["Lil Bot", "Lovely Bot", "Angry Bot", "Happy Bot", "Watson", "Buddy Bot", "Brainy Bot", "Mega Bot",]
        character = choice(
            character, 1, p=[0.195, 0.195, 0.195, 0.195, 0.09, 0.09, 0.037, 0.003,])
        print(character)
        sleep(how_long_between_boxes)


if which_box == "safari":
        for _ in range(how_many):
            character = ["Panda", "Sloth", "Tenerec", "Flamingo", "Zebra", "Elephant", "Lemur", "Peacock", "Chamelon", "Lion", "Rainbow Panda"]
            character = choice(
                character, 1, p=[0.15, 0.15, 0.15, 0.15, 0.15, 0.07, 0.07, 0.07, 0.0348, 0.005, 0.0002])
            print(character)
            sleep(how_long_between_boxes)


if which_box == "aquatic":
        for _ in range(how_many):
            character = ["Old Boot", "Jellyfish", "Clownfish", "Frog", "Crab", "Pufferfish", "Blobfish", "Octopus", "Narwhal", "Baby Shark", "Megladon"]
            character = choice(
                character, 1, p=[0.15, 0.15, 0.15, 0.15, 0.15, 0.068, 0.068, 0.068, 0.039, 0.005, 0.002])
            print(character)
            sleep(how_long_between_boxes)


if which_box == "Safari":
        for _ in range(how_many):
            character = ["Amber", "Dino Egg", "Dino Fossil", "Stegosaurus", "Velociraptor", "Brontosaurus", "Triceratops", "Tyrannosaurus Rex",]
            character = choice(
                character, 1, p=[0.195, 0.195, 0.195, 0.195, 0.09, 0.09, 0.037, 0.003])
            print(character)
            sleep(how_long_between_boxes)

if which_box == "spooky":
        for _ in range(how_many):
            character = ["Pumpkin", "Swamp Monster", "Frankenstein", "Vampire", "Zombie", "Mummy", "Werewolf", "Ghost", "Haunted Pumpkin",]
            character = choice(
                character, 1, p=[0.185, 0.185, 0.185, 0.185, 0.1015, 0.1015, 0.05, 0.0065, 0.0005,])
            print(character)
            sleep(how_long_between_boxes)

if which_box == "blizzard":
        for _ in range(how_many):
            character = ["Snow Globe", "Holiday Gift", "Hot Chocolate", "Holiday Wreath", "Gingerbread Man", "Gingerbread House", "Snowman", "Santa Claus", "Frost Wreath", "Troical Globe",]
            character = choice(
                character, 1, p=[0.185, 0.185, 0.185, 0.185, 0.1015, 0.1015, 0.05, 0.0065, 0.0005,])
            print(character)
            sleep(how_long_between_boxes)

if which_box == "spring":
        for _ in range(how_many):
            character = ["Spring Frog",]
            character = choice(
                character, 1, p=[1,])
            print(character)
            sleep(how_long_between_boxes)

if which_box == "lovely":
        for _ in range(how_many):
            character = ["Lovely Frog",]
            character = choice(
                character, 1, p=[1,])
            print(character)
            sleep(how_long_between_boxes)

if which_box == "lucky":
        for _ in range(how_many):
            character = ["lucky Frog",]
            character = choice(
                character, 1, p=[1,])
            print(character)
            sleep(how_long_between_boxes)


