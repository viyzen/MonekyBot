import commands

#dictionary entries should have str identifier key, followed by a value subdict with bool prefix, function func, int position, int minlength, list aliases
#prefix requires the command have the chosen prefix in config exist before evaluation
#func defines the function to call in commands.py if evaluated to be true
#pos defines the position the alias words should be found in the message (0 for first pos, 1 for second, etc) (-1 to ignore pos)
#minlen defines the minimum length a message containing this command should be (min should always be non zero)
#aliases defines a list of single world aliases for a command, it will be searched when evaluating if a message is a command
commandDict = {
    "pongp" : {
        "prefix" : True,
        "func" : commands.pong,
        "pos" : 1,
        "minlen" : 2,
        "aliases" : ["ping"]
    },
    "pong" : {
        "prefix" : False,
        "func" : commands.pong,
        "pos" : 0,
        "minlen" : 1,
        "aliases" : ["ping"]
    },
    "magicball" : {
        "prefix" : True,
        "func" : commands.magicball,
        "pos" : 1,
        "minlen" : 2,
        "aliases" : ["ball", "magicball"]
    },
    "british" : {
        "prefix" : False,
        "func" : commands.british,
        "pos" : -1,
        "minlen" : 1,
        "aliases" : ["british", "brits", "brit", "britain", "uk"]
    },
    "gas" : {
        "prefix" : False,
        "func" : commands.gas,
        "pos" : -1,
        "minlen" : 1,
        "aliases" : ["gas"]
    },
    "add" : {
        "prefix" : True,
        "func" : commands.add,
        "pos" : 1,
        "minlen" : 3,
        "aliases" : ["add"]
    },
    "remove" : {
        "prefix" : True,
        "func" : commands.remove,
        "pos" : 1,
        "minlen" : 3,
        "aliases" : ["remove"]
    },
    "reactlist" : {
        "prefix" : True,
        "func" : commands.reactlist,
        "pos" : 1,
        "minlen" : 2,
        "aliases" : ["list"]
    },
    "scream" : {
        "prefix" : True,
        "func" : commands.scream,
        "pos" : 1,
        "minlen" : 2,
        "aliases" : ["scream"]
    },
    "clear" : {
        "prefix" : True,
        "func" : commands.clear,
        "pos" : 1,
        "minlen" : 2,
        "aliases" : ["clear"]
    },
    "banana" : {
        "prefix" : True,
        "func" : commands.banana,
        "pos" : 1,
        "minlen" : 2,
        "aliases" : ["banana", "🍌"]
    },
    "flip" : {
        "prefix" : True,
        "func" : commands.flip,
        "pos" : 1,
        "minlen" : 2,
        "aliases" : ["flip"]
    },
    "counter" : {
        "prefix" : True,
        "func" : commands.reactcount,
        "pos" : 1,
        "minlen" : 2,
        "aliases" : ["counter","count"]
    },
    "help" : {
        "prefix" : True,
        "func" : commands.help,
        "pos" : 1,
        "minlen" : 2,
        "aliases" : ["help"]
    },
    "muteathon" : {
        "prefix" : True,
        "func" : commands.muteathon,
        "pos" : 1,
        "minlen" : 2,
        "aliases" : ["muteathon"]
    },
    "insulted" : {
        "prefix" : True,
        "func" : commands.insulted,
        "pos" : 1,
        "minlen" : 2,
        "aliases" : ["fuck", "fucker", "shit", "trash", "sucks"]
    },
    "rolereact" : {
        "prefix" : True,
        "func" : commands.rolereact,
        "pos" : 1,
        "minlen" : 4,
        "aliases" : ["rolereact"]
    },
    "censor" : {
        "prefix" : False,
        "func" : commands.deleteMessage,
        "pos" : -1,
        "minlen" : 1,
        "aliases" : ["nigger", "nigga", "nigs", "niggers", "niggas"]
    },
        "translator" : {
        "prefix" : True,
        "func" : commands.translator,
        "pos" : 1,
        "minlen" : 2,
        "aliases" : ["translate"]
    }
}

#dict to obj
class CommandStruct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

def createCommands():
    commandsObj = CommandStruct(**commandDict)
    return commandsObj
