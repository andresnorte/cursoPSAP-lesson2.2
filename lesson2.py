def isYearLeap(year):

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def daysInMonth(year, month):
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    if month in month_31:
        return 31
    elif month == 2:
        if isYearLeap(year):
            return 29
        else:
            return 28
    elif month > 12 or year < 1582:
        return None
    else:
        return 30

print(daysInMonth(2000, 11))

def dayOfYear(year, month, day):
    if (12 <= month or month <= 1) or day >= 31 or day <= 1:
        return None
    else:
        return True


print(dayOfYear(2000, 12, 31))






