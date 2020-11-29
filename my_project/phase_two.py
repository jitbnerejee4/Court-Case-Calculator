import xlrd
import datetime


def period_calculation(year1, month1, day1):
    i = 1
    count = 1
    #numbers = (1998, 4, 1, 0, 0, 0)
    numbers = (year1, month1, day1, 0, 0, 0)
    book = xlrd.open_workbook("test.xlsx")
    sheet = book.sheet_by_name('Sheet4')
    while True:
        date_cell = sheet.cell(i, 0)
        cell = xlrd.xldate_as_tuple(date_cell.value, book.datemode)
        if cell == numbers:
            break
        else:
            i += 1
    while True:
        cur_dr = sheet.cell(i, 2).value
        nex_dr = sheet.cell(i + 1, 2).value
        cur_dr = float(cur_dr)
        nex_dr = float(nex_dr)
        if cur_dr != nex_dr:
                dr = cur_dr
                dr_end_date = xlrd.xldate_as_tuple(sheet.cell(i, 1).value, book.datemode)
                new_start_date = xlrd.xldate_as_tuple(sheet.cell(i + 1, 0).value, book.datemode)
                return dr, dr_end_date, new_start_date, count
        elif sheet.cell(i, 2).value == sheet.cell(i + 1, 2).value:
                count += 1
                i += 1


def pension(bp, mr, interest_percent, year1, month1, day1, year2, month2, day2, paymonths):
    date1 = datetime.datetime(year1, month1, day1)
    date2 = datetime.datetime(year2, month2, day2)
    start_dates = [date1]
    end_dates = []
    interest_list = []
    total_interest = 0
    while date1 <= date2:
        dr, dr_end_date, new_start_date, months = period_calculation(year1, month1, day1)
        dr_amt = bp * dr
        total = round(bp + dr_amt + mr)
        if months > paymonths:
            months = paymonths
        year1 = new_start_date[0]
        month1 = new_start_date[1]
        day1 = new_start_date[2]
        temp_year = dr_end_date[0]
        temp_month = dr_end_date[1]
        temp_day = dr_end_date[2]
        temp_date = datetime.datetime(temp_year, temp_month, temp_day)
        if temp_date >= date2:
            end_dates.append(date2)
        else:
            end_dates.append(temp_date)
        date1 = datetime.datetime(year1, month1, day1)
        start_dates.append(date1)
        months2 = paymonths - months + 1
        total_sum = 0
        for i in range(months2, paymonths+1):
            total_sum += i
        paymonths = months2 - 1
        interest1 = (total * interest_percent/100)
        interest = round(interest1 * total_sum/12)          # MAY BE NEEDED TO CHANGE THE ROUND FUNCTION
        interest_list.append(interest)
        total_interest += interest
    return total_interest, start_dates, end_dates, interest_list
