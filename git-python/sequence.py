n = int(input("Enter the length of the sequence: ")) # Do not change this line
sequence = 0
x1 = 1
x2 = 2
x3 = 3
if n > 0:
    print(1)
if n > 1:
    print(2)
if n > 2:
    print(3)
if n > 3:
    for x in range(0,n-3):
        sequence = x1 + x2 + x3
        print(sequence)
        x1 = x2
        x2 = x3
        x3 = sequence




print(sequence)
