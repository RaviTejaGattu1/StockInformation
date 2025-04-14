# 📈 Python Finance Info

A sleek, web-based Python application for retrieving real-time stock information using the **Alpha Vantage API**.  

🔗 **Live Demo:** [https://stockinformation.onrender.com](https://stockinformation.onrender.com)

---

## 🚀 Features

- 🔎 Accepts a stock symbol (e.g., `ADBE`, `NVDA`) via a web form.
- 📅 Displays:
  - Current date and time in **PDT** (e.g., `Mon Apr 14 20:00:00 PDT 2025`)
  - Company name and symbol (e.g., `NVIDIA Corp (NVDA)`)
  - Stock price, value change, and percentage change (e.g., `552.75 +2.45 (+0.45%)`)
- 🛠️ Error handling for:
  - Invalid stock symbols (e.g., `INVALID`)
  - No internet connection
  - API service issues or failures
- 🌐 Publicly accessible via **Render**

---

## ⚙️ Setup (Local Development)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Python-Finance-Info.git
cd Python-Finance-Info
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

- Sign up at [Alpha Vantage](https://www.alphavantage.co) to get a free API key.
- Open `app.py` and replace `YOUR_API_KEY` with your actual key.

### 5. Run the Application

```bash
python3 app.py
```

### 6. Access Locally

Open your browser and navigate to:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## ☁️ Deployment

- Hosted on **Render** using **Gunicorn** as the WSGI server.

### Render Configuration:

- **Build Command:**  
  ```bash
  pip install -r requirements.txt
  ```

- **Start Command:**  
  ```bash
  gunicorn app:app
  ```

- **Live URL:**  
  [https://stockinformation.onrender.com](https://stockinformation.onrender.com)

---

## 💡 Notes

- Originally used the `yfinance` API (Yahoo Finance), but encountered persistent `401 Unauthorized` errors in deployment due to rate limits. Switched to **Alpha Vantage**.
- Alpha Vantage’s free tier allows **5 requests per minute**. Consider upgrading or implementing rate limiting for production use.
- Fully meets all SEP-285 project criteria:
  - ✅ Real-time stock data retrieval  
  - ✅ Robust error handling  
  - ✅ Web accessibility

---

## 📦 Example Output

**Input:** `ADBE`  
**Output:**

```
Mon Apr 14 20:00:00 PDT 2025
ADBE (ADBE)
552.75 +2.45 (+0.45%)
```

---

## 📚 Requirements

- **Python** 3.8+
- Key Libraries:
  - `flask`
  - `alpha-vantage`
  - `python-dateutil`
  - `gunicorn`

See `requirements.txt` for the complete list.
