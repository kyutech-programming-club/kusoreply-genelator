import nltk

def deny_sentence(en_sentence):
    tokens = nltk.word_tokenize(en_sentence)
    tagged = nltk.pos_tag(tokens)
    denied_en_sentence = ""
    for (token, tag) in tagged:
        if tag[:2] == "VB" and token in ["is", "am","are", "was", "were", "be", "do", "did", "does"]:
            denied_en_sentence += token + " not "
        elif tag == "VBD":
            denied_en_sentence += "did not " + token + " "
        elif tag in ["VB", "VBP"] and token != "Let":
            denied_en_sentence += "do not " + token + " "
        elif tag == "VBZ":
            denied_en_sentence += "dose not " + token + " "
        elif token in ["Let", "Please"]:
            continue
        else:
            denied_en_sentence += token + " "
    return denied_en_sentence[:-1]