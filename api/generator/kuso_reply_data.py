def data_formatter():
    raw_text = []
    raw = open("raw_text.txt", "r")
    for line in raw:
        raw_text.append(line)
    raw.close()

    raw_score = []
    raw = open("raw_score.txt", "r")
    for line in raw:
        raw_score.append(line)
    raw.close()

    posi = []
    neut = []
    nega = []

    for i in range(len(raw_text)):
        if float(raw_score[i]) < 0:
            nega.append(raw_text[i])
        elif 0 < float(raw_score[i]):
            posi.append(raw_text[i])
        else:
            neut.append(raw_text[i])

    print("-------------------------")
    for i in posi:
        print('\"' + i.rstrip() + '\",')

    print("-------------------------")
    for i in neut:
        print('\"' + i.rstrip() + '\",')

    print("-------------------------")
    for i in nega:
        print('\"' + i.rstrip() + '\",')

KUSO_REPLY = {
    "positive": [
        "それは本心ですか？",
        "不謹慎だとは思わないんですか！",
        "お前の話なんて聞きたくねーよ",
        "勘違いお疲れ様です",
        "僕は大嫌い",
        "アホですか？",
        "かわいくないね",
        "だからなんですか",
        "たぶん無理ですね笑",
        "中学生ですか？",
        "あなたが幸せそうで非常に残念です",
        "長すぎて読む気にならん",
        "そんなことより、親孝行しろ",
        "頭悪そう",
        "僕はそうは思いません",
        "ダカラなんですか",
        "綺麗事いうな！世の中のために動け",
    ],
    "neutral": [
        "また歳をとったね",
        "もうおそいですよ",
        "いやです",
        "ちゃんと寝てますか？",
        "僕はそう思いません",
        "きもいです",
    ],
    "negative": [
        "人の不幸は蜜の味。ありがとうございます"
        "ちゃんとごはんたべてますか?",
        "私事ですが、大学合格しました",
        "僕は今幸せの大絶頂でーーす",
        "不幸な人を見つけるのってこんなに気持ちいいんですねぇ",
        "お前はもう死んでいる",
        "そうですね！同情します（ニッコリ）",
        ""
    ],
}

COMB_KUSO_REPLY1 = [
    "調子のんな！",
    "どうでもいいんだよ！",
    "だからなんだよ！",
    "不謹慎じゃないですか！",
    "それなんか意味ある？",
    "それってあなたの感想ですよね。",
    "なんだろう、嘘つくのやめてもらっていいですか。",
    "それってなにか根拠あるんですか。"
]

COMB_KUSO_REPLY2 = [
    "ハゲが。", "たこが。", "くそが！！！", "ばかが！！！", "あほが。", "ガキが。"
]

if __name__ == '__main__':
    data_formatter()
