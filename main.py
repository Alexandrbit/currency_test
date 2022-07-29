from currency_converter import CurrencyConverter
from tkinter import *


root = Tk()
root.title('Currency Convecter')
root.geometry('300x250+300+300')
root.resizable(width=False, height=False)
root['bg'] = 'black'
c = CurrencyConverter()

header_frame = Frame(root)
header_frame.pack(fill=X)

header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

h_currency = Label(header_frame, text='Валюта', bg='black', fg='lime', font='Arial 12 bold')
h_currency.grid(row=0, column=0, sticky=EW)
h_course = Label(header_frame, text='Курс', bg='black', fg='lime', font='Arial 12 bold')
h_course.grid(row=0, column=1, columnspan=2, sticky=EW)

# USD currency
usd_currency = Label(header_frame, text='USD', font='Arial 10')
usd_currency.grid(row=1, column=0, sticky=EW)
usd_one = Label(header_frame, text='1', font='Arial 10')
usd_one.grid(row=1, column=1, sticky=EW)
usd_converted = Label(header_frame, text='%.2f'% c.convert(1, 'USD', 'EUR'), font='Arial 10')
usd_converted.grid(row=1, column=2, sticky=EW)

# BGN currency
usd_currency = Label(header_frame, text='BGN', font='Arial 10')
usd_currency.grid(row=2, column=0, sticky=EW)
usd_one = Label(header_frame, text='1', font='Arial 10')
usd_one.grid(row=2, column=1, sticky=EW)
usd_converted = Label(header_frame, text='%.2f'% c.convert(1, 'BGN', 'EUR'), font='Arial 10')
usd_converted.grid(row=2, column=2, sticky=EW)

# JPY currency
usd_currency = Label(header_frame, text='JPY', font='Arial 10')
usd_currency.grid(row=3, column=0, sticky=EW)
usd_one = Label(header_frame, text='1', font='Arial 10')
usd_one.grid(row=3, column=1, sticky=EW)
usd_converted = Label(header_frame, text='%.2f'% c.convert(1, 'JPY', 'EUR'), font='Arial 10')
usd_converted.grid(row=3, column=2, sticky=EW)

# CYP currency
usd_currency = Label(header_frame, text='CYP', font='Arial 10')
usd_currency.grid(row=4, column=0, sticky=EW)
usd_one = Label(header_frame, text='1', font='Arial 10')
usd_one.grid(row=4, column=1, sticky=EW)
usd_converted = Label(header_frame, text='%.2f'% c.convert(1, 'CYP', 'EUR'), font='Arial 10')
usd_converted.grid(row=4, column=2, sticky=EW)

# CZK currency
usd_currency = Label(header_frame, text='CZK', font='Arial 10')
usd_currency.grid(row=5, column=0, sticky=EW)
usd_one = Label(header_frame, text='1', font='Arial 10')
usd_one.grid(row=5, column=1, sticky=EW)
usd_converted = Label(header_frame, text='%.2f'% c.convert(1, 'CZK', 'EUR'), font='Arial 10')
usd_converted.grid(row=5, column=2, sticky=EW)

root.mainloop()