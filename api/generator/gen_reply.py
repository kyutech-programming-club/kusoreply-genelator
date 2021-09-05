import random
from googletrans import Translator

from .calc_negaposi import calc_negaposi
from .deny_sentence import deny_sentence
from .kuso_reply_data import KUSO_REPLY, COMB_KUSO_REPLY1, COMB_KUSO_REPLY2

def gen_reply_from_negaposi(negaposi):
    if 0 < negaposi:
        reply = random.choice(KUSO_REPLY["positive"])
    elif negaposi < 0:
        reply = random.choice(KUSO_REPLY["negative"])
    else:
        reply = random.choice(KUSO_REPLY["neutral"])

    return reply

def gen_reply_from_combination():
    reply = random.choice(COMB_KUSO_REPLY1) + random.choice(COMB_KUSO_REPLY2)
    return reply

translator = Translator()
def gen_reply_from_denial(sentence):
    en_sentence = translator.translate(sentence, dest='en',src='ja').text
    denied_en_sentence = deny_sentence(en_sentence)
    reply = translator.translate(denied_en_sentence, dest='ja', src='en').text
    return reply

def gen_reply(input_text):
    print("input text:", input_text)
    negaposi = calc_negaposi(input_text)
    reply = {'negaposi':'', 'comb':'', 'deny':''}
    reply['negaposi'] = gen_reply_from_negaposi(negaposi)
    reply['comb'] = gen_reply_from_combination()
    reply['deny'] = gen_reply_from_denial(input_text)
    return reply

if __name__ == '__main__':
    print(gen_reply("Hello, World!"))
