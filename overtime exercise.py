try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    if hours > 40:
        overtime = hours - 40
        pay = (40 * rate) + (overtime * rate * 1.5)
    else:
        pay = hours * rate

    print("Pay:", pay)

except:
    print("Error, please enter numeric input")