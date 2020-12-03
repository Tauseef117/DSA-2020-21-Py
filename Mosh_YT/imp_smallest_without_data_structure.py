largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    else:
        try:
            n=int(num)
            if smallest is None: #******
                smallest=n
            if n>largest:
                largest=n
            elif n<smallest:
                smallest=n
        except:
            print('Invalid input')
            continue
print("Maximum is", largest)
print("Minimum is", smallest)