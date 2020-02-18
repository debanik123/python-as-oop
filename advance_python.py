primelist = [x for x in range(50, 151) if not 0 in map(lambda z : x % z, range(2,x))]
print(primelist)
