# Currency-Converter

## Introduction
This Python program serves as a simple currency converter using an API that provides exchange rates. The graphical user interface (GUI) is built using the Tkinter library, making it user-friendly and accessible.

## Prerequisites
Python 3.x
Tkinter library
Requests library

## Installation
1. Ensure you have Python installed on your system.
2. Install the required libraries using the following commands:
   * `pip install requests`
   * `pip install pyinstaller`

## Usage
1. Run the main.py file using the following command: python main.py
2. The GUI window will appear, allowing you to convert currencies.

## Building
1. Run the following command to install the program as an executable: `pyinstaller main.py --onefile -w`
2. Open dist\main.exe

## Features
* From Section: Select the source currency and enter the amount to convert.
* To Section: Select the target currency.
* Converted Section: Displays the converted amount.
* Convert Button: Initiates the currency conversion based on the entered values.
* Clear Button: Clears the entered values.

## Supported Currencies
The converter supports a wide range of currencies. The default values for the "From" and "To" currencies are set to CAD and USD, respectively.

## API Used
The program uses the [Open Exchange Rates API](https://www.exchangerate-api.com/) to retrieve the latest exchange rates.

## How it Works
* Enter the amount and select the source currency ("From").
* Choose the target currency ("To").
* Click the "Convert" button to fetch the latest exchange rate from the API and calculate the converted amount.
* The converted amount is displayed in the "Converted" section.

## Error Handling
If an invalid input (non-numeric) is entered, a warning message will be displayed.

## Acknowledgments
[Open Exchange Rates API](https://www.exchangerate-api.com/) for providing free exchange rate data.
