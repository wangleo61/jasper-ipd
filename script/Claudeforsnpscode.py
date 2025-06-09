import requests

def get_snps_stock_info(api_key):
    symbol = "SNPS"
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        quote = data.get("Global Quote", {})
        
        print("Synopsys Inc. (SNPS) Stock Information:")
        print(f"Current Price: ${quote.get('05. price', 'N/A')}")
        print(f"Previous Close: ${quote.get('08. previous close', 'N/A')}")
        print(f"Change: {quote.get('09. change', 'N/A')}")
        print(f"Change Percent: {quote.get('10. change percent', 'N/A')}")
        print(f"Volume: {quote.get('06. volume', 'N/A')}")
        
    except Exception as e:
        print(f)

if __name__ == "__main__":
    API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"  # Replace with your actual API key
    get_snps_stock_info(API_KEY)