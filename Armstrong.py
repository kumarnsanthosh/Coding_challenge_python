#1. Write a Python program to check whether a given number is an Armstrong number or not.


num = int(input("Enter the number to check the number is Armstrong number or not :"))
digit = 0
n = num
while num > 0:
    mod = num % 10
    digit += 1
    num = num // 10
sum = 0
b = n
while n > 0:
    mod = n % 10
    power = mod ** digit
    sum += power
    n = n // 10
if b == sum:
    print(b, 'is Armstrong number')
else:
    print(b, "is not Armstrong number")

#2. Write a program that prints all Armstrong numbers in a given range.
n_range = int(input("Enter the range:"))
for i in range(n_range):
    dgt = 0
    num1 = i
    while i > 0:
        mod = i % 10
        dgt += 1
        i = i // 10
    sm = 0
    num2 = num1
    while num1 > 0:
        mod = num1 % 10
        pwr = mod ** dgt
        sm += pwr
        num1 = num1 // 10
    if sm == num2 and sm > 10:
        print(sm, 'is Armstrong number')

        