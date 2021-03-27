import discord
import random
import evals
import counter
import logging


async def reaction(message, reactID):
    RAND100 = random.randint(0, 100)
    RAND1K = random.randint(0, 1000)
    RAND10K = random.randint(0, 10000)
    RAND1M = random.randint(0, 1000000)

    if evals.isReact(message, reactID):
        if message.channel.id == 737546389969436682:
            await message.add_reaction(":monekymc:742447874633367582")
            counter.updateCounter()    
        else:
            await message.add_reaction(":moneky:742447598601764875")
            counter.updateCounter()

    if RAND100 == 50:
        if evals.isReact:
            logging.info("RAND100 on reactID member")
        elif message.channel.id == 737546389969436682:
            await message.add_reaction(":monekymc:742447874633367582")
            counter.updateCounter()
        else:
            await message.add_reaction(":moneky:742447598601764875")
            counter.updateCounter()

    if RAND1K == 500:
        logging.info("RAND1000 event")
        await message.add_reaction(":moneky:742447598601764875")
        await message.add_reaction("a:moenkygay:742447673076088954")
        counter.updateCounter()

    if RAND10K == 5000:
        logging.info("RAND10000 event")
        await message.channel.send("RANDOM CHIMP EVENT")
        await message.add_reaction(":moneky:742447598601764875")
        await message.add_reaction("🐒")
        await message.add_reaction("🍌")
        await message.add_reaction("🌮")
        counter.updateCounter()

    if RAND1M == 500000:
        logging.info("RAND100000 event")
        await message.channel.send(
            "@everyone <a:moenkygay:742447673076088954> EXTREME MONKEY MADNESS <a:moenkygay:742447673076088954> @everyone"
        )
        await message.add_reaction(":moneky:742447598601764875")
        await message.add_reaction("🐒")
        await message.add_reaction("🍌")
        await message.add_reaction("🌮")
        counter.updateCounter()