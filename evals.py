import discord

# BOOLEAN FUNCTIONS

#if the given message author is a member of the react role specified in config.cfg
def isReact(message, reactID):
    if message.guild.get_role(reactID) in message.author.roles:
        return True
    else:
        return False

#if the given message author is a member of the admin role specified in config.cfg
def isAdmin(message, adminID):
    if message.guild.get_role(adminID) in message.author.roles:
        return True
    else:
        return False

#if the given message author is the owner of the guild the message was sent in (todo update to if owner based on GUILD_ID from config.cfg)
def isOwner(message):
    if message.guild.owner_id == message.author.id:
        return True
    else:
        return False

#if the given message author is a bot or self
def isSelfOrBot(message, user):
    if (message.author == user) or (message.author.bot):
        return True
    else:
        return False

#evaluates commands based on a message array split by spaces, 
#the alias list of a command, 
#the minimum length the array should be to avoid index out of range issues, 
#and location to determine where it should be located
def isCommand(messageArray, commandNames, minLength, location):
    if len(messageArray) >= minLength:
        if location == -1:
            for command in commandNames:
                if command in messageArray:
                    return True
        else:
            for command in commandNames:
                if messageArray[location] == command:
                    return True
    return False