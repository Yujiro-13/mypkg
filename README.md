# mypkg
本パッケージは、千葉工業大学 未来ロボティクス学科 ロボットシステム学の講義内で作成した、ROS 2パッケージです。

## テスト結果
[![test](https://github.com/Yujiro-13/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Yujiro-13/mypkg/actions/workflows/test.yml)

## 動作確認済み環境
以下の環境、ソフトウェアにおいてプログラムの実行及びテストを確認しています。
- OS: Ubuntu22.04 LTS
- ROS 2: Humble

### ブランチ内容
このブランチでは、講義第9回を除く、第11回までの内容を含むパッケージを使用しています。

### トピック内容
本パッケージでは、16ビット符号付き整数のメッセージ型を持つトピック/countupを扱います。

### ノードの使用方法
- talker.py

0.5秒毎にカウントした数字を、トピック/countupを通じて送信するノードです。

以下のコマンドで起動します。
```
$ ros2 run mypkg talker #何も表示されない
```

- listener.py

トピック/countupを受信して端末に表示するノードです。

talker.pyを起動した端末と別端末を開き、以下のコマンドで起動します。
```
$ ros2 run mypkg listener
[INFO] [1703314540.253223410] [listener]: Listen: 0
[INFO] [1703314540.732753899] [listener]: Listen: 1
[INFO] [1703314541.231645432] [listener]: Listen: 2
・・・
```

- talk_listen.launch.py
talker.py、listener.pyを同じ端末で起動するためのノードです。

以下のコマンドで起動します。 
```
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [29541]
[INFO] [listener-2]: process started with pid [29543]
[listener-2] [INFO] [1703835315.633143352] [listener]: Listen: 0
[listener-2] [INFO] [1703835316.124830784] [listener]: Listen: 1
[listener-2] [INFO] [1703835316.624943984] [listener]: Listen: 2
```

## 著作権・ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2023 Yujiro Shito
