from .ScraperStockBR import ScraperStockBr
from .ScraperFII import ScraperFII
from model.TickerType import STOCKS_BR_ID, FII_ID

from contract.service.Scraper import Scraper as ScraperServiceInterface

class ScraperConstructor:
    def build(self, type: int) -> ScraperServiceInterface:
        if type == STOCKS_BR_ID:
            return ScraperStockBr()
        elif type == FII_ID:
            return ScraperFII()
