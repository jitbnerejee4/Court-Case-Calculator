import datetime
from my_project import monthcheck

# Calculating months, days


def start_days_calculation(month1, day1, year1):
    output = monthcheck.month_check(month1)
    days_in_first_month = day1
    if 1 < day1 <= output:
        month1 += 1
        day1 = 1
        pay_days1 = output-days_in_first_month+1
        if month1 > 12:
            month1 = 1
            year1 += 1
    else:
        pay_days1 = 0
    return pay_days1, month1, day1, year1


def end_days_calculation(month2, day2, year2):
    output = monthcheck.month_check(month2)
    pay_days2 = day2
    if 1 < day2 < output:
        month2 -= 1
        if month2 == 0:
            month2 = 12
            year2 -= 1
        day2 = monthcheck.month_check(month2)
    elif day2 == output:
        pay_days2 = 0

    return pay_days2, month2, day2, year2


def pay_months_calculation(year1, month1, day1, year2, month2, day2):
    date1 = datetime.datetime(year1, month1, day1)
    date2 = datetime.datetime(year2, month2, day2)
    pay_months = (date2.year - date1.year) * 12 + (date2.month - date1.month)
    return pay_months + 1

