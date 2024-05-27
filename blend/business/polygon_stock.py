from blend.libraries.polygon import PolygonLibrary


class PolygonStockModel:
    def get_current_price(self, symbol):
        response = PolygonLibrary().get(symbol=symbol)
        current_price = response.json().get("high")
        if current_price == 0 or current_price == "":
            raise Exception(f"We coulnd't find the stock price of {symbol}")

        return current_price
