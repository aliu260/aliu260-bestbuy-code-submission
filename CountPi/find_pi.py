import sys

print ("Now counting from:")
print (str(sys.argv[1]))

# assign names of input and output file from command line arguments
pi_string = str(sys.argv[1])
# output_file = str(sys.argv[2])

source = open(pi_string, "r")


# initialize values
found = False
i = 0
isPalindrome = True
isPrime = True
foundNum = 0
foundIndex = 0

# read from file
pi = source.read()
source.close()

# strip decimal point from pi string
pi = pi[0:1] + pi[2:]

while not found:
    # take next 7 digit substring
    temp = pi[i:i+7]
    # print(temp)
    # check if palindrome
    for j in range(len(temp)//2):
        if temp[j] != temp[j * (-1) - 1]:
            isPalindrome = False
    # check primality
    if (isPalindrome):
        piNum = int(temp)
        if ((piNum % 2 == 0) or (piNum % 3 == 0)):
            isPrime = False
        else:
            # use 6k +- 1
            k = 5
            while k * k <= piNum:
                if piNum % k == 0 or piNum % (k + 2) == 0:
                    isPrime = False
                k += 6
        if isPrime and isPalindrome:
            found = True
            foundNum = piNum
            foundIndex = i
    # reset values for next iteration
    isPalindrome = True
    isPrime = True
    i += 1

print('The first 7 digit palindrome in the digits of pi is:')
print(foundNum)
print(f'at index: {foundIndex}')


print("End of program.")
