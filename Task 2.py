# Initialize an empty list to store user inputs
a = []

# Take input from the user for a list of size 10
print("Enter Your Numbers in List")
for i in range(10):
    a.append(int(input("list[%d] Number:" % (i + 1))))

# Text for result
text = "Result"

# Display the result header with dashes
print(text)
print("-" * len(text))

# Check each number in the list and print whether it's even or odd
for i in range(10):
    if a[i] % 2 == 0:
        print("list[%d] Number is Even: %d" % (i + 1, a[i]))
    else:
        print("list[%d] Number is Odd: %d" % (i + 1, a[i]))
