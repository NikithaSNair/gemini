import requests

def get_crypto_price(symbol: str):
    """
    Fetches the current price of a cryptocurrency from Gemini API.
    
    Args:
        symbol (str): The trading pair symbol (e.g., 'btcusd', 'ethusd').

    Returns:
        str: Current price or an error message.
    """
    url = f"https://api.gemini.com/v1/pubticker/{symbol}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        price = data['last']
        return f"The current price of {symbol.upper()} is ${price}."
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"
    except KeyError:
        return f"Invalid symbol or data not available for {symbol.upper()}."

# Main program
if __name__ == "__main__":
    print("Welcome to the Gemini Crypto Price Tracker!")
    print("Enter the cryptocurrency symbol (e.g., btcusd, ethusd) or 'exit' to quit.")
    
    while True:
        symbol = input("Enter symbol: ").strip().lower()
        if symbol == "exit":
            print("Goodbye!")
            break
        print(get_crypto_price(symbol))
