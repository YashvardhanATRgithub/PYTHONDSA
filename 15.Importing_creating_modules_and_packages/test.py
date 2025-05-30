from package.maths import *

print(addition(2,3))
print(substraction(4,2))

# remember that you can only import custom package while staying inside a directory which contains that package.
# you can not import a package if you are inside that package or outside the directory which contains that package


from package.subpackages import mult

print(mult.multiply(4, 5))