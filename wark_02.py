import random
import time

best_time = None  # 最高記録用変数

while True:
    print("反応速度の測定をします。")
    print("【！！！！！】が出たら、できるだけ早くEnterキーを押してください。")
    print("準備ができたらEnterキーを押してください。")
    input()

    atime = random.uniform(5, 15)
    print("合図が出るまで待ってください...")
    time.sleep(atime)

    print("【！！！！！】")
    start_time = time.time()
    input()
    end_time = time.time()

    btime = end_time - start_time  # 反応時間

    if btime < 0.01:
        print("不正です！早すぎます。やり直してください。")
    else:
        print(f"あなたの反応時間は {btime:.4f} 秒です。")

        # 最高記録の更新チェック
        if best_time is None or btime < best_time:
            best_time = btime

    # 再チャレンジ確認
    retry = input("もう一度やりますか？（Yes または No）：")
    if retry.lower() != "yes":
        break
    else:
        continue

# 終了処理
if best_time is not None:
    print(f"これまでの最高記録は {best_time:.4f} 秒でした。")
print("さようなら！")
