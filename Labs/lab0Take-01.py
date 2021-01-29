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
#############################################################################
import sys

#############################################################################
# This is main, where the program will be driven from
#############################################################################
DEFAULT_VALUE = 'n'
arg1 = sys.argv[1] if len(sys.argv) == 2 else DEFAULT_VALUE


try:
    #Your code starts here
    if arg1 == 'n':
        print('Hello World!')
    elif arg1 == 'r':
        print('World Hello!')

    print('Input n, r, or q:')
    userInput = input()
    if userInput == 'n':
        print('Hello World!')
    elif userInput == 'r':
        print('World Hello!')
        
    while userInput != 'q':
        print('Input n, r, or q:')
        userInput = input()
        if userInput == 'n':
            print('Hello World!')
        elif userInput == 'r':
            print('World Hello!')

    print('All done!')

except KeyboardInterrupt:
    print('\nShutting down ...')
