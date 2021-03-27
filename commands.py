import discord
import logging
import counter
import responses
import roleconfig
import re
import uwuify

#all commands take a message object and argumentDictionary as arguments
#the first being an object containing basic info about author, guild, channel, etc.
#and the latter a dict containing all info from config.cfg,
#whether the user has elevated permission status at the time of the recieved message,
#and the message array after regex & split conversion

#"ping" -> "pong"
async def pong(message, argDict):
    await message.channel.send(responses.pongReply())

#magicball <y/n question>
async def magicball(message, argDict):
    if len(argDict["messageArray"]) > 2:
        await message.channel.send(responses.magicballReply())
    else:
        await message.channel.send("ask me a question ape")

#brit, british, etc replies
async def british(message, argDict):
    await message.channel.send(responses.britishReply())

#gas replies
async def gas(message, argDict):
    await message.channel.send(responses.gasReply())

#censor, future use for generic deleting sent message
async def deleteMessage(message, argDict):
    await message.delete()
    logging.info("deleted message from %s", message.author.name)

#bad command reply
async def badCommand(message, argDict):
    await message.channel.send(responses.badReply())

#generic react role adding for monkey reactions
async def add(message, argDict):
    if len(argDict["messageArray"]) > 2:
        #monkey add me
        if argDict["messageArray"][2] == "me":
            #if they have react role already
            if message.guild.get_role(argDict["CONFIG"].REACT_ID) in message.author.roles:
                await message.channel.send("you were already a monkey")
                return
            #else give them role and log
            await message.author.add_roles(message.guild.get_role(argDict["CONFIG"].REACT_ID))
            await message.channel.send(f"{message.author.name} is now a monkey")
            logging.info("added %s to apes", message.author)
        #monkey add @person & elevated permissions
        elif (len(message.mentions) > 0) and argDict["hasPermission"]:
            #always grabs first mention and drops rest, todo support multi adding
            #if chosen person has react role already
            if message.guild.get_role(argDict["CONFIG"].REACT_ID) in message.mentions[0].roles:
                await message.channel.send(
                    f"{message.mentions[0]} was already a monkey"
                )
                return
            #else give them role and log
            await message.mentions[0].add_roles(message.guild.get_role(argDict["CONFIG"].REACT_ID))
            await message.channel.send(f"{message.mentions[0]} is now a monkey")
            logging.info("added %s to apes", message.mentions[0])
        #if person has not typed me or @person and has elevated permissions
        elif argDict["hasPermission"]:
            await message.channel.send("who am i adding animal")
        #if person has not typed me and does not have elevated perms
        else:
            await message.channel.send('put "me"  you ape')
    #if message is just monkey add
    else:
        await message.channel.send("wtf am i adding animal")

#generic react role removal for monkey reactions
async def remove(message, argDict):
    if len(argDict["messageArray"]) > 2:
        if argDict["messageArray"][2] == "me":
            if not (message.guild.get_role(argDict["CONFIG"].REACT_ID) in message.author.roles):
                await message.channel.send("you were already not a monkey")
                return
            await message.author.remove_roles(message.guild.get_role(argDict["CONFIG"].REACT_ID))
            await message.channel.send(f"{message.author.name} is no longer a monkey")
            logging.info("removed %s from apes", message.author)
        elif (len(message.mentions) > 0) and argDict["hasPermission"]:
            if not (message.guild.get_role(argDict["CONFIG"].REACT_ID) in message.mentions[0].roles):
                await message.channel.send(f"{message.mentions[0]} was not a monkey")
                return
            await message.mentions[0].remove_roles(message.guild.get_role(argDict["CONFIG"].REACT_ID))
            await message.channel.send(f"{message.mentions[0]} is no longer a monkey")
            logging.info("removed %s from apes", message.mentions[0])
        else:
            await message.channel.send("who am i adding animal")
    else:
        await message.channel.send("who am i removing animal")


async def reactlist(message, argDict):
    reactID = argDict["CONFIG"].REACT_ID
    await message.channel.send(f"{message.guild.get_role(reactID)} members: ")
    replyarray = []
    messagelength = 0
    replysegment = "```\n"
    for user in message.guild.get_role(argDict["CONFIG"].REACT_ID).members:
        if user.nick == None:
            messagelength += len(user.name)
        else:
            messagelength += len(user.nick)
        if messagelength > 2000:
            logging.error("message too long")
            return
        if messagelength > 1700:
            replyarray.append(replysegment)
            replysegment = "```"
            if user.nick == None:
                messagelength = len(user.name)
            else:
                messagelength = len(user.nick)
        if user.nick == None:
            replysegment += user.name + "\n"
        else:
            replysegment += user.nick + "\n"
    replysegment += "```"
    replyarray.append(replysegment)
    for segment in replyarray:
        await message.channel.send(f"{segment}")


