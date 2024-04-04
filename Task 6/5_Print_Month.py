# Month Name Printer: Print Month name by input number of month example: input 1 print January

month = {
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"
}
#Display month
month_number = int(input("\nInput the number of the month: "))
if month_number in month:
    print("\nMonth: ", month[month_number])
else:
    print("\nInvalid month number, please input the number between 1-12")