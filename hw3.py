##CSC 4350 HW#3 - AugustineLi

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
print(question_one("area")) ##should return true
print(question_one("iota")) ##should return true

print(question_one("test")) ##should return false
print(question_one("hello")) ##should return false

print(question_one("ttee")) ##should return none
print(question_one("aaff")) ##should return none
