# exception= events detected duringexecution that interrupt the flow of a program.

try:
    numerator=int(input("enter the numerator-"))
    denominator=int(input("enter the denominators-"))
    res=numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("you can't divide by zero")
except ValueError as e:
    print(e)
    print("enter number only")
except Exception as e:
    print(e)
    print("Something went wrong")
else:
    print(res)
finally:
    print("this will always execute")