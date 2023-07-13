# Program to checkmleap year

def check_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, 'is a leap year')
            else:
                print(year, 'is not a leap year')
        else:
            print(year, 'is a leap year')
    else:
        print(year, 'is not a leap year')

check_leap(2000)