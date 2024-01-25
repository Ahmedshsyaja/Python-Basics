# Function to calculate the area of a rectangle
def Calculate_area(length, width):
    return length * width

# Function to calculate the volume of a rectangular prism
def Calculate_volume(length, width, height):
    return length * width * height

# Display a header for the AutoCleaner program
print("AutoCleaner")

# Underline the header with dashes
text = "AutoCleaner"
print("-" * len(text))

# Take user input for length, width, and height
length = float(input("Enter The Length: "))
width = float(input("Enter The Width: "))
height = float(input("Enter the Height: "))

# Calculate area and volume using the defined functions
area = Calculate_area(length, width)
volume = Calculate_volume(length, width, height)

# Display the calculated area and volume
print("Area: %f" % area)
print("Volume: %f" % volume)

# Print a message indicating that cleaning starts
print("Cleaning Starts...")
