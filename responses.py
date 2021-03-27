import random

# REPLY ARRAYS & RANDOM SELECTION
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
        ["this command make monkey an alcoholic", 1],
    ]
    return random.choices(
        [row[0] for row in badResponses], weights=[row[1] for row in badResponses], k=1
    )[0]


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
        ["🌮", 1],
        ["active server", 1],
        ["\U0001f1eb\U0001f1ee", 1],
        ["ping", 10],
        ["Bing.com", 1],
        ["<:excuse2:697479662246428683>", 1],
        ["<a:penguindance:747262505444966483>", 1],
    ]
    return random.choices(
        [row[0] for row in pongResponses],
        weights=[row[1] for row in pongResponses],
        k=1,
    )[0]


def gasReply():
    gasResponses = [
        ["did i smell gas ape?", 10],
        ["ITS KICK TIME", 5],
        ["<:nogas:742447562522492988>", 5],
        ["no gas or kick", 5],
        ["<:AAAAAA:742448034847260683>", 2],
        ["<:2gentlemenkissing:764729781069021185> <-- gas users", 2],
        ["<:simon:741938746899038319> GAS DETECTED", 1],
    ]
    return random.choices(
        [row[0] for row in gasResponses], weights=[row[1] for row in gasResponses], k=1
    )[0]


def britishReply():
    britResponses = [
        ["look at me im british <:british99:766724780249579610>", 10],
        ["<:british99:766724780249579610>", 5],
        ["brexit was a good idea", 5],
        ["god save the queen", 5],
        ["innit", 3],
        ["u wot", 3],
        ["govna", 3],
        ["ye im bri'ish ow'd ya kno govna", 1],
        ["u havin a go?", 1],
        ["\U0001f1fa\U0001f1f8 > \U0001f1ec\U0001f1e7", 1],
    ]
    return random.choices(
        [row[0] for row in britResponses],
        weights=[row[1] for row in britResponses],
        k=1,
    )[0]


def magicballReply():
    ballResponses = [
        # yes
        ["OOOK OOOK YES APE", 10],
        ["as monkey sees it, yes", 10],
        ["most certainly hmm yes", 10],
        ["the banana lover says possibly", 5],
        ["stupid question, of course", 5],
        ["the chimps point to yes", 5],
        ["ye probably", 5],
        # no
        ["sounds like ape speak, so no", 10],
        ["the banana lover says negative", 10],
        ["negative captain chimp", 10],
        ["absolutely not sth99%", 5],
        ["stupid question, hell no ape", 5],
        ["the chimps point to no", 5],
        ["nah", 5],
        # other
        ["cba", 1],
        ["i am unsure of this monkey business", 1],
        ["ape ball scratch ass ask later", 1],
        ["ping gergez about it", 1],
        ["monkey does not have the answer", 1],
        ["i need more banana to answer this", 1],
        ["try again later, chimp on break", 1],
        ["OOOK OOK", 1],
        ["🍌!", 1],
        ["idk chief", 1],
        ["im not an 8 ball why do you think i have the answer", 1],
        ["you should consult a therapist", 1],
    ]
    return random.choices(
        [row[0] for row in ballResponses],
        weights=[row[1] for row in ballResponses],
        k=1,
    )[0]


def flipReply():
    return random.choice(
        [
            "*landed on his head and cracked his skull*",
            "*landed on his ass and broke his tailbone*",
        ]
    )
