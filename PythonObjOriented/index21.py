#Exeption = An event that interrupt the flow of program
#           (zeroDivisonError,TypeError, ValueError)
#          1. Try  2.Except 3.Finally

try :
    number = int(input("Enter a number:"))
    print(1/number)

except ZeroDivisionError:
    print("You can't divide by zero IDIOT! ")

except ValueError:
    print("Enter only number please!")

finally:
    print("Do some clean up here")

