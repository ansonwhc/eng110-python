import json


class RatesParser:
    def __init__(self, rates_json_filepath):
        rates_info = self._load_json_file(rates_json_filepath)
        self.base = rates_info['base']
        self.date = rates_info['date']
        self.gbp = rates_info['rates']['GBP']

    @staticmethod
    def _load_json_file(rates_json_filepath):
        with open(rates_json_filepath) as rates_file:
            return json.load(rates_file)

    def base_to_gbp(self, base_amount):
        return base_amount * self.gbp

    def gbp_to_base(self, gbp_amount):
        return gbp_amount / self.base


if __name__ == "__main__":
    rp = RatesParser("rates.json")
    print(rp.gbp)
