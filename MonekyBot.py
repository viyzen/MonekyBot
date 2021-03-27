import discord
import re
#regex for fixing commands where people spam space bar
import random
#random numbers for some randomized command responses
from FileHelper import FileHelper
#filehelper for config file

intents = discord.Intents.default()
#intents instance
intents.members = True
#cache members at startup
intents.reactions = True
#cache reactions
c = discord.Client(intents=intents)
#client instance

#initialize important variables
commandPrefix = str("")
commandPrefix2 = str("")
adminID = 0
reactID = 0
counter = 0

print('initiating bot')
config = FileHelper("cfg")
#instance of FileHelper, default name for the config file (cfg.txt)
config.createFile()
#attempts to create a file, if successful it will end program, if not it ignores and continues
t = config.getConfigSetting("token")
commandPrefix = str(config.getConfigSetting("prefix"))
commandPrefix2 = str(config.getConfigSetting("prefix2"))
adminID = int(config.getConfigSetting("adminid"))
reactID = int(config.getConfigSetting("reactid"))
counter = int(config.getConfigSetting("counter"))
#get config settings at startup and store

#debug print stored vars
if 1:
    print(f'commandPrefix: {commandPrefix}')
    print(f'commandPrefix2: {commandPrefix2}')
    print(f'adminID: {adminID}')
    print(f'reactID: {reactID}')
    print(f'counter: {counter}')
    print('completed loading config')

#EVENT LISTENERS
@c.event
async def on_ready():
#once bot has logged in and gets returned the go ahead
    print(f'{c.user} has connected to discord')
    #login successful
    await c.get_channel(697476058177601567).send(f'Ook Ook, im MonekyBot :banana:\nThere are {counter} <:moneky:742447598601764875> in the zoo')
    #prints to general, todo make this config setting
    print(f'loaded {len(c.users)} users into cache')
    #number of users in cache, debug for members intent

#role selection functions

#tf2 role id 697482804757266505
#mvm role id 697482914341847122
#mc role id 697483011612082226
#rain role id 697486207034064976
#todo store role ID and message ID in config, and have autogenerators for the message/role to select based on a command

@c.event
async def on_raw_reaction_add(reactedMessage):
#any reactions added to messages
    if reactedMessage.member.bot:
    #message from self or another bot
        return

    if reactedMessage.message_id == 770409082371833866 :
    #tf2 message
        if reactedMessage.event_type == "REACTION_ADD" :
        #added reaction
            print(f'{c.get_guild(reactedMessage.guild_id).get_member(reactedMessage.user_id).name} added tf2 reaction')
            #debug
            await reactedMessage.member.add_roles(reactedMessage.member.guild.get_role(697482804757266505))
            #user who reacted to message will have role added based on that member's guild's role searched by 69... todo improve this nonsense
            #tf2 role added
        else :
            print(f'error in event_type')
            #catch error incase there was something else triggered by reaction_add


    elif reactedMessage.message_id == 770409082883407872 :
    #mvm message
        if reactedMessage.event_type == "REACTION_ADD" :
        #added reaction
            print(f'{c.get_guild(reactedMessage.guild_id).get_member(reactedMessage.user_id).name} added mvm reaction')
            #debug
            await reactedMessage.member.add_roles(reactedMessage.member.guild.get_role(697482914341847122))
            #mvm role added
        else :
            print(f'error in event_type')
            #catch all
    elif reactedMessage.message_id == 770409083345829888 :
        #mc message
        if reactedMessage.event_type == "REACTION_ADD" :
        #added reaction
            print(f'{c.get_guild(reactedMessage.guild_id).get_member(reactedMessage.user_id).name} added mc reaction')
            #debug
            await reactedMessage.member.add_roles(reactedMessage.member.guild.get_role(697483011612082226))
            #mc role added
        else :
            print(f'error in event_type')
            #catch all


    elif reactedMessage.message_id == 770409083890434079 :
    #rain message
        if reactedMessage.event_type == "REACTION_ADD" :
        #added reaction
            print(f'{c.get_guild(reactedMessage.guild_id).get_member(reactedMessage.user_id).name} added rain reaction')
            #debug
            await reactedMessage.member.add_roles(reactedMessage.member.guild.get_role(697486207034064976))
            #rain role added
        else :
            print(f'error in event_type')
            #catch all

