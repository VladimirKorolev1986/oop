f = 'koro..x@gmail.com'

for i in range(len(f)-1):
    if f[i] != '.' and f[i+1] != '.':
        print(True)
    else:
        print(False)
