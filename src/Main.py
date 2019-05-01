number = int(input("Enter any integer "))
changedNumber = number  # Creates an integer to be manipulated.
numberHalf = int(number/2)  # Integers cannot be divided by a number less than 2 for it's prime factorization.
count = 2
factorization = ""

if number > 0:
    while count <= numberHalf:
        if changedNumber % count == 0:
            factorization = factorization + str(count) + " * "  # Adds the prime to the string.
            changedNumber = int(changedNumber / count)  # Divides out the chosen prime.
            numberHalf = int(changedNumber / 2)  # Changes number of integers tested not to test useless numbers.
            count = 2
        else:
            count += 1

elif number < 0:  # Repeats previous while loop for negative integers.
    factorization = ""
    while count <= -numberHalf:
        if changedNumber % count == 0:
            factorization = factorization + str(count) + " * "
            changedNumber = int(changedNumber / count)
            numberHalf = int(changedNumber / 2)
            count = 2
        else:
            count += 1

factorization = factorization + str(changedNumber)  # Adds leftover prime to the string.
print("\nThe prime factorization of " + str(number) + " is\n" + factorization + "\n")
if factorization == str(0):  # checks if input number is 0.
    print(factorization + " is not a prime number.")
elif str(number) == factorization:  # checks if input number is a prime.
    print(str(number) + " is a prime number.")
else:
    print(str(number) + " is not a prime number.")