@c.event
async def on_raw_reaction_remove(reactedMessage):
#any reactions removed from messages--

    if reactedMessage.message_id == 770409082371833866 :
    #tf2 message
        if reactedMessage.event_type == "REACTION_REMOVE" :
        #removed reaction
            print(f'{c.get_guild(reactedMessage.guild_id).get_member(reactedMessage.user_id).name} removed tf2 reaction')
            await c.get_guild(reactedMessage.guild_id).get_member(reactedMessage.user_id).remove_roles(c.get_guild(reactedMessage.guild_id).get_role(697482804757266505))
        else :
            print(f'error in event_type')

    if reactedMessage.message_id == 770409082883407872 :
    #mvm message
        if reactedMessage.event_type == "REACTION_REMOVE" :
        #removed reaction
            print(f'{c.get_guild(reactedMessage.guild_id).get_member(reactedMessage.user_id).name} removed mvm reaction')
            await c.get_guild(reactedMessage.guild_id).get_member(reactedMessage.user_id).remove_roles(c.get_guild(reactedMessage.guild_id).get_role(697482914341847122))
        else :
            print(f'error in event_type')

    if reactedMessage.message_id == 770409083345829888 :
    #mc message
        if reactedMessage.event_type == "REACTION_REMOVE" :
        #removed reaction
            print(f'{c.get_guild(reactedMessage.guild_id).get_member(reactedMessage.user_id).name} removed mc reaction')
            await c.get_guild(reactedMessage.guild_id).get_member(reactedMessage.user_id).remove_roles(c.get_guild(reactedMessage.guild_id).get_role(697483011612082226))
        else :
            print(f'error in event_type')

    if reactedMessage.message_id == 770409083890434079 :
    #rain
        if reactedMessage.event_type == "REACTION_REMOVE" :
        #removed reaction
            print(f'{c.get_guild(reactedMessage.guild_id).get_member(reactedMessage.user_id).name} removed rain reaction')
            await c.get_guild(reactedMessage.guild_id).get_member(reactedMessage.user_id).remove_roles(c.get_guild(reactedMessage.guild_id).get_role(697486207034064976))
        else :
            print(f'error in event_type')

@c.event
async def on_message(message):
    #for any message this bot can see(has perms to view),
    #anywhere, any guild, any user, any channel
    #PRE EVALUATIONS
    if isSelfOrBot(message):
    #message from self or another bot
        return
    #MESSAGE DATA
    global counter
    msgA = re.sub(" +"," ",message.content.lower()).split(" ")
    #message -> lowercase -> remove duplicate spaces -> split by space -> array of strings
    msgRAW = message.content.lower()
    #message -> lowercase -> string
    msgL = len(msgA)

    #MESSAGE EVALUATIONS
    if (msgL == 0):
        return
    #prefix commands
    elif isCommand(msgA, msgL, [commandPrefix, commandPrefix2], 1, 0):
        if isCommand(msgA, msgL, ["ball"], 2, 1): #ball
            await magicball(message, msgL)
        elif isCommand(msgA, msgL, ["ping"], 2, 1): #ping
            await pong(message)
        elif isCommand(msgA, msgL, ["add"], 3, 1): #add
            await commandAdd(message, msgA, msgL, (isAdmin(message, adminID) or isOwner(message)), reactID)
        elif isCommand(msgA, msgL, ["remove"], 3, 1): #remove
            await commandRemove(message, msgA, msgL, (isAdmin(message, adminID) or isOwner(message)), reactID)
        elif isCommand(msgA, msgL, ["list"], 2, 1): #list
            await commandList(message, reactID)
        elif isCommand(msgA, msgL, ["scream"], 2, 1): #scream
            await commandScream(message)
        elif isCommand(msgA, msgL, ["clear"], 2, 1): #clear
            await commandClear(message, msgA, msgL, (isAdmin(message, adminID) or isOwner(message)))
            return
        elif isCommand(msgA, msgL, ["banana", "🍌"], 2, 1): #banana
            await commandBanana(message)
        elif isCommand(msgA, msgL, ["flip"], 2, 1): #flip
            await commandFlip(message)
        elif isCommand(msgA, msgL, ["count", "counter"], 2, 1): #counter
            await commandCounter(message, counter)
        elif isCommand(msgA, msgL, ["help"], 2, 1): #help
            await commandHelp(message)
        elif isCommand(msgA, msgL, ["fuck", "fucker", "shit", "trash", "sucks"], 2, 1): #insult
            await commandInsulted(message)
        else:
            await badCommand(message)
    #non prefix commands
    elif isCommand(msgRAW, msgL, ["nigger","nigga","nigs"], 1, -1): #censor
        await deleteMessage(message)
        return
    elif isCommand(msgA, msgL, ["ping"], 1, 0): #ping
        await pong(message)
    elif isCommand(msgA, msgL, ["gas"], 1, -1): #gas
        await gas(message)
    elif isCommand(msgA, msgL, ["british","brits","brit","britain","uk"], 1, -1): #british
        await british(message)

    await reaction(message, reactID)
    #reaction functions, monkey, random chance, etc.

    if (message.channel.id == 745099019709186108) and (len(message.content) > 128):
        await message.add_reaction(":holy_orange:796450345738829885")

