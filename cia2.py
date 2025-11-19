import sys

# If user does NOT give 3 parameters → use default values
if len(sys.argv) != 4:
    print("No parameters passed. Using default values...")
    price1 = 10
    price2 = 20
    price3 = 30
else:
    price1 = float(sys.argv[1])
    price2 = float(sys.argv[2])
    price3 = float(sys.argv[3])

minimum = min(price1, price2, price3)
maximum = max(price1, price2, price3)
average = (price1 + price2 + price3) / 3

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)
