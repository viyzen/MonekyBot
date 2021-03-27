import json
import logging

#format to first store incase it pulls an empty file, todo fix the empty key val storing
ROLE_MSG_FORMAT = {"" : ""}

#attempt to load rolereact.json at startup
def loadRoleReact():
    try:
        with open("rolereact.json") as rolereact_file:
            ROLEREACT_DICT = json.load(rolereact_file)
        logging.info("loaded rolereact.json")
    except (OSError, IOError, json.decoder.JSONDecodeError):
        logging.warning("no rolereact file exists, creating rolereact.json")
        createRoleReact()

#create a new rolereact.json file
def createRoleReact():
    with open("rolereact.json", "x") as rolereact_file:
        logging.info("rolereact.json created")
        json.dump(ROLE_MSG_FORMAT, rolereact_file)
    logging.warning("rolereact is empty")

#load the file, add entry to dict, save to the file
def addRoleReact(messageID, roleID):
    with open("rolereact.json", "r") as rolereact_file:
        ROLEREACT_DICT = json.load(rolereact_file)
    ROLEREACT_DICT[messageID] = roleID
    with open("rolereact.json", "w") as rolereact_file:
        json.dump(ROLEREACT_DICT, rolereact_file)

#load the file, remove entry from dict, save to the file
def removeRoleReact(messageID):
    with open("rolereact.json", "r") as rolereact_file:
        ROLEREACT_DICT = json.load(rolereact_file)
    try:
        logging.info("removing rolereact")
        del ROLEREACT_DICT[str(messageID)]
    except KeyError:
        logging.warning("rolereact.json failed to remove message %s from ROLEREACT_DICT")
    with open("rolereact.json", "w") as rolereact_file:
        json.dump(ROLEREACT_DICT, rolereact_file)

#get the dict from the file
def getRoleReact():
    with open("rolereact.json", "r") as rolereact_file:
        ROLEREACT_DICT = json.load(rolereact_file)
    return ROLEREACT_DICT
