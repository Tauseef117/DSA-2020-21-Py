# Tauseef Ahmed-4SF17CS173


def sumofsquares(m):
    for i in range(m):
        for j in range(m):
            if i ** 2 + j ** 2 == m:
                print("True")
                exit(0)
    else:
        print("False")


num = int(input("Enter number"))
if (num > 0):
    sumofsquares(num)
else:
    print("False")
