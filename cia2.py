import sys

# Check if exactly 3 command-line arguments are given
if len(sys.argv) == 4:
    price1 = float(sys.argv[1])
    price2 = float(sys.argv[2])
    price3 = float(sys.argv[3])
else:
    print("No proper parameters given. Please enter values manually...")
    price1 = float(input("Enter price1: "))
    price2 = float(input("Enter price2: "))
    price3 = float(input("Enter price3: "))

# Calculate minimum, maximum, and average
minimum = min(price1, price2, price3)
maximum = max(price1, price2, price3)
average = (price1 + price2 + price3) / 3

# Display results
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)
