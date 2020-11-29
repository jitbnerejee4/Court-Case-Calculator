
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os
from tkcalendar import dateentry
from datetime import datetime
from my_project import period_check, phase_two, amount_calculation_starting_days, amount_calculation_end_days
import fpdf
try:
    master = tk.Tk()
    master.geometry("900x600")
    master.title("Court Case Calculator by J.I.T")
    master.iconbitmap('icon.ico')

    path = '@%s' % os.path.join(os.environ['WINDIR'], 'Cursors/arrow_r.cur').replace('\\', '/')
    master.configure(cursor=path)

    image1 = ImageTk.PhotoImage(Image.open("biswa-bangla.png"))
    panel1 = tk.Label(master, image=image1)
    panel1.grid(row=0, column=2)
    panel1.image = image1

    var = tk.StringVar()
    v = tk.IntVar()

    tk.Label(master, text="Select for which Interest will be paid", font=("Times New Roman", 12, "bold")). \
        grid(row=7, column=0)


    def choice():
        input1 = (var.get())
        if input1 == "Arrear":

            root = tk.Toplevel(master)
            root.geometry("900x600")
            root.title("Court Case Calculator by J.I.T")
            root.iconbitmap('icon.ico')

            path = '@%s' % os.path.join(os.environ['WINDIR'], 'Cursors/arrow_r.cur').replace('\\', '/')
            root.configure(cursor=path)

            image2 = ImageTk.PhotoImage(Image.open("biswa-bangla.png"))
            panel2 = tk.Label(root, image=image2)
            panel2.grid(row=0, column=3)
            panel2.image = image2

            a1 = tk.Label(root, text="Basic", pady=20, font=("Times New Roman", 12, "bold"))
            a1.grid(row=10, column=1)

            a2 = tk.Label(root, text="Medical Relief", pady=20, padx=10, font=("Times New Roman", 12, "bold"))
            a2.grid(row=10, column=3)

            a3 = tk.Label(root, text="Interest Percentage", pady=20, padx=10, font=("Times New Roman", 12, "bold"))
            a3.grid(row=11, column=2)

            a4 = tk.Label(root, text="From", pady=20, padx=10, font=("Times New Roman", 12, "bold"))
            a4.grid(row=12, column=1)

            a5 = tk.Label(root, text="To", pady=20, padx=10, font=("Times New Roman", 12, "bold"))
            a5.grid(row=12, column=3)

            o1 = tk.Label(root, text="TOTAL INTEREST PAYABLE", pady=20, padx=10, font=("Times New Roman", 15, "bold"))
            o1.grid(row=13, column=2)

            basic_text = tk.IntVar()
            e1 = tk.Entry(root, textvariable=basic_text, bd=3)
            e1.grid(row=10, column=2)

            mr_text = tk.IntVar()
            e2 = tk.Entry(root, textvariable=mr_text, bd=3)
            e2.grid(row=10, column=4)

            interest_text = tk.IntVar()
            e3 = tk.Entry(root, textvariable=interest_text, bd=3)
            e3.grid(row=11, column=3)
            current_date = datetime.now()

            op1 = tk.Entry(root, bd=3)
            op1.grid(row=14, column=2)

            cal = dateentry.DateEntry(root, width=12, year=current_date.year, month=current_date.month,
                                  day=current_date.day, background='darkblue', foreground='white',
                                  selectbackground="red", normalbackground="pink", borderwidth=2, font="helvetica")
            cal.grid(row=12, column=2, padx=10, pady=10)

            cal2 = dateentry.DateEntry(root, width=12, year=current_date.year, month=current_date.month,
                                   day=current_date.day, background='darkblue', foreground='white',
                                   borderwidth=2, selectbackground="red", normalbackground="light green",
                                   font="helvetica")
            cal2.grid(row=12, column=4, padx=10, pady=10)

            def arrear_calculator():
                try:
                    bp = int(e1.get())
                    mr = int(e2.get())
                    interest_percent = int(e3.get())
                    date_entry1 = cal.get_date()
                    date_entry2 = cal2.get_date()
                    year1 = date_entry1.year
                    month1 = date_entry1.month
                    day1 = date_entry1.day
                    year2 = date_entry2.year
                    month2 = date_entry2.month
                    day2 = date_entry2.day

                    paydays1, new_start_month, new_start_day, new_start_year = period_check.start_days_calculation(month1, day1, year1)
                    if paydays1 >= 1:
                        interest_start_days = amount_calculation_starting_days.start_days_interest(bp, mr, month1, paydays1,
                                                                                           year1, interest_percent)
                    else:
                        interest_start_days = 0

                    paydays2, new_end_month, new_end_day, new_end_year = period_check.end_days_calculation(month2, day2, year2)
                    interest_end_days = amount_calculation_end_days.end_days_interest(bp, mr, month2, paydays2, year2,
                                                                              interest_percent)
                    paymonths = period_check.pay_months_calculation(new_start_year, new_start_month, new_start_day, new_end_year,
                                                            new_end_month, new_end_day)
                    interest_for_months, start_dates_list, end_dates_list, interest_list = \
                        phase_two.pension(bp, mr, interest_percent, new_start_year, new_start_month, new_start_day, new_end_year,
                                                new_end_month, new_end_day, paymonths)
                    round(interest_for_months)

                    total_interest = round(interest_start_days + interest_end_days + interest_for_months)
                    op1.insert(0, total_interest)

                    pdf = fpdf.FPDF(format='letter')
                    pdf.add_page()
                    pdf.set_font("Arial", size=12)
                    pdf.write(5, f"Calculation Sheet of Interest due to delayed payment of Interest on Arrear. "
                                 f"In pursuance of Order dated..........................passed by the "
                                 f"Honourable Justice.......................................... of Calcutta High Court "
                                 f"and communicated to this end by  Sri/Smt.................................. Advocate "
                                 f"for the Petitioner. WP No.....(W) of 20.... in the matter of ....................."
                                 f"......................................( Petitioner ) Vs the State of West Bengal "
                                 f"& Others. Amount on which Interest is payable Rs.........................../- for "
                                 f"Arrear. Rate of Interest payable Rs. {interest_percent}%\n\n\n")
                    length = interest_list.__len__()
                    for i in range(0, length):
                        pdf.write(5, f"From {start_dates_list[i]} to {end_dates_list[i]} :   {interest_list[i]}\n\n\n")
                    pdf.write(5, f"Total Amount of Interest for Starting Days :  {interest_start_days}\n\n\n")
                    pdf.write(5, f"Total Amount of Interest for Ending Days :   {interest_end_days}\n\n\n")
                    pdf.write(5, f"Total Amount of Interest payable  :  {total_interest}\n\n\n")
                    pdf.write(5, f"THE AMOUNT OF Rs. {total_interest}/- MAY BE PAID TO................................"
                                 f".............,if approved.")
                    pdf.output('Calculation_sheet_arrear.pdf')

                    my_button["state"] = DISABLED

                except UnboundLocalError:
                    messagebox.showerror("CourtCase Calculator by J.I.T", "PLEASE CHECK THE VALUES AND TRY AGAIN")
                    root.destroy()
                    master.destroy()
                except ValueError:
                    messagebox.showerror("CourtCase Calculator by J.I.T", "PLEASE CHECK THE VALUES AND TRY AGAIN")
                    root.destroy()
                    master.destroy()

            def reset_arrear():

                op1.delete(first=0, last=100)
                e1.delete(first=0, last=100)
                e2.delete(first=0, last=100)
                e3.delete(first=0, last=100)
                my_button["state"] = NORMAL

            my_button = tk.Button(root, text="Calculate", width=12, foreground="Yellow", bg="Blue",
                              command=arrear_calculator, padx=20, pady=20)
            my_button.grid(row=14, column=3)

            reset_button = tk.Button(root, text="Reset", width=12, foreground="Yellow", bg="Blue",
                                 command=reset_arrear, padx=20, pady=20)
            reset_button.grid(row=14, column=4)

        else:

            root2 = tk.Toplevel(master)
            root2.geometry("1100x600")
            root2.title("Court Case Calculator by J.I.T")
            root2.iconbitmap('icon.ico')

            path = '@%s' % os.path.join(os.environ['WINDIR'], 'Cursors/arrow_r.cur').replace('\\', '/')
            root2.configure(cursor=path)

            image3 = ImageTk.PhotoImage(Image.open("biswa-bangla.png"))
            panel3 = tk.Label(root2, image=image3)
            panel3.grid(row=0, column=2)
            panel3.image = image3

            l1 = tk.Label(root2, text="Basic Drawn", pady=20, font=("Times New Roman", 12, "bold"))
            l1.grid(row=10, column=0)

            l2 = tk.Label(root2, text="Basic Due", pady=20, padx=10, font=("Times New Roman", 12, "bold"))
            l2.grid(row=10, column=2)

            l3 = tk.Label(root2, text="Medical Relief Drawn", pady=20, padx=10, font=("Times New Roman", 12, "bold"))
            l3.grid(row=11, column=0)

            l4 = tk.Label(root2, text="Medical Relief Due", pady=20, padx=10, font=("Times New Roman", 12, "bold"))
            l4.grid(row=11, column=2)

            l5 = tk.Label(root2, text="From", pady=20, padx=10, font=("Times New Roman", 12, "bold"))
            l5.grid(row=12, column=0)

            l6 = tk.Label(root2, text="To", pady=20, padx=10, font=("Times New Roman", 12, "bold"))
            l6.grid(row=12, column=2)

            l7 = tk.Label(root2, text="Interest Percentage", pady=20, padx=10, font=("Times New Roman", 12, "bold"))
            l7.grid(row=13, column=1)

            o1 = tk.Label(root2, text="TOTAL INTEREST PAYABLE", pady=20, padx=10, font=("Times New Roman", 15, "bold"))
            o1.grid(row=14, column=1)

            basic_drawn_text = tk.IntVar()
            e1 = tk.Entry(root2, textvariable=basic_drawn_text, bd=3)
            e1.grid(row=10, column=1)

            basic_due_text = tk.IntVar()
            e2 = tk.Entry(root2, textvariable=basic_due_text, bd=3)
            e2.grid(row=10, column=3)

            mr_drawn_text = tk.IntVar()
            e3 = tk.Entry(root2, textvariable=mr_drawn_text, bd=3)
            e3.grid(row=11, column=1)

            mr_due_text = tk.StringVar()
            e4 = tk.Entry(root2, textvariable=mr_due_text, bd=3)
            e4.grid(row=11, column=3)

            interest_text = tk.IntVar()
            e7 = tk.Entry(root2, textvariable=interest_text, bd=3)
            e7.grid(row=13, column=2)

            op1 = tk.Entry(root2, bd=3)
            op1.grid(row=15, column=1)

            current_date = datetime.now()
            cal = dateentry.DateEntry(root2, width=12, year=current_date.year, month=current_date.month,
                                  day=current_date.day, background='darkblue', foreground='white',
                                  selectbackground="red", normalbackground="pink", borderwidth=2, font="helvetica")
            cal.grid(row=12, column=1, padx=10, pady=10)

            cal2 = dateentry.DateEntry(root2, width=12, year=current_date.year, month=current_date.month,
                                   day=current_date.day, background='darkblue', foreground='white',
                                   borderwidth=2, selectbackground="red", normalbackground="light green",
                                   font="helvetica")
            cal2.grid(row=12, column=3, padx=10, pady=10)

            def revised_arrear_calculator():
                try:
                    drawn_bp = int(e1.get())
                    due_bp = int(e2.get())
                    bp = due_bp - drawn_bp
                    drawn_mr = int(e3.get())
                    due_mr = int(e4.get())
                    mr = due_mr - drawn_mr
                    interest_percent = int(e7.get())
                    date_entry1 = cal.get_date()
                    date_entry2 = cal2.get_date()
                    year1 = date_entry1.year
                    month1 = date_entry1.month
                    day1 = date_entry1.day
                    year2 = date_entry2.year
                    month2 = date_entry2.month
                    day2 = date_entry2.day

                    paydays1, new_start_month, new_start_day, new_start_year = period_check.start_days_calculation(
                        month1, day1, year1)
                    if paydays1 >= 1:
                        interest_start_days = amount_calculation_starting_days.start_days_interest(bp, mr, month1,
                                                                                paydays1, year1, interest_percent)
                    else:
                        interest_start_days = 0

                    paydays2, new_end_month, new_end_day, new_end_year = period_check.end_days_calculation(month2, day2,
                                                                                                           year2)
                    if paydays2 < 30:
                        interest_end_days = amount_calculation_end_days.end_days_interest(bp, mr, month2, paydays2,
                                                                                year2, interest_percent)
                    else:
                        interest_end_days = 0
                    paymonths = period_check.pay_months_calculation(new_start_year, new_start_month, new_start_day, new_end_year,
                                                            new_end_month, new_end_day)
                    interest_for_months, start_dates_list, end_dates_list, interest_list = phase_two.pension(bp, mr,
                                                interest_percent, new_start_year, new_start_month, new_start_day, new_end_year,
                                                new_end_month, new_end_day, paymonths)

                    total_interest = round(interest_start_days + interest_end_days + interest_for_months)
                    op1.insert(0, total_interest)

                    pdf = fpdf.FPDF(format='letter')
                    pdf.add_page()
                    pdf.set_font("Arial", size=12)
                    pdf.write(5, f"Calculation Sheet of Interest due to delayed payment of Interest on Revised Arrear. "
                                 f"In pursuance of Order dated..........................passed by the "
                                 f"Honourable Justice.......................................... of Calcutta High Court "
                                 f"and communicated to this end by  Sri/Smt.................................. Advocate "
                                 f"for the Petitioner. WP No.....(W) of 20.... in the matter of ....................."
                                 f"......................................( Petitioner ) Vs the State of West Bengal "
                                 f"& Others. Amount on which Interest is payable Rs.........................../- for "
                                 f"Revised Arrear. Rate of Interest payable Rs. {interest_percent}%\n\n\n")
                    length = interest_list.__len__()
                    for i in range(0, length):
                        pdf.write(5, f"From {start_dates_list[i]} to {end_dates_list[i]} :   {interest_list[i]}\n\n\n")
                    pdf.write(5, f"Total Amount of Interest for Starting Days :  {interest_start_days}\n\n\n")
                    pdf.write(5, f"Total Amount of Interest for Ending Days :   {interest_end_days}\n\n\n")
                    pdf.write(5, f"Total Amount of Interest payable  :  {total_interest}\n\n\n")
                    pdf.write(5, f"THE AMOUNT OF Rs. {total_interest}/- MAY BE PAID TO................................"
                                 f".............,if approved.")
                    pdf.output('Calculation_sheet_revised_arrear.pdf')
                    my_button["state"] = DISABLED


                except ValueError:
                    messagebox.showerror("CourtCase Calculator by J.I.T", "PLEASE CHECK THE VALUES AND TRY AGAIN")
                    root2.destroy()
                    master.destroy()
                except UnboundLocalError:
                    messagebox.showerror("CourtCase Calculator by J.I.T", "PLEASE CHECK THE VALUES AND TRY AGAIN")
                    root2.destroy()
                    master.destroy()

            def reset_revised_arrear():
                op1.delete(first=0, last=100)
                e1.delete(first=0, last=100)
                e2.delete(first=0, last=100)
                e3.delete(first=0, last=100)
                e4.delete(first=0, last=100)
                #e5.delete(first=0, last=100)
                e7.delete(first=0, last=100)
                my_button["state"] = NORMAL

            my_button = tk.Button(root2, text="Calculate", width=12, foreground="Yellow", bg="Blue",
                              command=revised_arrear_calculator, padx=20, pady=20)
            my_button.grid(row=15, column=2)

            reset_button = tk.Button(root2, text="Reset", width=12, foreground="Yellow", bg="Blue",
                                 command=reset_revised_arrear, padx=20, pady=20)
            reset_button.grid(row=15, column=3)


    tk.Radiobutton(master, text="Revised Arrear", variable=var, value="Revised Arrear", foreground="Green",
               font=("Times New Roman", 12, "bold"), highlightcolor="Blue", command=choice).grid(row=7, column=1)
    tk.Radiobutton(master, text="Arrear", variable=var, value="Arrear", foreground="Green",
               font=("Times New Roman", 12, "bold"), highlightcolor="Blue", command=choice).grid(row=7, column=2)

    master.mainloop()
except ValueError:
    print("PLEASE ENTER A VALUE TO CALCULATE")