#MESSAGE FUNCTIONS
async def reaction(message, reactID):
    RAND100 = random.randint(0,100)
    RAND1K = random.randint(0,1000)
    RAND10K = random.randint(0,10000)
    RAND1M = random.randint(0,1000000)
    global counter
    if isReact(message, reactID):
        await message.add_reaction(":moneky:742447598601764875")
        counter += 1 #increase monkey emote by 1
        config.updateConfigSetting("counter", counter)

    if RAND100 == 50 :
        if isReact :
            print('random event fired on react user')
        else :
            await message.add_reaction(":moneky:742447598601764875")
            counter += 1
            config.updateConfigSetting("counter", counter)

    if RAND1K == 500 :
        print('rare monkey event')
        await message.add_reaction(":moneky:742447598601764875")
        await message.add_reaction("a:moenkygay:742447673076088954")
        counter += 1
        config.updateConfigSetting("counter", counter)

    if RAND10K == 5000 :
        print("super rare monkey event")
        await message.channel.send("RANDOM CHIMP EVENT")
        await message.add_reaction(":moneky:742447598601764875")
        await message.add_reaction("🐒")
        await message.add_reaction("🍌")
        await message.add_reaction("🌮")
        counter += 1
        config.updateConfigSetting("counter", counter)

    if RAND1M == 500000 :
        print("ultra rare monkey event")
        await message.channel.send("@everyone <a:moenkygay:742447673076088954> EXTREME MONKEY MADNESS <a:moenkygay:742447673076088954> @everyone")
        await message.channel.send("@everyone <a:moenkygay:742447673076088954> EXTREME MONKEY MADNESS <a:moenkygay:742447673076088954> @everyone")
        await message.channel.send("@everyone <a:moenkygay:742447673076088954> EXTREME MONKEY MADNESS <a:moenkygay:742447673076088954> @everyone")
        await message.add_reaction(":moneky:742447598601764875")
        await message.add_reaction("🐒")
        await message.add_reaction("🍌")
        await message.add_reaction("🌮")
        counter += 1
        config.updateConfigSetting("counter", counter)
async def pong(message):
    await message.channel.send(pongReply())
async def magicball(message, messageLength):
    if messageLength > 2:
        await message.channel.send(magicballReply())
    else:
        await message.channel.send("ask me a question ape")
async def british(message):
    await message.channel.send(britishReply())
async def gas(message):
    await message.channel.send(gasReply())
async def deleteMessage(message):
    await message.delete()
    print(f'deleted message from {message.author.name}')
async def badCommand(message):
    await message.channel.send(badReply())
async def commandAdd(message, messageArray, messageLength, hasPermission, reactID):
    if messageLength > 2:
        if (messageArray[2] == "me"):
            if (message.guild.get_role(reactID) in message.author.roles):
                await message.channel.send("you were already a monkey")
                return
            await message.author.add_roles(message.guild.get_role(reactID))
            await message.channel.send(f'{message.author.name} is now a monkey')
            print(f'{message.author} added to apes')
        elif ((len(message.mentions) > 0) and hasPermission):
            if (message.guild.get_role(reactID) in message.mentions[0].roles):
                await message.channel.send(f'{message.mentions[0]} was already a monkey')
                return
            await message.mentions[0].add_roles(message.guild.get_role(reactID))
            await message.channel.send(f'{message.mentions[0]} is now a monkey')
            print(f'{message.mentions[0]} added to apes')
        else:
            await message.channel.send("who am i adding animal")
    else:
        await message.channel.send("who am i adding animal")
