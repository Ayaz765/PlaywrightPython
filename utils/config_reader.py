import configparser

config = configparser.ConfigParser()
config.read("testdata/config.ini")

def get_config(section, key):
    try:
        return config.get(section, key)
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        raise ValueError(f"Missing configuration - {str(e)}")
