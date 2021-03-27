import json
import logging

COUNTER_FORMAT = {"COUNTER": 0}


def loadCounter():
    try:
        with open("counter.json") as counter_file:
            count_data = json.load(counter_file)
        COUNTER_NUM = count_data["COUNTER"]
        logging.info("counter: %s", COUNTER_NUM)
        COUNTER_FORMAT["COUNTER"] = COUNTER_NUM
    except (OSError, IOError) as e:
        logging.warning("no counter exists, creating counter.json")
        createCounter()


def createCounter():
    with open("counter.json", "x") as counter_file:
        logging.info("counter.json created")
        json.dump(COUNTER_FORMAT, counter_file)
    logging.warning("counter set to 0")


def updateCounter():
    with open("counter.json", "w") as counter_file:
        COUNTER_FORMAT["COUNTER"] += 1
        json.dump(COUNTER_FORMAT, counter_file)


def getCounter():
    with open("counter.json") as counter_file:
        count_data = json.load(counter_file)
    return count_data["COUNTER"]
