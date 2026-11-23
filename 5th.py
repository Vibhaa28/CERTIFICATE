marks=int(input("enter the marks:"))
if marks>100 or marks<0:
    print("invlid marks")
elif marks>=90:
    print("a grade")
elif marks>=88:
    print("b grade")
elif marks>=70:
    print("c grade")
elif marks>=60:
    print("d grade")
else:
    print("false")