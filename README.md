<div align="center">

# 🌍 Real-Time Weather & Currency Data Fetcher

### 🐍 A Python Console Application for Fetching Real-Time Data from Public APIs

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![API](https://img.shields.io/badge/Public-API-success?style=for-the-badge)
![JSON](https://img.shields.io/badge/Data-JSON-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Assignment-red?style=for-the-badge)

</div>

---

# 🎯 Objective

Build a Python application that fetches **real-time weather** and **currency exchange rate** data from public APIs.

The project demonstrates the use of:

- 🌐 HTTP Requests
- 📦 Python Modules
- 📄 JSON Files
- 📅 Date & Time
- 🧰 Built-in Python Libraries
- 🔄 API Integration

---

# ✨ Features

The application provides the following menu.

```text
========== Data Fetcher ==========

1. Current Weather
2. Currency Exchange Rate
3. Save Result to JSON File
4. View Previous Saved Data
5. Exit

==================================
```

---

# 🚀 Functional Requirements

## 🌤️ 1. Current Weather

Ask the user for a city name.

Example:

```text
Enter city name: Dhaka
```

Fetch the following information using a **Weather API**:

- 🏙️ City Name
- 🌡️ Temperature
- 💧 Humidity
- 💨 Wind Speed
- ☁️ Weather Condition
- 🕒 Date & Time

### Example Output

```text
------ Weather Report ------

City: Dhaka
Temperature: 31°C
Humidity: 74%
Wind Speed: 12 km/h
Condition: Cloudy
Fetched At: 22-07-2026 10:30 PM

----------------------------
```

---

## 💱 2. Currency Exchange Rate

Ask the user for:

- Base Currency
- Target Currency

Example

```text
Base Currency : USD
Target Currency : BDT
```

Fetch the exchange rate using a **Currency Exchange API**.

### Example Output

```text
1 USD = 122.45 BDT

Fetched At:
22-07-2026 10:31 PM
```

---

## 💾 3. Save Result

Save the latest fetched data into a JSON file.

File Name

```text
data.json
```

### Weather Example

```json
{
    "type": "weather",
    "city": "Dhaka",
    "temperature": 31,
    "humidity": 74,
    "condition": "Cloudy",
    "time": "2026-07-22 22:30:10"
}
```

### Currency Example

```json
{
    "type": "currency",
    "base": "USD",
    "target": "BDT",
    "rate": 122.45,
    "time": "2026-07-22 22:31:50"
}
```

---

## 📂 4. View Previous Saved Data

Read the saved JSON file and display the most recently stored information.

### Example Output

```text
Last Saved Data

Type : Weather
City : Dhaka
Temperature : 31°C
Saved Time : 2026-07-22 22:30
```

> Handle the case where **`data.json`** does not exist.

---

## 🚪 5. Exit

Safely terminate the application.

---

# 🌐 Public APIs

## 🌤️ Weather API

No API Key Required

```text
https://wttr.in/Dhaka?format=j1
```

Returns weather data in **JSON** format.

---

## 💱 Currency Exchange API

```text
https://open.er-api.com/v6/latest/USD
```

or

```text
https://api.exchangerate-api.com/v4/latest/USD
```

---

# 📁 Project Structure

The entire application should be implemented in a **single Python file**.

```text
data_fetcher.py
│
├── import modules
├── weather()
├── currency()
├── save_json()
├── view_json()
├── main_menu()
└── program starts here
```

---

# 📌 Sample Workflow

```text
Start Program
      │
      ▼
Display Main Menu
      │
      ▼
Choose an Option
      │
      ├─────────────► Current Weather
      │                     │
      │                     ▼
      │             Fetch Weather Data
      │
      ├─────────────► Currency Exchange
      │                     │
      │                     ▼
      │             Fetch Exchange Rate
      │
      ├─────────────► Save Result
      │                     │
      │                     ▼
      │              Save to data.json
      │
      ├─────────────► View Previous Data
      │                     │
      │                     ▼
      │             Read JSON File
      │
      ▼
Exit Program
```

---

# 📚 Python Concepts Used

| Concept | Used |
|---------|:----:|
| Variables | ✅ |
| Functions | ✅ |
| Modules | ✅ |
| JSON | ✅ |
| HTTP Requests | ✅ |
| API Integration | ✅ |
| File Handling | ✅ |
| Date & Time | ✅ |
| Exception Handling | ✅ |

---

# 🛠 Built-in Modules

The project may utilize the following Python modules.

- 📦 `json`
- 🌐 `requests`
- 📅 `datetime`
- ⚠️ `os` *(optional for file checking)*

---

# ⚠️ Exception Handling

Handle common runtime errors gracefully.

| Exception | Description |
|-----------|-------------|
| Invalid Menu Choice | User selects an invalid option |
| Invalid City Name | Weather data cannot be retrieved |
| Invalid Currency Code | Currency not supported |
| API Connection Error | Unable to connect to the API |
| File Not Found | `data.json` does not exist |
| JSON Decode Error | Invalid or corrupted JSON file |
| Unexpected Errors | Prevent program crashes |

> **The application should never terminate unexpectedly because of invalid input or network issues.**

---

# 📄 Example Output

```text
========== Data Fetcher ==========

1. Current Weather
2. Currency Exchange Rate
3. Save Result to JSON File
4. View Previous Saved Data
5. Exit

==================================

Choose an option: 1

Enter city name: Dhaka

------ Weather Report ------

City: Dhaka
Temperature: 31°C
Humidity: 74%
Wind Speed: 12 km/h
Condition: Cloudy
Fetched At: 22-07-2026 10:30 PM

----------------------------
```

---

<div align="center">

## ⭐ Built with Python & Public APIs

A beginner-friendly project demonstrating **API Integration**, **JSON Processing**, **File Handling**, and **HTTP Requests** in Python.

If you found this project helpful, consider giving it a ⭐ on GitHub!

</div>
