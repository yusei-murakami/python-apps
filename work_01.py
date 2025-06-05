#1.ランダムな数字を生成して出力するプログラム
#2.入力された文字列もそのまま出力するプログラム
#3.数学が合っているか判定すします
#4.
#5.

import random

while True:
    a = random.randint(1, 100)
    print("1〜100の数を当ててください！（チャンスは5回）")

    for i in range(5):
        b = int(input(f"{i+1}回目の予想: "))

        if b == a:
            print("当たり！")
            break
        elif b < a:
            print("もっと大きいです")
        else:
            print("もっと小さいです")

    else:
        print(f"残念！正解は {a} でした")

    c = input("もう一度やりますか？（Yes/No）: ")
    if c.lower() != "yes":
        print("終了です。さようなら")
        break
