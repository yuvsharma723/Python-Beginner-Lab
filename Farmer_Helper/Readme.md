# 🌾 Bajra Farming Profit Calculator

A simple Python program to estimate **seed requirement, yield, revenue, cost, and profit** for Bajra farming based on user input (land area in acres) and predefined agricultural parameters.

---

## 👨‍💻 Author

- **Name:** Yuv Sharma  
- **GitHub Username:** [yuvsharma723](https://github.com/yuvsharma723)

---

## 📌 Features

- Calculates:
  - 🌱 Seed required
  - 🌾 Expected yield
  - 💰 Revenue based on MSP
  - 📉 Total cost
  - 📈 Estimated profit
- Soil moisture analysis:
  - Suggests irrigation or drainage based on moisture level
- Input validation for area
- Simple and easy-to-understand structure using Python class

---

## ⚙️ Parameters Used

| Parameter | Value | Description |
|----------|------|-------------|
| Seed required per acre | 45 kg | Standard seed usage |
| Average yield per acre | 14 quintals | Expected production |
| MSP (Minimum Support Price) | ₹2425/quintal | Government price |
| Seed rate | ₹48/kg | Cost of seeds |
| Miscellaneous cost | ₹15400/acre | Includes water, fertilizer, labor |
| Moisture content | 75% | Default sensor value |

---

## 🚀 How It Works

1. User inputs farm area (in acres)
2. Program calculates:
   - Total seed requirement
   - Expected yield
   - Revenue
   - Total cost
   - Profit
3. Checks soil moisture condition:
   - `< 60%` → Irrigation needed
   - `60% - 80%` → Optimal
   - `> 80%` → Drainage needed

---

## 🧮 Formula Used

- **Seed Required**  
  `seed_required = seed_required_per_acre × area`

- **Yield**  
  `yield = avg_yield_per_acre × area`

- **Revenue**  
  `revenue = MSP × yield`

- **Cost**  
  `cost = (seed_rate × seed_required_per_acre × area) + (misc_cost × area)`

- **Profit**  
  `profit = revenue - cost`

---

## ▶️ How to Run

1. Make sure Python is installed (Python 3.x recommended)
2. Save the code in a file, e.g., `bajra.py`
3. Run the script:

```bash
python bajra.py
```

4.Enter the farm area when prompted

---
## 📥 Sample Input

```
enter the area in acres: 2
```

---

## 📤 Sample Output

```
soil moisture is optimal for growth
seed required for 2.0 acres is 90.0 kg
expected yield for 2.0 acres is 28.0 quintals
expected revenue for 2.0 acres is 67900.0 rs
estimated cost for 2.0 acres is 33720.0 rs
estimated profit for 2.0 acres is 34180.0 rs
```

---

## 📦 Future Improvements

- Add GUI (Tkinter / Web App)
- Real-time sensor integration for moisture
- Support for multiple crops
- Dynamic market price fetching
- Data storage and analytics

---

## 🙌 Acknowledgment

Built as a basic agricultural calculator to help farmers estimate profitability and resource requirements efficiently.
