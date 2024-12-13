name = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age)

age += 1

print(f"Hello {name}!")
print(f"You are {age} years old!")

print("input 2 integers")

age1, age2 = map(int, input().split())

print(f"The numbers: {age1} {age2}")
