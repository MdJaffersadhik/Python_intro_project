# Personal Introduction Program

print("👋 Welcome! Let's create your personal introduction.\n")

# Asking questions with validation
name = ""
while name == "":
    name = input("What is your name? ").strip()
    if name == "":
        print("Name cannot be empty. Please enter your name.")

age = ""
while age == "":
    age = input("How old are you? ").strip()
    if age == "":
        print("Age cannot be empty. Please enter your age.")

hobby = ""
while hobby == "":
    hobby = input("What is your favorite hobby? ").strip()
    if hobby == "":
        print("Hobby cannot be empty. Please enter a hobby.")

city = ""
while city == "":
    city = input("Which city do you live in? ").strip()
    if city == "":
        print("City cannot be empty. Please enter your city.")

fav_food = ""
while fav_food == "":
    fav_food = input("What is your favorite food? ").strip()
    if fav_food == "":
        print("Favorite food cannot be empty. Please enter something.")

# Displaying the output
print("\n========================================")
print(f"🎉 Welcome, {name}! 🎉")
print("----------------------------------------")
print(f"You are {age} years old and love {hobby}.")
print(f"You live in {city} and your favorite food is {fav_food}.")
print("========================================\n")

print("Thanks for sharing! Keep coding and exploring. 💡")
