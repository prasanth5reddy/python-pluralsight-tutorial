from hello import student

# STRINGS
hello = 'hello\nworld'
print(hello)

# triple quoted string
triplequoted_hello = """hello
world"""
print(triplequoted_hello)
print(triplequoted_hello == hello)

planet = 'Pluto'
print(planet[1])
# planet[2] = m --this won't work

claim = "Pluto is a planet!"
datestr = '1956-01-31'

# split and join
print(claim.split())
year, month, day = datestr.split("-")
print("/".join([year, month, day]))

print(str(claim.startswith(planet)) + " " + str(claim.endswith("star")))

# Above print statement is cumbersome. Hence use format function
pluto_mass = 1.303 * 10 ** 22
earth_mass = 5.9722 * 10 ** 24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians."
      .format(planet, pluto_mass, pluto_mass / earth_mass, population, ))

# DICTIONARIES
print("id" in student)
# prints all the key value pairs. Better to use format function to print else type conversion errors may come
for s in student:
    print(f"{s} = {student[s]}")

# Another way of getting key value pairs
for key, value in student.items():
    print(f"{key.rjust(max([len(key) for key in student]))} is {value}")
