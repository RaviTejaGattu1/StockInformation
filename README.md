Python Finance Info
A web-based Python application to retrieve stock information using the Alpha Vantage API. Deployed for the SEP-285 course at SJSU, Spring 2025.

Live Demo
https://stockinformation.onrender.com

Features
Accepts a stock symbol (e.g., ADBE, NVDA) as input via a web form.
Displays:
Current date and time in PDT (e.g., Mon Apr 14 20:00:00 PDT 2025).
Company name and symbol (e.g., NVDA (NVDA)).
Current stock price, value change, and percentage change (e.g., 123.45 +1.23 (+1.00%)).
Handles errors gracefully:
Invalid symbols (e.g., INVALID).
No internet connection.
API failures.
Deployed on Render for public access.
Setup (Local Development)
Clone the repository:
bash

Copy
git clone https://github.com/your-username/Python-Finance-Info.git
cd Python-Finance-Info
Create a virtual environment:
bash

Copy
python3 -m venv venv
source venv/bin/activate
Install dependencies:
bash

Copy
pip install -r requirements.txt
Set up Alpha Vantage API key:
Get a free API key from alphavantage.co.
Replace YOUR_API_KEY in app.py with your key.
Run the app:
bash

Copy
python3 app.py
Access locally:
Open http://127.0.0.1:5000 in a browser.
Deployment
Deployed on Render using gunicorn as the WSGI server.
Configuration:
Build command: pip install -r requirements.txt
Start command: gunicorn app:app
Live URL: https://stockinformation.onrender.com
Notes
Initially used yfinance (Yahoo Finance API), but switched to Alpha Vantage due to persistent 401 Unauthorized errors caused by Yahoo's rate limits in deployed environments.
Alpha Vantage’s free tier has a limit of 5 requests/minute. For production, consider a premium key or rate limit handling.
The app meets all project requirements: stock data retrieval, error handling, and web accessibility.
Example Output
Input: ADBE
Output:
Mon Apr 14 20:00:00 PDT 2025
ADBE (ADBE)
552.75 +2.45 (+0.45%)
Requirements
Python 3.8+
Libraries: flask, alpha-vantage, python-dateutil, gunicorn
See requirements.txt for full list
