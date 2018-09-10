# stdout
print("Hello World\n")
# print without new line
print("Hello ", end='')
print("Universe")

# data types
answer: float = 2.6
print(answer)
print("answer = " + f"{answer}\n")

# booleans
is_python = True
data = None
print(int(is_python), data, "\n")

# conditions
number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is not 5")
if None:
    print("None executable")
a = 1
b = 2
var = "a is bigger" if a > b else "b is bigger"
print(var, "\n")

# lists similar to Arrays
names = ["Hello", "Hi", "How"]
print(f"{names[0]} " + names[-2])
names[1] = "Hey"
names.append(2)
del names[1]
print(f"{names} and length = {len(names)}")
print("What" in names)
print(names[1:-1], "\n")

# loops
# for
for name in names:
    print(f"name is {name}")
print("Other way of for loop")
# range(5, 10, 2) is same as [5, 7, 9]
for i in range(1, len(names), 1):
    print(f"name is {names[i]}")
# while
x = 5
while x < 10:
    print(f"x = {x}")
    x += 1
print()

# break and continue
student_names = ["John", "Mary", "Sean", "Paul", "Emma"]
for name in student_names:
    if name == "Paul":
        print("Found " + name)
        break
    elif name == "Mary":
        print("Skipping " + name)
        continue
    print("Testing " + name)
print()

# dictionaries similar to Map/JSON
student = {
    "first_name": "John",
    "id": 1,
    "grade": "A"
}
print(student["first_name"] + " " + student.get("last_name", "Terry"))
print("Keys " + str(student.keys()) + "\n" + "Values " + str(student.values()))
del student["grade"]
student["id"] = 2
print("Keys " + str(student.keys()) + "\n" + "Values " + str(student.values()) + "\n")

# exceptions
student["last_name"] = "Walker"
try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("last_name not found")
except TypeError as error:
    print("numbered_last_name cannot be evaluated")
    print(error)
print()

# other data types ( long only in python2 )
complex_example: complex = 1235.6788
tuple_example: tuple = (1, 2, "Sam")
set_example = {3, 2, 3, 1, 5, 2}
frozen_set_example = frozenset([3, 2, 3, 1, 5, 2])  # immutable, can be used as keys for dictionaries
print(complex_example, tuple_example, set_example, frozen_set_example)