async def scream(message, argDict):
    await message.channel.send("OOK OOOK OOOK OOOOOOOOK")


async def clear(message, argDict):
    if argDict["hasPermission"]:
        if len(argDict["messageArray"]) > 2:
            try:
                num = int(argDict["messageArray"][2])
                if num < 100:
                    logging.warning(
                        "user %s purged %s messages from #%s",
                        message.author,
                        num + 1,
                        message.channel.name,
                    )
                    await message.channel.purge(limit=(num + 1))
                    return
                elif (num == 0) or (num == 1):
                    logging.warning(
                        "user %s purged 2 messages from #%s",
                        message.author,
                        message.channel.name,
                    )
                    await message.channel.purge(limit=2)
                    return
                elif num == 100:
                    logging.warning(
                        "user %s purged 100 messages from #%s",
                        message.author,
                        message.channel.name,
                    )
                    await message.channel.purge(limit=num)
                    return
                else:
                    await message.channel.send("not 0 to 100 messages, cba")
            except:
                await message.channel.send("put a number ape")
    else:
        await message.channel.send("no")
    return


async def banana(message, argDict):
    await message.channel.send(":) 🍌")


async def flip(message, argDict):
    await message.channel.send(responses.flipReply())


async def reactcount(message, argDict):
    await message.channel.send(counter.getCounter())


async def insulted(message, argDict):
    await message.channel.send(
        "I will not be blackmailed by some innefectual, privileged, effete, soft-penised, debutante."
    )
    await message.channel.send(
        "You want to start a street fight with me, bring it on, but you're gonna be surprised by how ugly it gets."
    )
    await message.channel.send(
        "You dont even know my real name. I'm the fucking MONKEY KING"
    )


async def help(message, argDict):
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
        "monkey muteathon rules\t`rules for discord muteathons`\n"
        "\n"
        "*admin only*\n"
        "monkey add @user\t`add user to react list`\n"
        "monkey remove @user\t`remove user from react list`\n"
        "monkey clear (0 - 100)\t`delete # of messages in channel used in`\n"
        "monkey muteathon begin\t`start a muteathon in current voice channel`\n"
        "monkey muteathon cancel\t`cancels the active muteathon`\n"
        "monkey rolereact add roleID\t`adds a role with given id to role-selection`\n"
        "monkey rolereact remove msgID\t`removes a msg with given id from role-selection`\n"
    )


async def muteathon(message, argDict):
    if len(argDict["messageArray"]) > 2:
        if argDict["messageArray"][2] == "rules":
            await message.channel.send(
                "Muteathon Rules:"
                "\n> 1. All Contestants must stay **Muted** and **Undeafened** for the duration of the Muteathon."
                "\n> 2. Leaving the voice channel at any time will automatically remove you from the competition."
                "\n> 3. Going AFK will remove contestants after 15 minutes."
                "\n> 4. Moving contestants is stricly not allowed and permissions will be revoked from those who do so."
            )
            return
        if argDict["messageArray"][2] == "cancel" and argDict["hasPermission"]:
            logging.info("muteathon cancelled, wiping MUTE role members")
            for users in message.guild.get_role(809905948910944277).members:
                users.remove_roles(message.guild.get_role(809905948910944277))
            logging.info("wipe complete")
            await message.channel.send("Muteathon cancelled")
            return
        if argDict["messageArray"][2] == "begin" and argDict["hasPermission"]:
            inValidChannel = False
            if message.author.voice != None and message.author.voice.channel != None:
                # in a voice channel
                logging.info(
                    "%s began muteathon detection in voice channel: %s",
                    message.author.name,
                    message.author.voice.channel.name,
                )
                channelMembers = []  # list of users in current voice channel
                for user in message.author.voice.channel.members:  
                    # list of users in voice channel
                    if user.bot:
                        continue  # not counting bots
                    if not user.voice.self_mute:
                        continue
                    if user.voice.self_deaf:
                        continue
                    if user.voice.afk:
                        continue
                    logging.info(
                        "%s detected in channel",
                        user.name,
                    )
                    channelMembers.append(
                        user
                    )  # add to the non-bot channelMembers list
                logging.info("%s total non-bot channelMembers", len(channelMembers))
                if len(channelMembers) >= 2:
                    logging.info("muteathon has valid number of members")
                    inValidChannel = True
                else:
                    logging.info("muteathon has invalid number of members")
            if inValidChannel:
                ow = discord.PermissionOverwrite()
                ow.move_members = False
                everyoneRole = message.guild.get_role(402355423287574529)
                await message.author.voice.channel.set_permissions(everyoneRole, overwrite=ow)
                for user in channelMembers:
                    await user.add_roles(message.guild.get_role(809905948910944277))
                await message.channel.send(
                    "Muteathon begun with the following participants:"
                )
                replyarray = []
                messagelength = 0
                replysegment = "```\n"
                for user in channelMembers:
                    if user.nick == None:
                        messagelength += len(user.name)
                    else:
                        messagelength += len(user.nick)
                    if messagelength > 2000:
                        logging.error("message too long")
                        return
                    if messagelength > 1700:
                        replyarray.append(replysegment)
                        replysegment = "```"
                        if user.nick == None:
                            messagelength = len(user.name)
                        else:
                            messagelength = len(user.nick)
                    if user.nick == None:
                        replysegment += user.name + "\n"
                    else:
                        replysegment += user.nick + "\n"
                replysegment += "```"
                replyarray.append(replysegment)
                for segment in replyarray:
                    await message.channel.send(f"{segment}")
        elif (
            argDict["hasPermission"]
        ):  # "monkey muteathon ..." but not in channel or channel has <2 non-bot users in it
            await message.channel.send(
                "Review rules or join a channel to start a muteathon"
            )
        else:
            await message.channel.send('Review rules with "muteathon rules"')
    else:  # "monkey muteathon"
        await message.channel.send(
            'Start a muteathon by joining a channel and typing "muteathon begin", or for rules type "muteathon rules"'
        )


