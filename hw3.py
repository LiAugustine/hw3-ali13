import math
import pathlib
import os
import shutil

##CSC 4350 HW #3 - AugustineLi

##Question 1 function
def question_one(str):
  
  vowelCount = 0
  consonantCount = 0

  vowels = set("aeiouAEIOU") ##set which contains vowels, lowercase and uppercase

  for alphabet in str:
    if alphabet in vowels: ##if letter in str is a vowel
      vowelCount = vowelCount + 1 ##increment vowel count
    else: ##if not a vowel, has to be a consonant
      consonantCount = consonantCount + 1 


  if (vowelCount > consonantCount): ##more vowels than consonants
    return True
  elif (consonantCount > vowelCount): ##more consonants than vowels
    return False

  return None ##equal vowels and consonants
  
##Test cases
print('Question 1 Test Cases:')
print(question_one("area")) ##should return true
print(question_one("iota")) ##should return true

print(question_one("test")) ##should return false
print(question_one("hello")) ##should return false

print(question_one("ttee")) ##should return none
print(question_one("aaff")) ##should return none
print()

##Question 2 Function
def question_two(R, H): ##two inputs, radius and height
  cylinderVolume = math.pi * H * R * R ##math.pi = pi value
  return 'The volume of a cylider with radius ' + str(R) + ' and height ' + str(H) + ' is ' + str(cylinderVolume) ##clear return statement. must use str() to convert number into string to properly concatenate

print('Question 2 Test Cases:')
print(question_two(2, 2)) ##should be 25.13
print(question_two(3, 4)) ##should be 113.1
print()

##Question 3 Function
def question_three(list): 
  singleString = ', '.join(list) ##joins into one string
  return singleString
print('Question 3 Test Cases:')
print(question_three(["One", "Two", "Three"]))
print(question_three(["123", "456", "789"]))
print()

##Question 4 Function

def question_four(listOfLists):
  row = [''.join(list) for list in listOfLists] ##each list within the list of lists becomes a string 
  ##create outputFile.txt if it does not already exist (a+), if already exists it is appeneded
  with open('outputFile.txt', 'a+') as outputFile: 
    ##data = outputFile.read()
    for list in row: ##for list in row
      outputFile.write("[" + list + "]") ##write it to the file
    outputFile.write("\n")
    outputFile.truncate()
    outputFile.seek(0)
    path = pathlib.Path(__file__).parent.absolute() ##path of current working directory
    return "Path is " + str(path) + "/" + outputFile.name + " which contains the row " + outputFile.read()
  
print('Question 4 Test Cases:')
print(question_four([["one, two, three"], ["four, five, six"] ]))
print(question_four([["four, five, six"], ["one, two, three"]  ]))
print()

##Question 5 Function, works with multiple lines
def question_five(filename):
  with open(filename) as file:
    return "The list of list of the CSV is " + str(file.read().splitlines()) ##each line is split into a list

print('Question 5 Test Cases:')
print(question_five('/home/runner/hw3-1/outputFile.txt'))
print()
  
##Question 6 Function
def question_six(num1, num2):
  try:
    return num1/num2 ##try returning num1/num2
  except ZeroDivisionError: 
    return None ##return None

print('Question 6 Test Cases:')
print(question_six(6,3))
print(question_six(6,0))
print()

##Question 7 Function
def question_seven(intList):
  from collections import OrderedDict
  ##print("Original list: " + str(intList))
  newList = list(OrderedDict.fromkeys(intList)) ##remembers the order that keys were inserted
  return "Original list: " + str(intList) + "\nNew list: " + str(newList) 

print('Question 7 Test Cases:')
print(question_seven([1, 2, 3, 3, 3, 4]))##[1, 2, 3, 4]
print(question_seven([1, 2, 3, 2, 5, 6, 6, 5, 1]))##[1, 2, 3, 5, 6]
print()

def question_eight(dirName): ##take directory name
  currentDir = os.getcwd() ##get current working directory
  fullPath = os.path.join(currentDir, dirName)

   ##make sure folder does not already exist
  if not os.path.exists(fullPath): 
    os.mkdir(fullPath, 0o666) ##0o666 = default mode
  else:
    shutil.rmtree(fullPath)   ##deletes the folder if it already exists        
    os.mkdir(fullPath, 0o666)
  
  return "Directory named " + dirName + " created."

print('Question 8 Test Cases:')
print(question_eight("TestDir"))
print(question_eight("TestDir")) ##test for duplicate
print(question_eight("AnotherDir"))
