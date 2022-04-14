# postcode, country, region, admin_district, parish
# the Postcode obect will be initialised by passing in a dictionary


class Postcode:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
