def encrypt(message, key):
    letter = message
    new = ''
    for c in letter:
        n = ord(c)
        if n == 32:
            w = chr(n)
            new += w
        elif n + key > 122:
            n -= 25
            w1 = chr(n)
            new += w1
        elif n + key < 122 and n + key > 97:                 
            w = chr(n)
            new += w
        else:
            w2 = chr(n)
            new += w2
    return new 

message = str(input("enter a message "))
key = int(input("enter offset key "))
word = encrypt(message, key)

print(word)
