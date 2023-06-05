def number_generator(n):
    for i in range(n):
        yield i

# Using the generator
gen = number_generator(5)
print(gen)
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
print(next(gen))  # Output: 4
