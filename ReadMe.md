# このソフトウェアについて

ゲーム状態とその変更のフレームワークを仮実装してみた。

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [pyenv](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md) 1.0.10
    * Python 3.6.1
        * [PyGame](http://ytyaru.hatenablog.com/entry/2018/06/11/000000) 1.9.3
        * [PyGame Utilities(pgu)](http://ytyaru.hatenablog.com/entry/2018/06/19/000000) 0.18
        * [PyOpenGL](http://ytyaru.hatenablog.com/entry/2018/06/15/000000) 3.1.0
        * PyOpenGL_accelerate 3.1.0
        * PyOpenGL_Demo 3.0.0
        * [Pillow](https://pillow.readthedocs.io/en/4.2.x/) 4.2.1
        * [NumPy](http://www.numpy.org/) 1.13.1

# 実行

```sh
cd 4/
$ python Main.py
```

Enter, Space, Zキーのいずれかでゲーム状態が変化する。各ゲーム状態ごとに画面の色が変わる。ESCキーまたはAlt+F4で終了する。

# 概要

あみだくじゲームをつくる場合、以下の3つの状態がある。

状態|ユーザ入力|表示
----|----------|----
選択|左右キーであみだ選択|カーソル表示
アニメ|なし|選択した線からゴールまでのアニメーション表示
結果|SPACEキーで"選択"へ戻る|選択した線の結果表示

各状態は、ユーザ入力や表示の内容が異なる。それぞれ別クラスで実装したい。そのための枠組みを考えた。デザインパターンでいうStateパターンを使ったつもり。

実際の処理は実装していない。単に画面を塗りつぶすだけ。各状態ごとに赤、緑、青になる。

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[pygame](http://www.pygame.org/)|[LGPL](https://www.pygame.org/docs/)|[pygame](http://www.pygame.org/)

