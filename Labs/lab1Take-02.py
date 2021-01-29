#############################################################################
# Program:
#    Lab 1, Learning Some Python
#    Brother Jones, CSE354
# Author:
#    Jason Kent
# Summary:
#    This program will read in a file of assembly code
#    and then proceed to translate it into machine code
#    and write the output to a file with the correct 
#    instructions.
#############################################################################




#############################################################################
# 
# Changes made to my code for the Lab 1 Take-2:
#   - Made the Program be able to run a test without a cmd line argument
#   - Added one more removal of any blank strings in my final array
#      as to make the "out of range" error go away.
#
#############################################################################
import sys
import os
DEFAULT_VALUE = 'ECEN160_test1.txt'

#############################################################################
# This is main, where the program will be driven from
#############################################################################
filepath = sys.argv[1] if len(sys.argv) == 2 else DEFAULT_VALUE

if not os.path.isfile(filepath):
    print("File path {} does not exist.".format(filepath))
    input("Press Enter to Exit... ")
    sys.exit()

with open(filepath) as fp:
    try:
        data = fp.read().replace(',', '')
        data = data.replace('\n', ' \n ')
        dataArray = data.split(' ')
        for x in dataArray:
            if x == '':
                dataArray.remove(x)
        for x in dataArray:
            if x == '':
                dataArray.remove(x)
        
        replacements = {'LD':'1', 
                        'MOV': '2',
                        'DISP':'30', 
                        'ADD':'7', 
                        'NOP': '0000',
                        'r0':'0',
                        'r1':'1', 
                        'r2':'2', 
                        'r3':'3', 
                        'r4':'4',
                        'r5':'5',
                        'r6':'6',
                        'r7':'7',
                        'r8':'8'}
        newArray = []
        for y in dataArray:
            newArray.append(replacements.get(y, y))

        newString = ''.join([str(element) for element in newArray])

        finalArray = newString.split('\n')
        for x in finalArray:
            if x == '':
                finalArray.remove(x)
        for y in finalArray:
            if y[0] == '1':
                y = y[:2] + '0' + y[2]
                print(y)
            elif y[0] == '2':
                y = y[:3] + '0'
                print(y)
            else:
                print(y)

    finally:
        input("Press Enter to Exit... ")
        fp.close()