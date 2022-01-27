import math
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
  singleString = ", ".join(list) ##joins into one string
  return singleString
print('Question 3 Test Cases:')
print(question_three(["One", "Two", "Three"]))
print(question_three(["123", "456", "789"]))
print()


