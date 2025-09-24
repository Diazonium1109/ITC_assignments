#PROBLEM 1
import numpy as np

# roll dice 1000 times and generating random outputs for every roll
rolls = [np.random.randint(1, 7) for _ in range(1000)]
print("List of dice rolls\n", rolls)

# count frequency in dictionary
counts = {i: rolls.count(i) for i in range(1, 7)}

print("Dice roll frequencies:")
print(counts)



#PROBLEM 2
import random

# choose password length
n = int(input("Enter a number: "))

# define characters
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
specials = "^!@$%&*"

# pick at least one from each
password = [
    random.choice(uppercase),
    random.choice(lowercase),
    random.choice(digits),
    random.choice(specials)
]

# fill the rest with random picks from all characters
all_chars = uppercase + lowercase + digits + specials
for i in range(n - 4):
    password.append(random.choice(all_chars))

# shuffle so it’s not predictable
random.shuffle(password)

# join into string
password = "".join(password)

print("Generated password:", password)



#PROBLEM 3
import random
x, y = 0, 0

# Define directions
# 1 - up
# 2 - down
# 3 - left
# 4 - right
for i in range(50):
    step = random.randint(1,4)
    if (step == 1):
        y = y + 1
    elif (step == 2):
        y = y - 1
    elif (step == 3):
        x = x - 1
    else:
        x = x + 1

print("The final position after 50 moves is:", x, y)
