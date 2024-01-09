from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests

root = Tk()
root.title('Currency Converter')
root.geometry("300x450")

# Create frame
frame = Frame(master=root)
frame.pack(pady=20, fill="both", expand=True)

# Create label
label = Label(master=frame, text="Currency Converter", font=("Arial", 18))
label.pack(pady=12, padx=10)

# Create frame for "from" section
from_frame= LabelFrame(frame, text="From:")
from_frame.pack(pady=20, padx=50)

# Create "From" entry/combobox
from_entry = ttk.Combobox(from_frame,
    values=['CAD', 'USD', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM',
            'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN',
            'BZD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP',
            'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP',
            'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR',
            'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW',
            'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD',
            'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO',
            'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON',
            'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS',
            'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD',
            'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR',
            'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL'], font=("Arial", 14))
from_entry.pack(pady=10, padx=10)
from_entry.set("CAD")

# Create "Amount" entry
amount_entry = Entry(from_frame, font=("Arial", 14))
amount_entry.pack(pady=10, padx=10)

# Create frame for "To" section
to_frame= LabelFrame(frame, text="To:")
to_frame.pack(pady=10, padx=50)

# Create "To" entry/combobox
to_entry = ttk.Combobox(to_frame,
    values=['CAD', 'USD', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM',
            'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN',
            'BZD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP',
            'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP',
            'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IGR', 'ILS', 'IMP', 'INR',
            'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW',
            'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD',
            'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO',
            'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON',
            'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS',
            'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD',
            'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR',
            'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL'], font=("Arial", 14))
to_entry.pack (pady=10, padx=10)
to_entry.set("USD")

# Create "Converted" entry
converted_entry = Entry(to_frame, font=("Arial", 14), bd=0, bg="systembuttonface")
converted_entry.pack(pady=10, padx=10)

# Convert amount
def convert():
    try:
        amount = float(amount_entry.get())
        from_ = from_entry.get()
        to_ = to_entry.get()
        response = requests.get(f'https://open.er-api.com/v6/latest?base={from_}&symbols={to_}')
        data = response.json()
        exchange_rate = data['rates'][to_]
        conversion = amount * exchange_rate
        conversion = format(conversion, '.2f')
        converted_entry.delete(0, END)
        converted_entry.insert(0, conversion)
    except ValueError:
        messagebox.showwarning("WARNING!", "Invalid input. Please enter a number.")

# Clear entries
def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)

# Create frame for buttons
button_frame = Frame(frame)
button_frame.pack(pady=20)

# Create "Convert" button
convert_button = Button(button_frame, text=("Convert"), command=convert)
convert_button.grid(column=0, row=0, padx=10)

# Create "Clear" button
clear_button = Button(button_frame, text=("Clear"), command=clear)
clear_button.grid(column=1, row=0, padx=10)

root.mainloop()