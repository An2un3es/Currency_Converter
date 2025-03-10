from ast import While
from lib2to3.pgen2.token import NUMBER
from locale import currency
from socketserver import DatagramRequestHandler
from tkinter import E, N
from tkinter.messagebox import NO
from urllib import response
import requests

API_KEY = 'fca_live_Re6xf5C4M7IOYAcM98NYXngPpfJfgQNsSVYFS8HM'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES=[ "EUR", "USD", "CAD", "AUD", "CNY", "GBP"]

def convert_currency(base):
    currencies= ",".join(CURRENCIES)
    url= f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response= requests.get(url)
        data= response.json()
        return data["data"]

    except:
        print("Error getting data. Verify you connection or the currency that was asked.")
        return None

while True:
    entry = input("Enter the ammount and the currency (ex: 200 EUR) or 'q' to quit: ").upper()
    
    if entry == "Q":
        break
    
    parts = entry.split()
    
    if len(parts) != 2:
        print("Wrong format! Here's an example: '200 EUR'")
        continue
    
    value, base = parts
    
    try:
        value = float(value)  
    except ValueError:
        print("Value must be a valid number.")
        continue

    data = convert_currency(base)
    
    if not data:
        continue
    
    del data[base] 
    
    print(f"\n{value} {base} equivalent to:\n")
    for curr, rate in data.items():
        print(f"{curr}: {value * rate:.2f}")
    print()