import discord
import re
import config
import counter
import logging
import monkeylogs
import commands
import commandstruct
import evals
import reacts
import roleconfig
from aiohttp import connector
import builtins
import os
import socket

logging.info("-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-")
logging.info("started loading configs...")
config = config.loadConfig()
counter.loadCounter()
roleconfig.loadRoleReact()
logging.info("finished loading configs")

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.voice_states = True
c = discord.Client(intents=intents)

commandList = commandstruct.createCommands()

@c.event
async def on_ready():
    logging.info("%s has connected to discord", c.user)
    await c.get_channel(config.BOTCHAN_ID).send(
        f"Ook Ook, im MonekyBot :banana:\nThere are {counter.getCounter()} <:moneky:742447598601764875> in the zoo"
    )
    logging.info("loaded %s users into cache", len(c.users))

    logging.info("wiping MUTE role members")
    for users in c.get_guild(config.GUILD_ID).get_role(config.MUTEROLE_ID).members:
        users.remove_roles(c.get_guild(config.GUILD_ID).get_role(config.MUTEROLE_ID))
    logging.info("wipe complete")

@c.event
async def on_voice_state_update(member, before, after):
    if not c.get_guild(config.GUILD_ID).get_role(config.MUTEROLE_ID) in member.roles:
        return
    revokeMute = False
    # check if deafened
    if after.self_deaf:
        revokeMute = True
    # check if unmuted
    if not after.self_mute:
        revokeMute = True
    # check if channel changed
    if after.channel != before.channel:
        revokeMute = True
    if revokeMute:
        logging.info("user %s had MUTE role revoked", member)
        await member.remove_roles(c.get_guild(config.GUILD_ID).get_role(config.MUTEROLE_ID))
        logging.info(
            "MUTE members left: %s",
            len(c.get_guild(config.GUILD_ID).get_role(config.MUTEROLE_ID).members),
        )
        if len(c.get_guild(config.GUILD_ID).get_role(config.MUTEROLE_ID).members) == 1:
            logging.info("Muteathon concluded with winner %s", c.get_guild(config.GUILD_ID).get_role(config.MUTEROLE_ID).members[0])
            await c.get_channel(697486819880599683).send(
                f"MUTEATHON WINNER: {c.get_guild(config.GUILD_ID).get_role(config.MUTEROLE_ID).members[0].mention}")
            ow = discord.PermissionOverwrite()
            ow.move_members = None
            everyoneRole = c.get_guild(config.GUILD_ID).get_role(402355423287574529)
            await c.get_guild(config.GUILD_ID).get_role(config.MUTEROLE_ID).members[0].voice.channel.set_permissions(everyoneRole, overwrite=ow)
            await c.get_guild(config.GUILD_ID).get_role(config.MUTEROLE_ID).members[0].remove_roles(c.get_guild(config.GUILD_ID).get_role(config.MUTEROLE_ID))

@c.event
async def on_message(message):
    #no bots
    if evals.isSelfOrBot(message, c.user):
        return

    msgA = re.sub(" +", " ", message.content.lower()).split(" ")
    # message -> lowercase -> remove duplicate spaces -> split by space -> array of strings

    if len(msgA) == 0:
        return

    #elevated perms for owner of guild or admin role members
    hasPermission = evals.isAdmin(message, config.ADMIN_ID) or evals.isOwner(message)

    #data to pass to command functions
    argumentDict = {
        "CONFIG" : config,
        "messageArray" : msgA,
        "hasPermission" : hasPermission,
    }

    if evals.isCommand(msgA, config.PREFIX, 1, 0):
        #prefix commands
        isBadCommand = True
        #will reply with bad command if no valid function is called
        for attr in vars(commandList):
            #list of commands
            command = getattr(commandList, attr)
            #if the command's prefix setting is False, don't evaluate
            if not command["prefix"]:
                continue
            if evals.isCommand(msgA, command["aliases"], command["minlen"], command["pos"]):
                await command["func"](message, argumentDict)
                isBadCommand = False
                continue
        if isBadCommand:
            await commands.badCommand(message, argumentDict)
    else:
        #no prefix commands
        for attr in vars(commandList):
            #list of commands
            command = getattr(commandList, attr)
            #if the command's prefix setting is True, don't evaluate
            if command["prefix"]:
                continue
            #evaluate if recieved message is one of the non-prefix commands with the required arguments
            if evals.isCommand(msgA, command["aliases"], command["minlen"], command["pos"]):
                #evals true and call the desired function
                await command["func"](message, argumentDict)
                continue

    try:
        #attempt to add reaction based on message author's react role
        await reacts.reaction(message, config.REACT_ID)
    except Exception:
        logging.warning("reaction failed, message likely deleted")

    if (message.channel.id == config.BINDSCHAN_ID) and (len(message.content) > 128):
        try:
            await message.add_reaction(":holy_orange:796450345738829885")
        except Exception:
            logging.warning("reaction failed, message likely deleted")

@c.event
async def on_raw_reaction_add(msg):
    if msg.member.bot:
        return
    if not msg.channel_id == config.ROLECHAN_ID:
        return
    if not msg.event_type == "REACTION_ADD":
        return
    
    ROLEREACT_DICT = roleconfig.getRoleReact()
    try:
        ROLEREACT_DICT[str(msg.message_id)]
        logging.info("%s added %s reaction", 
        msg.member.name,
        c.get_guild(msg.guild_id).get_role(ROLEREACT_DICT[str(msg.message_id)]))
        
        await msg.member.add_roles(
            msg.member.guild.get_role(ROLEREACT_DICT[str(msg.message_id)]))
    except KeyError:
        logging.warning("message %s not found in dict", msg.message_id)

@c.event
async def on_raw_reaction_remove(msg): 
    if not msg.channel_id == config.ROLECHAN_ID:
        return
    if not msg.event_type == "REACTION_REMOVE":
        return

    ROLEREACT_DICT = roleconfig.getRoleReact()
    try:
        ROLEREACT_DICT[str(msg.message_id)]
        logging.info("%s removed %s reaction", 
        c.get_guild(msg.guild_id).get_member(msg.user_id).name,
        c.get_guild(msg.guild_id).get_role(ROLEREACT_DICT[str(msg.message_id)]))
        
        await c.get_guild(msg.guild_id).get_member(msg.user_id).remove_roles(
            c.get_guild(msg.guild_id).get_role(ROLEREACT_DICT[str(msg.message_id)]))
    except KeyError:
        logging.warning("message %s not found in dict", msg.message_id)


# login
logging.info("bot logging in...")
try:
    c.run(config.TOKEN)
except (discord.errors.LoginFailure, discord.errors.HTTPException):
    logging.error("bad login, check config.json for correct token")
    quit()
except (connector.ClientConnectionError, discord.errors.ConnectionClosed, socket.gaierror):
    logging.error("failed to connect")
