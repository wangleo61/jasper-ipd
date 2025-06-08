import requests

def get_cadence_stock_info(api_key):
    symbol = "CDNS"
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    quote = data.get("Global Quote", {})
    print("Cadence Design Systems Inc. (CDNS) Stock Information:")
    print(f"Current Price: {quote.get('05. price')}")
    print(f"Previous Close: {quote.get('08. previous close')}")
    print(f"Change Percent: {quote.get('10. change percent')}")

if __name__ == "__main__":
    api_key = "YOUR_ALPHA_VANTAGE_API_KEY"  # Replace with your actual API key
    get_cadence_stock_info(api_key)