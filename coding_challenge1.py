sub1 = 78
sub2 = 85
sub3 = 92
sub4 = 74 
sub5 = 88
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total_marks/500 * 100
print(f"Total marks = {total_marks}/500")
print(f"percentage = {round(percentage, 1)}%")
if percentage >= 90 and percentage <= 100:
    print("Grade A+")
elif percentage >= 80 and percentage <= 89:
    print("Grade A")
elif percentage >= 70 and percentage <= 79:
    print("Grade B")
elif percentage >= 60 and percentage <= 69:
    print("Grade C")
elif percentage >= 50 and percentage <= 59:
    print("Grade D")
else:
    print("Grade F")