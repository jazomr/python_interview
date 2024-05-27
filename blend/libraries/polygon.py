import logging
import requests

logger = logging.getLogger(__name__)


class PolygonLibrary:
    base_url = "https://api.polygon.io/v1/open-close"
    apikey = "H3AbgxjKB67dVCpcMEuIG59HlFg6U3WZ"

    def get(self, **kwargs):
        url = self.base_url + "/" + kwargs.get("symbol") + "/2023-01-09"
        params = dict(adjusted=True, apiKey=self.apikey)
        response = requests.get(url=url, params=params, timeout=60)
        if response.status_code != 200:
            logger.debug(response.content)
            raise Exception("The response code is different than 200")

        return response
