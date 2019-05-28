def shift(c, n):
    asc=ord(c)
    asc += n
    if asc > 122:
        return chr(asc - 25)
    else:
        return chr(asc)

print('c shifted 2 positions', shift('c', 2))
print('w shifted 4 positions', shift('w', 4))
