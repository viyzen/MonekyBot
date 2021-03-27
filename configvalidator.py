import logging

#validates recieved data from config.py in dict format (from json)
#converts into a config object after validating and printing info on:
#optional settings
#type required settings
#supports int, list, or string validation

schema = {
    "TOKEN": {
        "type": "string",
        "optional": False,
    },
    "PREFIX": {
        "type": "list",
        "optional": True,
    },
    "ADMIN_ID": {
        "type": "int",
        "optional": True,
    },
    "REACT_ID": {
        "type": "int",
        "optional": True,
    },
    "ROLECHAN_ID": {
        "type": "int",
        "optional": True,
    },
    "MUTEROLE_ID": {
        "type": "int",
        "optional": True,
    },
    "GUILD_ID": {
        "type": "int",
        "optional": False,
    },
    "BOTCHAN_ID": {
        "type": "int",
        "optional": False,
    },
    "BINDSCHAN_ID": {
        "type": "int",
        "optional": True,
    },
}

class Validator:
    """Defines validation for incoming json config dictionary and assigns attributes to object"""
    def __init__(self, cfgdata):
        #takes type & optional values for each config setting from schema and validates ones taken from json
        #types can be int, string, or list
        #optional is a bool
        for key, value in schema.items(): 
            #KEY, value[type, optional, ...]
            if value["type"] == "int":
                #integer validator, attempts to cast to int, catches valueerror for blank input, cant use isinstance since json load will likely grab a string
                try:
                    setattr(self, key, int(cfgdata[key]))
                except ValueError:
                    logging.warn("config.cfg key: %s should be type int, setting to None", key)
                    setattr(self, key, None)
            elif value["type"] == "string":
                #string validator
                if isinstance(cfgdata[key], str):
                    setattr(self, key, cfgdata[key])
                else:
                    logging.warn("config.cfg key: %s should be type string, setting to None", key)
                    setattr(self, key, None)
            elif value["type"] == "list":
                #list validator
                if isinstance(cfgdata[key], list):
                    setattr(self, key, cfgdata[key])
                else:
                    logging.warn("config.cfg key: %s should be type list, setting to None", key)
                    setattr(self, key, None)
            if getattr(self, key) == None:
                if value["optional"]:
                    logging.info("config.cfg optional key: %s is empty", key)
                else:
                    #force quit if non optional setting is blank
                    logging.error("config.cfg non-optional key: %s is empty, exiting program", key)
                    quit()