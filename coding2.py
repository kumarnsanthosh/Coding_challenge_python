# create a list of first 100 numbers
numbers = []
for i in range(1,101):
    numbers.append(i)
# from that list create list for all even numbers
even_numbers = []
for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)
print("even_numbers", even_numbers)

# create aa list for all odd numbers

odd_numbers = []
for n in numbers:
    if n % 2 == 1:
        odd_numbers.append(n)
print("odd_numbers :", odd_numbers)
# create a list for numbers that are divisible by both 3 and 5
div_num = []
for n in numbers:
    if n % 3 == 0 and n % 5 == 0:
        div_num.append(n)
print("divisble_numbers :",div_num)

