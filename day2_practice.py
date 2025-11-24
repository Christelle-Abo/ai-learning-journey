# Day 2: Python Fundamentals

print("=== LISTS ===")
# Lists are ordered collections - like arrays
fruits = ["apple", "banana", "orange"]
print("My fruits:", fruits)
print("First fruit:", fruits[0])  # Index starts at 0
print("Last fruit:", fruits[-1])  # -1 means last item

# Adding and removing
fruits.append("mango")  # Add to end
print("After adding:", fruits)

# Looping through lists
print("\nAll fruits:")
for fruit in fruits:
    print(f"  - {fruit}")


print("\n=== DICTIONARIES ===")
# Dictionaries store key-value pairs
person = {
    "name": "Sarah",
    "age": 28,
    "city": "Lagos"
}

print("Name:", person["name"])
print("Age:", person["age"])

# Add new key-value pair
person["job"] = "Engineer"
print("Updated person:", person)

# Loop through dictionary
print("\nAll person info:")
for key, value in person.items():
    print(f"  {key}: {value}")


print("\n=== LOOPS ===")
# For loop with range
print("Count to 5:")
for i in range(1, 6):  # range(1, 6) means 1,2,3,4,5
    print(i)

# While loop
print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Done!")


print("\n=== CONDITIONALS ===")
# If-elif-else
age = 25
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# Checking if item in list
if "apple" in fruits:
    print("We have apples!")


print("\n=== PRACTICE PROBLEMS ===")

# Problem 1: Find sum of list
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Sum of {numbers} = {total}")

# Problem 2: Find even numbers
all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in all_numbers:
    if num % 2 == 0:  # % is modulo - checks remainder
        even_numbers.append(num)
print(f"Even numbers: {even_numbers}")

# Problem 3: Count occurrences
words = ["cat", "dog", "cat", "bird", "cat", "dog"]
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(f"Word counts: {word_count}")