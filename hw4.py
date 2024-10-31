# -*- coding: utf-8 -*-
"""hw4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12WPYr6-I15qthmOLRiGcXkohXxctj8Qo
"""

def display_info():
  title = "The Hitchhiker's Guide to the Galaxy"
  author = "Douglas Adams"
  description = "A humorous science fiction series following the adventures of Arthur Dent."
  print(f"Title: {title}")
  print(f"Author: {author}")
  print(f"Description: {description}")

display_info()

def london_attractions():
  """Prints top attractions in London."""
  print("Top attractions in London:")
  print("- Buckingham Palace")
  print("- Tower Bridge")
  print("- British Museum")
  print("- London Eye")


def paris_attractions():
  """Prints top attractions in Paris."""
  print("Top attractions in Paris:")
  print("- Eiffel Tower")
  print("- Louvre Museum")
  print("- Arc de Triomphe")
  print("- Notre Dame Cathedral")


def new_york_attractions():
  """Prints top attractions in New York."""
  print("Top attractions in New York:")
  print("- Times Square")
  print("- Statue of Liberty")
  print("- Central Park")
  print("- Empire State Building")


# Call the functions to display the attractions
london_attractions()
print()  # Add an empty line for separation
paris_attractions()
print()
new_york_attractions()

!pip3 install ColabTurtle
from ColabTurtle.Turtle import *
initializeTurtle()

def draw_square():
    side_length = 100
    for _ in range(4):
        forward(side_length)
        right(90)

# Draw the first square
draw_square()

# Move the turtle to a new position for the second square
penup()
forward(150)
pendown()
draw_square()

# Move the turtle to a new position for the third square
penup()
backward(150)  # Move back to the starting line
right(90)      # Turn to face down
forward(150)   # Move down
left(90)       # Face right
pendown()
draw_square()

done()

def find_even_numbers():
    even_numbers = []
    for number in range(0, 11):
        if number % 2 == 0:
            even_numbers.append(number)
    print(even_numbers)

find_even_numbers()