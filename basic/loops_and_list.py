nums = [1, 2, 4, 8, 16]
for i in range(len(nums)):
    nums[i] = nums[i] * 2
print(nums)

# loop over elements and index of a list
nums = list(range(10))
for i, num in enumerate(nums):
    if num % 2 == 1:
        nums[i] = num * 2

print(nums)
# when enumerate converted to list it will be a list of tuples with tuple size 2.
# first element in tuple is index and second is element
print(list(enumerate(nums)))
# enumerate tuple is analogous to .as_integer_ratio() function
numerator, denominator = 0.5.as_integer_ratio()
print(f"numerator : {numerator} and denominator : {denominator}")

# List Comprehensions
squares = [n ** 2 for n in range(10)]
print(squares)
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loud_short_planets)
nums = [-3, -2, -5, 1, 2, 3]
# two ways to count number of negatives
print("Number of negatives")
print(len([num for num in nums if num < 0]))
print(sum([num < 0 for num in nums]))
# nice way of printing list with separator
print(*[num for num in nums], sep=',')
