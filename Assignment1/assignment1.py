# Variables and Input

# 1. Create a variable my_age and assign your age to it. Print a message using this variable.
my_age= 20
print("I am ", my_age ,"years old.")

# 2. Ask the user to enter their favorite food and print a message incorporating this input.
fav_food = input("Enter your favourite food:")
print("Favourite Food is:" ,fav_food)

# Type Conversion:

# 1. Convert the string "42" to an integer and print the result
st="42"
print("the integer is",int(st))


num = int("42")
print(num)

num1 = int("40")
num2 = 50
print("Sum=" ,num1+num2)

# 2. Convert the floating-point number 3.14159 to a string and print the result.
floating_pt = str(3.14159)
print(floating_pt)


# Strings:

# 1. Concatenate strings
result = "Hello" + " World!"
print(result)

text = f"{'Hello'} {'World!'}"
print(text)

# 2. Use string indexing to extract the third character from the string "Python".
third_char = "Python"[2]  
print(third_char)

word = "Python"
print(word[2])

# 3. Take a sentence as input and print only the first five words.

sentence = input("Enter a sentence: ")
words = sentence.split()
print(" ".join([words[i] for i in range(min(5, len(words)))]))

sentence = input("Enter a sentence: ")
print(*sentence.split()[:5])

sentence = input("Enter a sentence: ")
words = sentence.split()
first_five = words[:5]
print(" ".join(first_five))

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# print(" ".join(words[:5]))


