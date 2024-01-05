# mypkg
本パッケージは、千葉工業大学 未来ロボティクス学科 ロボットシステム学の講義内で作成した、ROS 2パッケージです。

## テスト結果
[![test](https://github.com/Yujiro-13/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Yujiro-13/mypkg/actions/workflows/test.yml)

## 動作確認済み環境
以下の環境、ソフトウェアにおいてプログラムの実行及びテストを確認しています。
- OS: Ubuntu22.04 LTS
- ROS 2: Humble

## トピック内容
本パッケージでは、64ビット符号付き整数のメッセージ型を持つトピック/unix_timeを扱います。

## ノードの使用方法
- pub_unix_time.py

1秒毎のUnix時間を、トピック/unix_timeを通じて送信するノードです。

以下のコマンドで起動します。
```
$ ros2 run mypkg pub_unix_time.py #何も表示されない
```

- sub_unix_time.py

トピック/unix_timeを受信して、Unix時間と、それを日時に変換した内容を端末に表示するノードです。

pub_unix_time.pyを起動した端末と別端末を開き、以下のコマンドで起動します。
```
$ ros2 run mypkg sub_unix_time.py
[INFO] [1703979324.976998715] [sub_unix_time]: Unix time: 1703979324, Date time: 2023-12-31 08:35:24+09:00
[INFO] [1703979325.959554845] [sub_unix_time]: Unix time: 1703979325, Date time: 2023-12-31 08:35:25+09:00
[INFO] [1703979326.959363177] [sub_unix_time]: Unix time: 1703979326, Date time: 2023-12-31 08:35:26+09:00
・・・
```

- datetime.launch.py
pub_unix_time.py, sub_unix_time.pyを同じ端末で起動するためのノードです。

以下のコマンドで起動します。 
```
$ ros2 launch mypkg datetime.launch.py
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [sub_unix_time-1]: process started with pid [19725]
[INFO] [pub_unix_time-2]: process started with pid [19727]
[sub_unix_time-1] [INFO] [1703979387.984456956] [sub_unix_time]: Unix time: 1703979387, Date time: 2023-12-31 08:36:27+09:00
[sub_unix_time-1] [INFO] [1703979388.742199070] [sub_unix_time]: Unix time: 1703979388, Date time: 2023-12-31 08:36:28+09:00
[sub_unix_time-1] [INFO] [1703979388.958912025] [sub_unix_time]: Unix time: 1703979388, Date time: 2023-12-31 08:36:28+09:00
```

## 著作権・ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2023 Yujiro Shito
