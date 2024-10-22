# -*- coding: utf-8 -*-
"""Part2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14cmdSan3tmT_OKaFokm4QkmnTweirRyD
"""

base = 10
height = 4
area = .5 * base * height
print (area)

length = 50
width = 80
perimeter = 2 * (length + width)
fence = perimeter / 15
print(fence)

cents = 835

dollars = cents // 100
cents %= 100

dimes = cents // 10
cents %= 10

quarters = cents // 25
cents %= 25

print("Total Amount:", 835, "cents")
print("Dollars:", dollars)
print("Dimes:", dimes)
print("Quarters:", quarters)

print("One")
print("  Two")
print("    Three")

name = input("What is your name? ")
print(f"Hello, {name} is a common name.\n")

file_path = "C:\\Users\\Documents\\MyFile.txt"
print(file_path)