async def rolereact(message, argDict):
    # monkey rolereact add roleid
    # monkey rolereact remove msgid
    if argDict["hasPermission"]:
        if argDict["messageArray"][2] == "add" and len(argDict["messageArray"]) > 3:
            roleID = None
            try:
                roleID = int(argDict["messageArray"][3])
            except ValueError:
                logging.warning("desired role was not an integer")
            if not message.guild.get_role(roleID) == None:
                if len(argDict["messageArray"]) == 4:
                    try:
                        sentmessage = await message.guild.get_channel(argDict["CONFIG"].ROLECHAN_ID).send(
                            f"**{message.guild.get_role(roleID).name}**"
                        )
                        await sentmessage.add_reaction("a:moenkygay:742447673076088954")
                        roleconfig.addRoleReact(sentmessage.id, roleID)
                        logging.info(
                            "added rolereact message in ROLECHAN with msgid %s and roleid %s",
                            sentmessage.id,
                            roleID,
                        )
                    except (
                        discord.errors.HTTPException,
                        discord.errors.InvalidArgument,
                    ):
                        logging.error(
                            "failed to retrieve message sent in ROLECHAN, roleconfig not updated"
                        )
                else:
                    msgA = re.sub(" +", " ", message.content).split(" ")
                    description = ""
                    for x in range(len(msgA)):
                        if x > 3:
                            description += msgA[x] + " "
                    try:
                        sentmessage = await message.guild.get_channel(argDict["CONFIG"].ROLECHAN_ID).send(
                            f"**{description}({message.guild.get_role(roleID).name})**"
                        )
                        await sentmessage.add_reaction("a:moenkygay:742447673076088954")
                        roleconfig.addRoleReact(sentmessage.id, roleID)
                        logging.info(
                            "added rolereact message in ROLECHAN with msgid %s and roleid %s",
                            sentmessage.id,
                            roleID,
                        )
                    except (
                        discord.errors.HTTPException,
                        discord.errors.InvalidArgument,
                    ):
                        logging.error(
                            "failed to retrieve message sent in ROLECHAN, roleconfig not updated"
                        )
            else:
                await message.channel.send("Role not found")
        elif argDict["messageArray"][2] == "remove":
            try:
                roleconfig.removeRoleReact(argDict["messageArray"][3])
                desiredmessage = await message.guild.get_channel(
                    argDict["CONFIG"].ROLECHAN_ID
                ).fetch_message(argDict["messageArray"][3])
                await desiredmessage.delete()
            except discord.errors.NotFound:
                await message.channel.send("Message not found")
                return
            except (discord.errors.HTTPException, discord.errors.InvalidArgument):
                logging.error(
                    "failed to retrieve desiredmessage to delete from ROLECHAN"
                )
        else:
            await message.channel.send(
                "Usage: `rolereact add msgID roleID (opt desc)` to create a new message for role-selection, or rolereact remove msgID to remove an existing one"
            )
    else:

        await message.channel.send("u have no permission animal")

async def translator(message, argDict):
    #monkey translate ....
    #12345678901234567

    toTranslate = message.content[17:]
    logging.info("attempting to translate text")

    text = uwuify.uwu(toTranslate)

    if text == "":
        await message.channel.send("can't translate ape")
    else:
        await message.channel.send(f"{text}")