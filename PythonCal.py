#Output to show the user options
print("Select Operations.")
print("""
1.Add
2.Subtract
3.Mutipliy
4.Divide
""")


#try:
    #val = int(choice)
#except ValueError:
    #print("That's not an int!")
#make sure the cal. keeps going
while True:
#Ask user for input
    firstNumber = float(input("Enter first number: "))
    secondNumber = float(input("Enter second number: "))


#Options for the menu
    choice = int(input("Enter choice (1/2/3/4): "))
    if choice == 1:
        #sum += firstNumber + secondNumber
        #print(sum)
        print(firstNumber + secondNumber)
    elif choice == 2:
        #sum -= firstNumber - secondNumber
        #print(sum)
        print(firstNumber - secondNumber)
    elif choice == 3:
        #sum *= firstNumber * secondNumber
        #print(sum)
        print(firstNumber * secondNumber)
    elif choice == 4:
        #sum /= firstNumber / secondNumber
        #print(sum)
        print(firstNumber / secondNumber)
    else:
        break
        print("Finish")