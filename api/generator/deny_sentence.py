import nltk

def deny_sentence(en_sentence):
    tokens = nltk.word_tokenize(en_sentence)
    tagged = nltk.pos_tag(tokens)
    denied_en_sentence = ""
    for i, (token, tag) in enumerate(tagged):
        print(tagged[i])
        if token == "not":
            continue
        elif token == "please":
            reply += "do not "
        elif i < len(tagged)-1 and tagged[i+1][0] == "not":
            reply += token + " "
        elif i > 0 and tagged[i-1][0] in ["not", "to"]:
            reply += token + " "
        elif tag[:2] == "VB" and token in ["is", "am","are", "was", "were", "be", "do", "did", "does", "'m"]:
            reply += token + " not "
        elif tag == "VBD":
            reply += "did not " + token + " "
        elif tag in ["VB", "VBP"] and token != "Let":
            if i > 0 and tagged[i-1][1] == 'MD':
                reply += "not " + token + " "
            else:
                reply += "do not " + token + " "
        elif tag == "VBZ":
            if i > 0 and tagged[i-1][1] == 'MD':
                reply += "not " + token + " "
            else:
                reply += "does not " + token + " "
        else:
            reply += token + " "

    return denied_en_sentence[:-1]
