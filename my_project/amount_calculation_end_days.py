from my_project import monthcheck
import xlrd


def end_days_dr(end_month, end_year):
    book = xlrd.open_workbook("test.xlsx")
    sheet = book.sheet_by_name('Sheet3')
    days = monthcheck.month_check(end_month)
    numbers = (end_year, end_month, days, 0, 0, 0)
    for i in range(2, 271):
        date_cell = sheet.cell(i, 1)
        cell = xlrd.xldate_as_tuple(date_cell.value, book.datemode)
        if cell == numbers:
            if end_year >= 2008 and end_month >= 4:
                dr = sheet.cell(i, 3).value
                break
            else:
                dr = sheet.cell(i, 2).value
                break
    return dr


def end_days_interest(bp_diff, mr_diff, end_month, paydays2, end_year, interest_percent):
    dr = end_days_dr(end_month, end_year)
    dr_amt = bp_diff * dr
    total_amount = bp_diff + dr_amt + mr_diff
    pay_days = monthcheck.month_check(end_month)
    for_days = (total_amount * paydays2)/pay_days
    interest = (for_days*paydays2/365) * interest_percent/100
    interest = round(interest)
    return interest


