import logging
import requests

logger = logging.getLogger(__name__)


class AlphavantageLibrary:
    base_url = "https://www.alphavantage.co/query"
    apikey = "X1AN6OR1Y3WI51E3"

    def get(self, **kwargs):
        params = dict(
            function="GLOBAL_QUOTE", symbol=kwargs.get("symbol"), apikey=self.apikey
        )
        response = requests.get(url=self.base_url, params=params, timeout=60)
        if response.status_code != 200:
            logger.debug(response.content)
            raise Exception("The response code is different than 200")

        return response
