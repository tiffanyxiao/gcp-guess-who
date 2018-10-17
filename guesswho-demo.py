'''Between the following two commented lines is code to help you access
the API. There is only ONE part that you need to change, avoid changing
if possible.
-------------------------------------------'''
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    # CHANGE THE NAME OF THE FILE BELOW HERE TO MATCH YOUR IMAGE FILE NAME:
    'images/animals/it.jpg')

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
user_input = input("Please enter your guess for the animal:").lower()
# check if the input is correct
while(user_input != label):
    user_input = input("Oops. Thats wrong. Please try again:").lower()\
# if it is correct, tell the user
print("You got it! The answer is "+label+".")
