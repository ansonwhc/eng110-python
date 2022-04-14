import configparser

_config = configparser.ConfigParser()
_config.read('./postcode_service/config.ini')


def base_url():
    return _config['DEFAULT']['base_url']


if __name__ == "__main__":
    pass
