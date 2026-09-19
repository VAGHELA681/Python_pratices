#What is the difference between == and is?
#Answer:
#== checks whether values are equal.
#is checks whether two variables refer to the same object.

a = [1, 2]
b = [1, 2]

print(a == b)  # True
print(a is b)  # False
