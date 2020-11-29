
from my_project import monthcheck
import xlrd


def staring_days_dr(start_month, start_year):
    book = xlrd.open_workbook("test.xlsx")
    sheet = book.sheet_by_name('Sheet3')
    numbers = (start_year, start_month, 1, 0, 0, 0)
    for i in range(2, 271):
        date_cell = sheet.cell(i, 0)
        cell = xlrd.xldate_as_tuple(date_cell.value, book.datemode)
        if cell == numbers:
            if start_year >= 2008 and start_month >= 4:
                dr = sheet.cell(i, 3).value
                break
            else:
                dr = sheet.cell(i, 2).value
                break
    return dr


def start_days_interest(bp_diff, mr_diff, start_month, paydays1, start_year, interest_percent):
    dr = staring_days_dr(start_month, start_year)
    dr_amt = bp_diff * dr
    total_amount = bp_diff + dr_amt + mr_diff
    pay_days = monthcheck.month_check(start_month)
    for_days = (total_amount * paydays1)/pay_days
    interest = (for_days*paydays1/365) * interest_percent/100
    interest = round(interest)
    return interest


