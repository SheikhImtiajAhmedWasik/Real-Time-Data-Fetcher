# Imports
import json, requests
import datetime


def current_weather():
    city = input("Enter city name: ")
    url = "https://wttr.in/Dhaka?format=j1"
    pass


def currency_exchange_rate():
    base_currency = input("Base Currency: ")
    target_currency = input("Target Currency: ")

    url = "https://open.er-api.com/v6/latest/"

    url = url + base_currency.upper()

    response = requests.get(url)
    data = response.json()
    print(data.keys())

    target_rate = data["rates"][target_currency.upper()]
    print(target_rate)
    print(type(target_rate))

    print(f"1 {base_currency.upper()} = {target_rate} {target_currency.upper()}")

    now = datetime.datetime.now()
    time = now.strftime("%d-%m-%Y %I:%M %p")

    print(f"\nFetched At:\n{time}")



currency_exchange_rate()


def save_result():
    pass


def view_data():
    pass


def main():
    while True:
        print("\n========== Data Fetcher ==========\n")
        print("1. Current Weather\n2. Currency Exchange Rate\n3. Save Result to JSON File\n4. View Previous Saved Data\n5. Exit")
        print("\n" + "="*30 + "\n")

        choose = int(input("Choose an option: "))

        try:
            if choose == 1:
                current_weather()
            elif choose == 2:
                currency_exchange_rate()
            elif choose == 3:
                save_result()
            elif choose == 4:
                view_data()
            elif choose == 5:
                print("Thank you for using Data Fetcher System.\nGoodbye!")
                break
            else:
                raise Exception("Invalid Menu Choose...")
        except Exception as e:
            print(e)



# main()