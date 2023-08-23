print("------------------Welcome To Basic Calulator--------------------")
print("Enter These Words For Calculation\n A to Add\n B to Subtract\n C to multiply\n D to Divide")
input0 = input("Select the letter: ")
input1 = int(input("Enter the first value you want to calculate: "))
input2 = int(input("Enter the second value you want to calculate: "))

if input0 == 'A':

    print("Addition of your number is = ", input1 + input2)#(,=concat ho joslai chai seperator ho and eukai thau print garxa)
elif input0 == 'B':
     print("Subtraction of your number is = ", input1 - input2)
elif input0 == 'C':
    print("Multipication of your number is = ", input1 * input2)
elif input0 == 'D':
    print("Division of your number is = ", input1 / input2)
else:
    print("Something is wrong on your operation")

    # kusum magar