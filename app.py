import os
from flask import Flask, request, render_template
from alpha_vantage.timeseries import TimeSeries
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
    """Retrieve stock information using Alpha Vantage."""
    try:
        # Check internet connectivity
        if not check_internet():
            return None, "Error: No internet connection."

        # Initialize Alpha Vantage
        api_key = "V3JRGD8MJ6KSIA64"  # Replace with your Alpha Vantage API key
        ts = TimeSeries(key=api_key, output_format="json")

        # Get quote data
        data, meta = ts.get_quote_endpoint(symbol)

        # Check if valid symbol
        if not data:
            return None, f"Error: Invalid symbol '{symbol}'."

        # Get current date and time (PDT)
        utc_time = datetime.now(tz.tzutc())
        pdt_time = utc_time.astimezone(tz.gettz("America/Los_Angeles"))
        formatted_time = pdt_time.strftime("%a %b %d %H:%M:%S PDT %Y")

        # Get stock details
        company_name = symbol  # Alpha Vantage quote doesn't provide full name
        current_price = float(data["05. price"])
        previous_close = float(data["08. previous close"])
        value_change = current_price - previous_close
        percentage_change = (value_change / previous_close) * 100 if previous_close != 0 else 0

        # Format changes
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)