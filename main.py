import os


from utils.add import add

print(add(1, 2))

base_path = os.path.dirname(__file__)
full_path = os.path.join(base_path, 'data', "example.txt")

with open(full_path, "r") as file:
    print(file.read())

