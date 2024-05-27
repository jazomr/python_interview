from blend.libraries.alphavantage import AlphavantageLibrary


class AlphavantageStockModel:
    def get_current_price(self, symbol):
        response = AlphavantageLibrary().get(symbol=symbol)
        current_price = response.json().get("Global Quote").get("05. price", 0)
        if current_price == 0:
            raise Exception(f"We coulnd't find the stock price of {symbol}")

        return float(current_price)
