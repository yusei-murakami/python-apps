import random
dict = {
    "いくら": "北海道",
    "ひらめ": "青森県",
    "カラメ餅": "岩手県",
    "牛タン": "宮城県",
    "いぶりがっこ": "秋田県",
    "さくらんぼ": "山形県",
    "きゅうり": "福島県",
    "水戸納豆": "茨城県",
    "餃子": "栃木県",
    "こんにゃく": "群馬県",
    "さといも": "埼玉県",
    "落花生": "千葉県",
    "うなぎ": "東京都",
    "あなご": "神奈川県",
    "柿の種": "新潟県",
    "白えび": "富山県",
    "きんつば": "石川県",
    "越前おろしそば": "福井県",
    "ぶどう": "山梨県",
    "信州そば": "長野県",
    "栗きんとん": "岐阜県",
    "茶": "静岡県",
    "味噌カツ": "愛知県",
    "伊勢エビ": "三重県",
    "鮒寿司": "滋賀県",
    "漬物": "京都府",
    "たこ焼き": "大阪府",
    "丹波黒豆": "兵庫県",
    "茶がゆ": "奈良県",
    "梅": "和歌山県",
    "梨": "鳥取県",
    "出雲そば": "島根県",
    "桃": "岡山県",
    "牡蠣": "広島県",
    "瓦そば": "山口県",
    "酢橘": "徳島県",
    "うどん": "香川県",
    "みかん": "愛媛県",
    "カツオ": "高知県",
    "辛子明太子": "福岡県",
    "イカ": "佐賀県",
    "カステラ": "長崎県",
    "馬刺し": "熊本県",
    "とり天": "大分県",
    "マンゴー": "宮崎県",
    "さつま揚げ": "鹿児島県",
    "パイナップル": "沖縄県"
}
def clean(pref):
    return pref.replace("都", "").replace("道", "").replace("府", "").replace("県", "")

print("★ 全国名産品 都道府県当てクイズ ★")
print("名産品の名前が表示されるので、それがどこの都道府県かを当ててください。")
print("例：『りんご』→『青森』 または『青森県』 どちらでもOKです。")
print("終了したいときは 'exit' と入力してください。")


correct = 0
wrong = 0
mistakes = []

while True:
    item = random.choice(list(dict.items()))
    product = item[0]
    answer = item[1]

    user = input(product + " はどこの都道府県？：")

    if user == "exit":
        break

    if clean(user) == clean(answer):
        print("◎ 正解！")
        correct += 1
    else:
        print("× 不正解。正解は " + answer)
        wrong += 1
        mistakes.append((product, user, answer))

total = correct + wrong
print("\n--- 結果 ---")
print("正解：", correct, "/", total)
if total > 0:
    rate = correct / total * 100
    print("正解率：", round(rate, 1), "%")

if mistakes:
    print("\n間違えた問題：")
    for m in mistakes:
        print("・", m[0], "→ あなたの答え：", m[1], " / 正解：", m[2])
else:
    print("全問正解！お見事！")