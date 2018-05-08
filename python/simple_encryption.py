# Python 3
# *****  NOTE: works with BYTE strings ONLY ***** 
import sys

DEBUG = False

k = b"NexmoRocks"
m = b"Nexmo is looking to hire good people."

def reduce (c):

    while c > 126:
        c = c - 95
    return c    

def expand (c):

    while c < 32:
        c = c + 95
    return c

def encrypt (k, m):

    es = b"" # es = encrypted byte string 
    kl = len(k) # Length of key byte string
    i = 0 # index into key byte string
    for c in m:
        # Encrypt char
        e = c + k[i]
        e = reduce (e)
        if DEBUG == True:
            print ("k is `%c` e is `%c` %d" % (k[i], e, e))    
        es = es + e.to_bytes(1, byteorder='little')
        # Reset key index if required
        i = i + 1
        if i > (kl - 1):
            i = 0
        
    return es

def decrypt (k, m):

    ds = b"" # ds = decrypted string
    kl = len(k) # Length of key string
    i = 0 # index into key string
    for c in m:
        # decrypt char
        e = c - k[i] # subtract for decrypt 
        e = expand(e)
        ds = ds + e.to_bytes(1, byteorder='little')        
        # Reset key index if required
        i = i + 1
        if i > (kl - 1):
            i = 0
            
    return ds

if (sys.version_info < (3, 0)):
    print ("Python version 3 and above only - join the future!!")
    exit(-1)

em = encrypt(k, m)
print (em)

dm = decrypt (k, em)
print (dm)

# For Testing only below

if DEBUG == True:
    s = "=k2{ ryw,u[}z($r#imxh&.}0[yvq4Vu)r0cus|!T4"
    em = s.encode('ascii')
    dm = decrypt (k, em)
    print (dm)

    print(reduce (127))
    print(reduce (145))
    print(reduce (126))

