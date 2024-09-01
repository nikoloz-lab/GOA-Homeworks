#სიაში შეინახეთ 5 რიცხვი, შემდეგ კი დარპინტეთ პირველი და მეოთხე ელემენტების ნამრავლი.

def printValues():
    # Create an empty list 'l'
    l = list()
    # Loop from 1 to 20 (inclusive)
    for i in range(1, 21):
        # Calculate the square of 'i' and append it to the list 'l'
        l.append(i**2)
    # Print the first 5 elements of the list 'l'
    print(l[:5])
    # Print the last 5 elements of the list 'l'
    print(l[-5:])

# Call the printValues function to execute it
printValues()