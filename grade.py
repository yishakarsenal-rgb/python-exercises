score = float(input("enter score= "))

if score < 0 or score > 100:
    print("invalid score")
elif score >= 90:
    print("A+")
elif score >= 85:
    print("A")
elif score >= 80:
    print("A-")
elif score >= 75:
    print("B+")
elif score >= 70:
    print("B")
elif score >= 65:
    print("B-")
elif score >= 60:
    print("C+")
elif score >= 50:
    print("C")
elif score >= 40:
    print("D")
else:
    print("F")