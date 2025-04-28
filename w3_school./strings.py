# 1 Write a one-line Python command to reverse this string
text = "hello world"  # define the string first
reversed_text = text[::-1]  # then reverse it
print(reversed_text)

# 2 You have two variables:
# name = "Alice"
# age = 30
# Write a string that says:
# "My name is Alice and I am 30 years old."
# using f-strings.
age = 30
name = "Alice"
txt = f"My name is {name}, and I am {age} years old"
print(txt)

# 3 Count how many times the letter "a" appears in the string
# "A cat and a hat sat at a mat."
txt = "A cat and a hat sat at a mat."

x = txt.count("a")
print(x)

# 4 Given: "OrderID: 12345; Status: Shipped" Extract only the 12345 from the string.

# 5 Given "   too     much   space   " remove extra space
messy = "   too     much   space   "
cleaned = " ".join(messy.split())
print(cleaned)