async def commandRemove(message, messageArray, messageLength, hasPermission, reactID):
    if messageLength > 2:
        if (messageArray[2] == "me"):
            if not (message.guild.get_role(reactID) in message.author.roles):
                await message.channel.send("you were already not a monkey")
                return
            await message.author.remove_roles(message.guild.get_role(reactID))
            await message.channel.send(f'{message.author.name} is no longer a monkey')
            print(f'{message.author} removed from apes')
        elif ((len(message.mentions) > 0) and hasPermission):
            if not (message.guild.get_role(reactID) in message.mentions[0].roles):
                await message.channel.send(f'{message.mentions[0]} was not a monkey')
                return
            await message.mentions[0].remove_roles(message.guild.get_role(reactID))
            await message.channel.send(f'{message.mentions[0]} is no longer a monkey')
            print(f'{message.mentions[0]} removed from apes')
        else:
            await message.channel.send("who am i adding animal")
    else:
        await message.channel.send("who am i removing animal")
async def commandList(message, reactID):
    await message.channel.send(f'{message.guild.get_role(reactID)} members: ')
    replyarray = []
    messagelength = 0
    replysegment = "```"
    for user in message.guild.get_role(reactID).members :
        if user.nick == None :
            messagelength += len(user.name)
        else :
            messagelength += len(user.nick)
        if messagelength > 2000 :
            print('message too long')
            return
        if messagelength > 1700 :
            replyarray.append(replysegment)
            replysegment = "```"
            if user.nick == None :
                messagelength = len(user.name)
            else :
                messagelength = len(user.nick)
        if user.nick == None :
            replysegment += user.name + "\n"
        else :
            replysegment += user.nick + "\n"
    replysegment += "```"
    replyarray.append(replysegment)
    for segment in replyarray :
        await message.channel.send(f'{segment}')
async def commandScream(message):
    await message.channel.send("OOK OOOK OOOK OOOOOOOOK")
async def commandClear(message, messageArray, messageLength, hasPermission,):
    if hasPermission:
        if messageLength > 2:
            try:
                num = int(messageArray[2])
                if num < 100:
                    await message.channel.purge(limit=(num + 1))
                    return
                elif (num == 0) or (num == 1):
                    await message.channel.purge(limit=2)
                    return
                elif num == 100:
                    await message.channel.purge(limit=num)
                    return
                else:
                    await message.channel.send('not 0 to 100 messages, cba')
            except:
                await message.channel.send('put a number ape')
    else:
        await message.channel.send("no")
    return
async def commandBanana(message):
    await message.channel.send(":) 🍌")
async def commandFlip(message):
    await message.channel.send(flipReply())
async def commandCounter(message, counter):
    await message.channel.send(str(counter))
async def commandInsulted(message):
    await message.channel.send("I will not be blackmailed by some innefectual, privileged, effete, soft-penised, debutante.")
    await message.channel.send("You want to start a street fight with me, bring it on, but you're gonna be surprised by how ugly it gets.")
    await message.channel.send("You dont even know my real name. I'm the fucking MONKEY KING")
async def commandHelp(message):
    await message.channel.send(
        "**how to speak ape:**\n"
        "\n"
        "monkey add me\t`add yourself to react list`\n"
        "monkey remove me\t`remove yourself from react list`\n"
        "monkey list\t`show list of apes`\n"
        "monkey scream\t`activate chimp`\n"
        "monkey banana\t`feed monkey`\n"
        "monkey ping\t`pong`\n"
        "monkey help\t`this command`\n"
        "monkey flip\t`flip the monkey instead of coins`\n"
        "monkey ball\t`ask the magic ape ball`\n"
        "monkey counter\t`number of monkey reactions`\n"
        "\n"
        "*admin only*\n"
        "monkey add @user\t`add user to react list`\n"
        "monkey remove @user\t`remove user from react list`\n"
        "monkey clear (0 - 100)\t`delete # of messages in channel used in`\n"
    )


#BOOLEAN FUNCTIONS
def isReact(message, reactID):
    if (message.guild.get_role(reactID) in message.author.roles):
        return True
    else:
        return False
def isAdmin(message, adminID):
    if (message.guild.get_role(adminID) in message.author.roles):
        return True
    else:
        return False
def isOwner(message):
    if (message.guild.owner_id == message.author.id):
        return True
    else:
        return False
def isSelfOrBot(message):
    if (message.author == c.user) or (message.author.bot):
        return True
    else:
        return False
def isCensor(msgRAW):
    censored = [
    "nigger",
    "nigga",
    "nigs"
    ]
    for word in censored:
        if word in msgRAW:
            return True
    return False
