import json
import logging
import configvalidator

# key+val format for config.json
CONFIG_FORMAT = {
    "TOKEN": "",
    "PREFIX": [""],
    "ADMIN_ID": "",
    "REACT_ID": "",
    "ROLECHAN_ID": "",
    "MUTEROLE_ID": "",
    "GUILD_ID": "",
    "BOTCHAN_ID": "",
    "BINDSCHAN_ID": "",
}


def loadConfig():
    """Attempt to load config.json, validate its values, and otherwise create a new config.json"""
    try:
        with open("config.json") as config_file:
            logging.info("reading config.json")
            # load json data
            cfgdata = json.load(config_file)
    except (OSError, IOError):
        logging.warning("no config exists, creating config.json")
        createConfig()
        return

    #create config object using validator
    config = configvalidator.Validator(cfgdata)

    #print out non-token values to verify
    for setting, value in config.__dict__.items():
        if not setting == "TOKEN":
            logging.info("config.json: %s : %s", setting, value)

    return config


# for first time creation
def createConfig():
    """First time creation of config file using CONFIG_FORMAT, exits program after"""
    with open("config.json", "x") as config_file:
        logging.info("config.json created")
        config_file.write(json.dumps(CONFIG_FORMAT, indent=4))
    logging.warning("please fill in config.json")
    logging.warning("exiting")
    quit()