num_int = int(input("Input a number: "))
max_int = num_int

while num_int >= 0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:
        max_int = num_int
    else:
        max_int
print("The maximum is ", max_int)