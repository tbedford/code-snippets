# This is a slightly weird looking Python idiom that I have see quite
# a few times now. It's now how I would do things but it is common and
# probably the "Python way"

# Make a new list from a list
list1 = ['Hello', 'Goodbye', 'Pythonesque']
list2 = [len(c) for c in list1]

print(list2)
