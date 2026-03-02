try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    pay = hours * rate
    print("Pay:", pay)

except ValueError:
    print("Error, please enter numeric input")