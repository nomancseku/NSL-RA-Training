try:
    a = 1000
    b = int(input("Enter a divisor to divide 1000: "))
    print(a/b)
except ZeroDivisionError:
    print("You entered 0 which is not permitted!")



try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Type or value error occurred")


try:
    word = "spam"
    print(word / 0)
except:
    print("An error occurred")
