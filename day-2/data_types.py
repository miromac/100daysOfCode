# Data types

# String

# Prints "H"
print("Hello"[0])
# Prints "123456"
print("123" + "456")

# Integer

print(123 + 456)
# Large Integers
123_456_789

# Float

3.14159

# Boolean

True
False

# Type conversion

num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = str(123)
print(type(a))

# print(70 + float("100.5")) 170.5
# print(str(70) + str(100))  70100

two_digit_number = input("Type a two digit number: ")
print(type(two_digit_number))
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
print(first_digit)
print(second_digit)
result = int(first_digit) + int(second_digit)
print(result)

# Mathematical operations

print(type(6/2)) # 2.0 float
print(type(2 ** 3))  # 8 int

# Pemdas
# () ** * / + -

# Number manipulation

print(8 / 3)        # 2.6666666666
print(int(8 / 3))   # 2
print(round(8 / 3)) # 3
print(round(8 / 3, 2)) # 2.67
print(round(2.66666666, 2)) # 2.67
print(8 // 3) # 2 floor division

# f-string

score = 0
height = 1.8
isWinning = True
print(f"Your score is {score}, height is {height}, winning is {isWinning}")
