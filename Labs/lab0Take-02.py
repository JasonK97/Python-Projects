#############################################################################
# Program:
#    Lab 0, Practice Lab Submission
#    Brother Jones, CSE354
# Author:
#    Jason Kent
# Summary:
#    This program when ran, prints 'Hello World!' by default, but will
#    print 'World Hello!' if the argv given in the command line is r.
#    Then it will ask the user for input that will determine the future
#    input, and with quit if q is entered, or if the user quits with 
#    Ctrl+C.
# Changes made to my code for the Lab 0 Take-2:
#   - Introduced a Dictionary with the values
#   - Deleted redundant code
#############################################################################
import sys

#############################################################################
# This is main, where the program will be driven from
#############################################################################
DEFAULT_VALUE = 'n'
arg1 = sys.argv[1] if len(sys.argv) == 2 else DEFAULT_VALUE


try:
    userInput = {   "n": "Hello World!", 
                    "r":"World Hello!"  } 
    helloMessage = userInput.get(arg1, False)
    if helloMessage != False: 
        print(helloMessage)

    while(helloMessage != False):
        user_input = str(input("Input n, r, or q: "))
        helloMessage = userInput.get(user_input, False)
        if helloMessage != False: 
            print(helloMessage)

    print('All done!')

except KeyboardInterrupt:
    print('\nShutting down ...')
