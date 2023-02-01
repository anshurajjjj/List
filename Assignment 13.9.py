#Write a Python script to create a list of city names taken from the user.
n = int(input("Enter the length of list: "))
list = []
for i in range(n):
    city = input("Enter the names of city:")
    list.append(city)

print("Names of city are: ", list)
