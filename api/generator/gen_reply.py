import random

from .calc_negaposi import calc_negaposi
from .kuso_reply_data import KUSO_REPLY

def gen_reply_from_negaposi(negaposi):
    if 0 < negaposi:
        reply = random.choice(KUSO_REPLY["positive"])
    elif negaposi < 0:
        reply = random.choice(KUSO_REPLY["negative"])
    else:
        reply = random.choice(KUSO_REPLY["neutral"])

    return reply

def gen_reply(input_text):
    print("input text:", input_text)
    negaposi = calc_negaposi(input_text)
    # reply = "だからなんですか"
    reply = gen_reply_from_negaposi(negaposi)
    return reply

if __name__ == '__main__':
    print(gen_reply("Hello, World!"))
