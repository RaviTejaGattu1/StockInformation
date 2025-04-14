import os
from flask import Flask, request, render_template
import yfinance as yf
from datetime import datetime
from dateutil import tz
import socket


app = Flask(__name__)

def check_internet():
    """Check if there is an internet connection."""
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

def get_stock_info(symbol):
    """Retrieve stock information for the given symbol."""
    try:
        # Check internet connectivity
        if not check_internet():
            return None, "Error: No internet connection."

        # Fetch stock data
        stock = yf.Ticker(symbol)
        info = stock.info

        # Check if valid symbol
        if not info.get("shortName"):
            return None, f"Error: Invalid symbol '{symbol}'."

        # Get current date and time (PDT)
        utc_time = datetime.now(tz.tzutc())
        pdt_time = utc_time.astimezone(tz.gettz("America/Los_Angeles"))
        formatted_time = pdt_time.strftime("%a %b %d %H:%M:%S PDT %Y")

        # Get stock details
        company_name = info.get("shortName", "N/A")
        current_price = info.get("regularMarketPrice", 0.0)
        previous_close = info.get("regularMarketPreviousClose", 0.0)
        
        # Calculate value and percentage change
        value_change = current_price - previous_close
        percentage_change = (value_change / previous_close) * 100 if previous_close != 0 else 0

        # Format changes with + or - signs
        value_change_str = f"+{value_change:.2f}" if value_change >= 0 else f"{value_change:.2f}"
        percentage_change_str = f"+{percentage_change:.2f}" if percentage_change >= 0 else f"{percentage_change:.2f}"

        # Prepare result
        result = {
            "date_time": formatted_time,
            "company": f"{company_name} ({symbol.upper()})",
            "price": f"{current_price:.2f}",
            "value_change": value_change_str,
            "percentage_change": f"({percentage_change_str}%)"
        }
        return result, None

    except Exception as e:
        return None, f"Error: Unable to fetch data for '{symbol}'. Details: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        symbol = request.form.get("symbol").strip().upper()
        result, error = get_stock_info(symbol)
        if error:
            return render_template("index.html", error=error)
        return render_template("result.html", result=result)
    return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)