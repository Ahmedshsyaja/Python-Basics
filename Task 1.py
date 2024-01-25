#User to input the number
#Input Number should be taken int
a = int(input("Input your Number : "))
#if the input number is factor then a%5 should be zero else it is not
if a % 5 == 0:
    print("Input number is factor of 5")
else:
    print("Input number is not a factor of 5")