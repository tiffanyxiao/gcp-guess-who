'''Between the following two commented lines is code to help you access
the API. There is only ONE part that you need to change, avoid changing
if possible.
-------------------------------------------'''
import io
import os
import random

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# list of all possible animals
animals = ["elephant", "cat", "fish", "dog", "koala", "panda"]
animal = animals[random.randint(0,6)]

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    # CHANGE THE NAME OF THE FILE BELOW HERE TO MATCH YOUR IMAGE FILE NAME:
    'images/animals/'+animal+'.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

# get FIRST label of the labels
label = labels[0].description
'''-------------------------------------------
Code below this line is for the actual guessing game, feel free to edit'''

# ask the user for their input
print("Hello! Welcome to Guess Who by the Amazing Tiffany.")

# score keeper
score = 4
number_of_hints = 1

user_input = input("Please enter your guess for the animal:").lower()
# check if the input is correct
while(user_input != label):
    score -= 1
    if (score == 0):
        print("Oops sorry! You guessed wrong too many times. You lost! The word was "+label)
        break
    # create a hint
    hint = labels[number_of_hints].description
    number_of_hints += 1
    while (label in hint):
        number_of_hints += 1
        hint = labels[number_of_hints].description
    print("Oops. Thats wrong. \nHere's a hint:")
    print(hint)
    user_input = input("Please try again:").lower()
# if it is correct, tell the user
if (score != 0):
    print("You got it! The answer is "+label+". Your score is "+str(score))
