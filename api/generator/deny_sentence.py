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
            denied_en_sentence += "do not "
        elif i < len(tagged)-1 and tagged[i+1][0] == "not":
            denied_en_sentence += token + " "
        elif i > 0 and tagged[i-1][0] in ["not", "to"]:
            denied_en_sentence += token + " "
        elif tag[:2] == "VB" and token in ["is", "am","are", "was", "were", "be", "do", "did", "does", "'m"]:
            denied_en_sentence += token + " not "
        elif tag == "VBD":
            denied_en_sentence += "did not " + token + " "
        elif tag in ["VB", "VBP"] and token != "Let":
            if i > 0 and tagged[i-1][1] == 'MD':
                denied_en_sentence += "not " + token + " "
            else:
                denied_en_sentence += "do not " + token + " "
        elif tag == "VBZ":
            if i > 0 and tagged[i-1][1] == 'MD':
                denied_en_sentence += "not " + token + " "
            else:
                denied_en_sentence += "does not " + token + " "
        else:
            denied_en_sentence += token + " "

    return denied_en_sentence[:-1]