def isCommand(messageArray, messageLength, commandNames, minLength, location):
    if (messageLength >= minLength):
        if location == -1:
            for command in commandNames:
                if command in messageArray:
                    return True
        else:
            for command in commandNames:
                if (messageArray[location] == command):
                    return True
    return False

#REPLY ARRAYS & RANDOM SELECTION
def badReply():
    badResponses = [
        ["ook ook learn to write command ape", 10],
        ["how u expect me to read this ape", 4],
        ["?", 2],
        ["learn speak", 2],
        ["wtf is this", 1],
        ["lol", 1],
        ["chimp write command", 1],
        ["?????????", 4],
        ["can we win?", 1],
        ["OOOK", 1],
        ["何", 1],
        ["error reading chimp languag", 2],
        ["french people speak better english than u", 1],
        ["ape cant think hard enough to read that", 1],
        ["this command make monkey an alcoholic", 1]
    ]
    return random.choices([row[0] for row in badResponses], weights = [row[1] for row in badResponses], k=1)[0]
def pongReply():
    pongResponses = [
        ["pong", 30],
        ["bing bong", 5],
        ["<a:moenkygay:742447673076088954>", 1],
        ["sth99%", 1],
        ["<:hapey:749530691435495504>", 3],
        ["apeapeapepape", 2],
        ["tb ping", 5],
        ["swole time get gains", 1],
        [":taco:", 1],
        ["active server", 1],
        [":flag_fi:", 1],
        ["ping", 10],
        ["Bing.com", 1],
        ["<:excuse2:697479662246428683>", 1],
        ["<a:penguindance:747262505444966483>", 1]
    ]
    return random.choices([row[0] for row in pongResponses], weights = [row[1] for row in pongResponses], k=1)[0]
def gasReply():
    gasResponses = [
        ["did i smell gas ape?", 10],
        ["ITS KICK TIME", 5],
        ["<:nogas:742447562522492988>", 5],
        ["no gas or kick", 5],
        ["<:AAAAAA:742448034847260683>", 2],
        ["<:2gentlemenkissing:764729781069021185> <-- gas users", 2],
        ["<:simon:741938746899038319> GAS DETECTED", 1]
    ]
    return random.choices([row[0] for row in gasResponses], weights = [row[1] for row in gasResponses], k=1)[0]
def britishReply():
    britResponses = [
        ["look at me im british <:british:766724764672458793>", 10],
        ["<:british99:766724780249579610>", 5],
        ["brexit was a good idea", 5],
        ["god save the queen", 5],
        ["innit", 3],
        ["u wot", 3],
        ["govna", 3],
        ["ye im bri'ish ow'd ya kno govna", 1],
        ["u havin a go?", 1],
        [":flag_us: > :flag_gb:", 1]
    ]
    return random.choices([row[0] for row in britResponses], weights = [row[1] for row in britResponses], k=1)[0]
def magicballReply():
    ballResponses = [
        #yes
        ["OOOK OOOK YES APE",                                   10],
        ["as monkey sees it, yes",                              10],
        ["most certainly hmm yes",                              10],
        ["the banana lover says possibly",                       5],
        ["stupid question, of course",                           5],
        ["the chimps point to yes",                              5],
        ["ye probably",                                          5],
        #no
        ["sounds like ape speak, so no",                        10],
        ["the banana lover says negative",                      10],
        ["negative captain chimp",                              10],
        ["absolutely not sth99%",                                5],
        ["stupid question, hell no ape",                         5],
        ["the chimps point to no",                               5],
        ["nah",                                                  5],
        #other
        ["cba",                                                  1],
        ["i am unsure of this monkey business",                  1],
        ["ape ball scratch ass ask later",                       1],
        ["ping gergez about it",                                 1],
        ["monkey does not have the answer",                      1],
        ["i need more banana to answer this",                    1],
        ["try again later, chimp on break",                      1],
        ["OOOK OOK",                                             1],
        [":banana:!",                                            1],
        ["idk chief",                                            1],
        ["im not an 8 ball why do you think i have the answer",  1],
        ["you should consult a therapist",                       1]
    ]
    return random.choices([row[0] for row in ballResponses], weights = [row[1] for row in ballResponses], k=1)[0]
def flipReply():
    return random.choice(["*landed on his head and cracked his skull*", "*landed on his ass and broke his tailbone*"])


#LOGIN
try :
    c.run(t, bot=True)
except (discord.errors.LoginFailure, discord.errors.HTTPException) as e:
    print("Bad login, check config for correct token")
    print(f'Current token: {t}')
    quit()
