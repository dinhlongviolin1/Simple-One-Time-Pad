# RMIT University Vietnam
# Nguyen Dinh Long - s3804737
# Simple One - Time Pad Implementation
import random

# Support Functions
def string2bits(s=''):
    """
    Convert ascii characters to arrays of strings of ascii binaries
    Reference: tmthydvnprt, stackoverflow. Accessed on December 1st, 2020 [https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa]
    """
    return [bin(ord(x))[2:].zfill(8) for x in s]

def bits2string(b=None):
    """
    Convert arrays of strings of ascii binaries to ascii characters
    Reference: tmthydvnprt, stackoverflow. Accessed on December 1st, 2020 [https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa]
    """
    return ''.join([chr(int(x, 2)) for x in b])

def stringXOR(s1, s2):
    """
    Perform xor on two string with the same length (my own code)
    """
    if len(s1) != len(s2):
        raise Exception("The length of two strings is different")
    else:
        return ''.join([str(int(s1[i]) ^ int(s2[i])) for i in range(0, len(s1))])

def generateKeyArray(length=0):
    """
    Generate random binary key based on the given number of ascii characters (my own code)
    """
    return [(''.join(str(random.randint(0, 1)) for i in range(0, 8))) for i in range(0, length)]

def arrayToString(arr, delimeter=''):
    """
    Convert string to array with specify delimeter (my own code)
    """
    return delimeter.join(arr)

def is8bitBinaryArrays(arr):
    """
    Sanity Check for decoding input. Check to see if the inputs are 8 bits binary (my own code)
    """
    a = True
    for x in arr:
        # Check length (8 bit)
        if len(x) != 8:
            a = False
            break
        # Check every characters in each input to see if the characters is binary
        for c in x:
            if c not in '10':
                a = False
                break
    return a

# Switch Case Function for main program
def encoding():
    """
    Encoding case for the program
    """
    # Get message string
    str = input("Enter your message: ")
    # generate key
    key = generateKeyArray(len(str))
    # Convert message to binary
    strBinaries = string2bits(str)
    strEncoded = []
    # Perform xor encoding operation for all values
    for i in range(0, len(strBinaries)):
        strEncoded.append(stringXOR(strBinaries[i], key[i]))
    # Print out key and encoded message
    print("Your key is:")
    print(arrayToString(key, " "))
    print("Your encoded binary is:")
    print(arrayToString(strEncoded, " "))

def decoding():
    """
    Decoding case for the program
    """
    # Get key and perform splting with delimeter=" " to convert to list
    key = input("Enter your binary key: ").strip().split(" ")
    # Get binary encoded message and perform splting with delimeter=" " to convert to list
    strBinaries = input("Enter your binary message: ").strip().split(" ")
    # Perform sanity check for input
    if is8bitBinaryArrays(strBinaries) and is8bitBinaryArrays(key) and len(strBinaries) == len(key):
        strDecoded = []
        # Perform xor decoding operation for all values
        for i in range(0, len(strBinaries)):
            strDecoded.append(stringXOR(strBinaries[i], key[i]))
        # print out the encoded message
        print("Your encoded message is:")
        print(arrayToString(bits2string(strDecoded)))
    else:
        invalidInput()

# Invalid input case
def invalidInput():
    print("Input is invalid!")

# Execute options
def execute(x):
    return {
        "1": encoding,
        "2": decoding,
    }.get(x, invalidInput)

# Main Function
# Execute the main funciton only if it is run directly, not through import
if __name__ == "__main__":
    print("Welcome to this simple One Time Pad program!")
    execute(input("Enter 1 for encoding, 2 for decoding: "))()
    print("Program is exiting!")


