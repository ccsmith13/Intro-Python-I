num = int(input("Enter a number: "))

for i in range(2,num):
    if (num % i == 0):
        print(num, "is not a prime number")
        print(i, "times", num//i, "is", num)
        break
    else:
        pass
else:
    print(num, "is a prime number")