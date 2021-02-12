import openpyxl

# read in a .xlsx file
book = openpyxl.load_workbook("./coordinates.xlsx")

# set active worksheet
sheet = book.active

coordinatedictionary = {}

# for x in 

a2 = sheet['A2']
b2 = sheet['B2']
a3 = sheet['A3']
b3 = sheet['B3']
a4 = sheet['A4']
b4 = sheet['B4']

# This is how you can get the values of each cell.
# print(a2.value, b2.value, a3.value, b3.value)

# Formula from https://stackoverflow.com/questions/2579535/convert-dd-decimal-degrees-to-dms-degrees-minutes-seconds-in-python
def decdeg2dms(dd):
   is_positive = dd >= 0
   dd = abs(dd)
   minutes,seconds = divmod(dd*3600,60)
   degrees,minutes = divmod(minutes,60)
   degrees = degrees if is_positive else -degrees
   return (degrees,minutes,round(seconds, 6))


print('Latitude values: ' + str(decdeg2dms(a2.value)) + ' : ' + str(decdeg2dms(a3.value)) + ' : ' + str(decdeg2dms(a4.value)))
print('Longitude values: ' + str(decdeg2dms(b2.value)) + ' : ' + str(decdeg2dms(b3.value)) + ' : ' + str(decdeg2dms(b4.value)))