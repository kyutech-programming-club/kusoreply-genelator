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
        print('\"' + i.rstrip() + '\"')

    print("-------------------------")
    for i in neut:
        print('\"' + i.rstrip() + '\"')

    print("-------------------------")
    for i in nega:
        print('\"' + i.rstrip() + '\"')

KUSO_REPLY = {
    "positive": [
        "もうおそいですよ"
        "いやです"
        "ぼっち乙です"
        "寝たわけ無いやろ"
        "わかりました。僕は行きませんけど"
        "ちゃんと寝てますか？"
        "僕はわかりません"
        "やらなくていいですよ"
        "明日からは遅いです"
        "まずそう"
        "誰も君とはやりたくない"
        "行きたくないです"
        "もっと暑いところもありますよ"
        "どこが？"
        "明日働いている人に不謹慎じゃないですか"
        "それは文句ですか"
        "わかりました。しませんけど"
        "きもいです"
    ],
    "neutral": [
        "もうおそいですよ"
        "いやです"
        "ぼっち乙です"
        "寝たわけ無いやろ"
        "わかりました。僕は行きませんけど"
        "ちゃんと寝てますか？"
        "僕はわかりません"
        "やらなくていいですよ"
        "明日からは遅いです"
        "まずそう"
        "誰も君とはやりたくない"
        "行きたくないです"
        "もっと暑いところもありますよ"
        "どこが？"
        "明日働いている人に不謹慎じゃないですか"
        "それは文句ですか"
        "わかりました。しませんけど"
        "きもいです"
    ],
    "negative": [
        "ちゃんとごはんたべてますか"
        "自炊しろ"
        "そんなのもわからないんですね"
        "おかげで合格できました"
        "そんなんもわからんのかww"
        "嫌です"
        "負けるやつおる？"
        "綺麗事いうな"
        "暴力反対です"
        "あなたとは誰も付き合いませんね"
        "嫌です"
        "老害ですね"
        "お前ももう死んでいる"
        "私はすぐ思いつきます"
        "そして眼鏡も似合ってない"
        "視野狭そう"
        "実装されてないね"
        "そうですね！"
        "きのこ関係者に誤ってください"
    ],
}

if __name__ == '__main__':
    data_formatter()
