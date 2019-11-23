
def my_func(count=4):
    for i in range (1, 5):
        print("count", count)
        if count == 2:
            print("count", count)
        count = count - 1

my_func()
