# gemini
I used google Gemini to build a cryptocurrency price tracker.
The Python script `gemini_price_tracker.py` fetches and displays the current price of a cryptocurrency from the Gemini exchange using the Gemini Public API.

### **Script Overview**
Here’s a breakdown of how it works:

1. **Imports the `requests` library**:
   ```python
   import requests
   ```
   This allows the script to send HTTP requests to web servers and fetch data. In this case, it fetches data from the Gemini API.

2. **Defines a function to fetch cryptocurrency price**:
   ```python
   def get_crypto_price(symbol: str):
   ```
   This function takes a cryptocurrency symbol (e.g., `btcusd`, `ethusd`) and fetches the current price from the Gemini API.

3. **Builds the URL to call the Gemini API**:
   ```python
   url = f"https://api.gemini.com/v1/pubticker/{symbol}"
   ```
   The URL is dynamically built using the `symbol` provided by the user (e.g., `btcusd` or `ethusd`).

4. **Sends a request to Gemini API**:
   ```python
   response = requests.get(url)
   ```
   It sends a GET request to the Gemini API for the given cryptocurrency symbol.

5. **Handles the API Response**:
   - If the response is successful, it extracts and displays the current price of the cryptocurrency.
   - If there's an error (e.g., invalid symbol or network issue), it displays an error message.
   ```python
   price = data['last']
   return f"The current price of {symbol.upper()} is ${price}."
   ```

6. **Main Program Logic**:
   ```python
   if __name__ == "__main__":
   ```
   This part of the script is executed when you run the script directly. It continuously asks the user to input a cryptocurrency symbol (like `btcusd`) and then calls the `get_crypto_price()` function to fetch and display the price.

   The program loops and keeps asking for new symbols until the user types `"exit"` to quit.

### **How It Works in Practice**

1. **Example Execution**:
   When you run the script, you’ll see a prompt asking for a cryptocurrency symbol, for example:
   ```bash
   Welcome to the Gemini Crypto Price Tracker!
   Enter the cryptocurrency symbol (e.g., btcusd, ethusd) or 'exit' to quit.
   Enter symbol: btcusd
   The current price of BTCUSD is $35000.
   ```

2. **When You Exit**:
   The program will keep asking for cryptocurrency symbols and showing their prices. If you enter `exit`, the program will print:
   ```bash
   Goodbye!
   ```

### **In Summary**:
- **Purpose**: The script fetches real-time cryptocurrency prices from Gemini’s public API and displays them.
- **How it works**: By sending a GET request to Gemini’s public ticker endpoint, it retrieves the latest price data for the given symbol.

Let me know if you need further explanation or if you want to extend the functionality of this script!
