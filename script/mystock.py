import yfinance as yf

def get_snps_stock_info():
    snps = yf.Ticker("SNPS")
    info = snps.info
    print("Synopsys Inc. (SNPS) Stock Information:")
    print(f"Current Price: {info.get('currentPrice')}")
    print(f"Previous Close: {info.get('previousClose')}")
    print(f"Market Cap: {info.get('marketCap')}")
    print(f"52 Week High: {info.get('fiftyTwoWeekHigh')}")
    print(f"52 Week Low: {info.get('fiftyTwoWeekLow')}")
    print(f"PE Ratio: {info.get('trailingPE')}")
    print(f"Summary: {info.get('longBusinessSummary')[:200]}...")  # Print first 200 chars

if __name__ == "__main__":
    get_snps_stock_info()    