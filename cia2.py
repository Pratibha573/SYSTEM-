import sys

# If user gives 3 parameters → convert them
if len(sys.argv) == 4:
    price1 = float(sys.argv[1])
    price2 = float(sys.argv[2])
    price3 = float(sys.argv[3])
else:
    print("No proper parameters given. Using default values...")
    price1 = 10
    price2 = 30
    price3 = 20.00

minimum = min(price1, price2, price3)
maximum = max(price1, price2, price3)
average = (price1 + price2 + price3) / 3

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)
