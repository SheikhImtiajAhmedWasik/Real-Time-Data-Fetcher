# Imports
import json, requests
import datetime
import os


json_data = dict()

def current_weather():
    city = input("Enter city name: ")
    url = "https://wttr.in/"

    url = url + city + "?format=j1"
    response = requests.get(url)

    data = response.json()

    temperature = data["current_condition"][0]["temp_C"]
    humidity = data["current_condition"][0]["humidity"]
    wind_speed = data["current_condition"][0]["windspeedKmph"]
    condition = data["current_condition"][0]["weatherDesc"][0]["value"]

    now = datetime.datetime.now()
    time = now.strftime("%d-%m-%Y %I:%M %p")

    print("\n------ Weather Report ------")
    print(f"City: {city.title()}\nTemperature: {temperature}\u00b0C\nHumidity: {humidity}%\nWind Speed: {wind_speed}Km/h\nCondition: {condition}\nFetched At: {time}")
    print("-" * 30)

    json_data.clear()
    json_data.update({
        "type": "weather",
        "city": city,
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition,
        "time": time
    })


def currency_exchange_rate():
    base_currency = input("Base Currency: ").upper()
    target_currency = input("Target Currency: ").upper()

    url = "https://open.er-api.com/v6/latest/"
    url = url + base_currency

    response = requests.get(url)
    data = response.json()

    target_rate = data["rates"][target_currency]

    print(f"\n1 {base_currency} = {target_rate} {target_currency}")

    now = datetime.datetime.now()
    time = now.strftime("%d-%m-%Y %I:%M %p")

    print(f"\nFetched At:\n{time}")

    json_data.clear()
    json_data.update({
        "type": "currency",
        "base": base_currency,
        "target": target_currency,
        "rate": target_rate,
        "time": time
    })


def save_result():
    if json_data == {}:
        raise Exception("No operation done yet!")
    with open("data.json", "w") as f:
        json.dump(json_data, f, indent=4)
        print("File Save successfully.")


def view_data():
    if json_data == {}:
        raise Exception("No data save yet!")
    elif not os.path.exists("data.json"):
        raise Exception("No file exist yet! First create and save.")
    with open("data.json", "r") as f:
        content = f.read()
        print(content)


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
                try:
                    save_result()
                except Exception as e:
                    print(e)
            elif choose == 4:
                try:
                    view_data()
                except Exception as e:
                    print(e)
            elif choose == 5:
                print("Thank you for using Data Fetcher System.\nGoodbye!")
                break
            else:
                raise Exception("Invalid Menu Choose...")
        except Exception as e:
            print(e)
        else:
            input("\nPress Enter to continue....")


main()

