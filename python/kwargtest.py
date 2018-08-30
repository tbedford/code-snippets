def pkwargs1(**kwargs):
    print(kwargs)

def pkwargs2(**kwargs):
    for key, value in kwargs.items():
        print("Key:{} -- Value:{}".format(key, value))

    
pkwargs1 (kw1='Shark', kw2='Angelfish', kw3='Nudibranch')
pkwargs2 (kw1='Shark', kw2='Angelfish', kw3='Nudibranch', kw4='Dolphin')

