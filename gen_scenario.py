"""
https://docs.google.com/document/d/1JIYEfG2ZTI6NfGATaiU8_lb_NEhzdRq4IDlNlbcsc2I/edit
"""
import json

"""
b1_いらっしゃいませ、ようこそ養老乃瀧へ.m4a
b2_僕の名前はバックン、よろしくね.m4a
b3_飲み物はそろったかな.m4a
b4_ねえねえ、記念写真を撮らない？.m4a
b5_おっけー！じゃあ上のカメラを見てね。3.2.1.はい、撮れたよー.m4a
b6_撮るならイエスボタン、撮らないならノーボタンを押してね.m4a
b7_シェアする？するならイエスボタン、しないならノーボタンを押してね.m4a
b8_シェアしたよ、僕の一言コメントもチェックしてね.m4a
b9_シェアはしないんだね、わかったよ.m4a
b10_えー？じゃあ、後で撮ろうね.m4a
b11_そろそろ美味しいご飯と一緒に写真を撮ろうよ.m4a
b12_いいね、じゃあ上のカメラを見ておいしそうな顔をして！3.2.1.はい、撮れたよ〜.m4a
b13_まあ、最後に記念撮影っていうのもアリかもね〜.m4a
b14_さあ、みんなで最後に写真を撮ろうよ.m4a
b15_チッ(最後に写真を撮らなかった).m4a
b16_今日は来てくれてありがとう！また遊ぼうね.m4a
b17_それじゃあ、またねー.m4a
b18_ゆっくり楽しんでいってね.m4a
"""

scenario_orig = [
    # 来店時
    {
        "cmd": "texts",
        "data": [
            "いらっしゃいませ〜！",
            "ようこそ養老の滝へ！",
            "僕の名前はバックン！よろしくね！",
            "",
            "飲み物は揃ったかな？",
            "ねえねえ、記念写真を撮らない？撮るならイエスボタン、撮らないならノーボタンを押してね！",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b1.m4a",
    },
    {
        "cmd": "audio",
        "data": "assets/b2.m4a",
    },
    {
        "cmd": "audio",
        "data": "assets/b3.m4a",
    },
    {
        "cmd": "audio",
        "data": "assets/b4.m4a",
    },
    {
        "cmd": "audio",
        "data": "assets/b6.m4a",
    },
    {
        "cmd": "pause",
        "data": "",
    },
    {
        "cmd": "yes-no",
        "data": [1, 14],
    },
    {
        "cmd": "texts",
        "data": [
            "オッケー！じゃあ、上のカメラを見てね。",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b22.m4a",
    },
    {
        "cmd": "photo",
        "data": "",
    },
    {
        "cmd": "audio",
        "data": "assets/b21.m4a",
    },
    {
        "cmd": "texts",
        "data": [
            "はい、撮れたよ〜！",
            "シェアする？するならイエスボタン、しないならノーボタンを押してね！",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b7.m4a",
    },
    {
        "cmd": "pause",
        "data": "",
    },
    {
        "cmd": "yes-no",
        "data": [1, 4],
    },
    {
        "cmd": "tweet",
        "data": "",
    },
    {
        "cmd": "texts",
        "data": [
            "シェアしたよ、僕の一言コメントもチェックしてね",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b8.m4a",
        "next": 5,
    },
    {
        "cmd": "texts",
        "data": [
            "シェアはしないんだね、わかったよ",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b9.m4a",
        "next": 3,
    },

    {
        "cmd": "texts",
        "data": [
            "えー！じゃあ、後で撮ろうね！楽しんで〜！",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b10.m4a",
    },

    {
        "cmd": "texts",
        "data": [
            "ゆっくり楽しんでいってね",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b18.m4a",
    },

    # {
    #     "cmd": "sleep",
    #     "data": 5,
    # },
    {
        "cmd": "pause",
        "data": "",
    },

    # １時間経過
    {
        "cmd": "texts",
        "data": [
            "そろそろ、美味しいご飯と一緒に写真を撮ろうよ！撮るならイエスボタン、撮らないならノーボタンを押してね！",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b11.m4a",
    },
    {
        "cmd": "audio",
        "data": "assets/b6.m4a",
    },
    {
        "cmd": "pause",
        "data": "",
    },
    {
        "cmd": "yes-no",
        "data": [1, 16],
    },
    {
        "cmd": "texts",
        "data": [
            "いいね！じゃあ、上のカメラを見て、美味しそうな顔をして！",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b19.m4a",
    },
    {
        "cmd": "photo",
        "data": "",
    },
    {
        "cmd": "audio",
        "data": "assets/b21.m4a",
    },
    {
        "cmd": "texts",
        "data": [
            "はい、撮れたよ〜！",
            "シェアする？するならイエスボタン、しないならノーボタンを押してね！",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b7.m4a",
    },
    {
        "cmd": "pause",
        "data": "",
    },
    {
        "cmd": "yes-no",
        "data": [1, 4],
    },
    {
        "cmd": "tweet",
        "data": "",
    },
    {
        "cmd": "texts",
        "data": [
            "シェアしたよ、僕の一言コメントもチェックしてね",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b8.m4a",
        "next": 3,
    },
    {
        "cmd": "texts",
        "data": [
            "シェアはしないんだね、わかったよ",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b9.m4a",
    },
    {
        "cmd": "texts",
        "data": [
            "それじゃあ、またねー",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b17.m4a",
        "next": 3,
    },

    {
        "cmd": "texts",
        "data": [
            "最後に記念撮影っていうのもアリかもね。",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b13.m4a",
    },

    # {
    #     "cmd": "sleep",
    #     "data": 5,
    # },
    {
        "cmd": "pause",
        "data": "",
    },

    # ２時間半経過
    {
        "cmd": "texts",
        "data": [
            "さあ！みんなで最後に写真を撮ろうよ！撮るならイエスボタン、撮らないならノーボタンを押してね！",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b14.m4a",
    },
    {
        "cmd": "audio",
        "data": "assets/b6.m4a",
    },
    {
        "cmd": "pause",
        "data": "",
    },
    {
        "cmd": "yes-no",
        "data": [1, 14],
    },
    {
        "cmd": "texts",
        "data": [
            "オッケー！じゃあ、上のカメラを見て、最高の笑顔でね。",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b20.m4a",
    },
    {
        "cmd": "photo",
        "data": "",
    },
    {
        "cmd": "audio",
        "data": "assets/b21.m4a",
    },
    {
        "cmd": "texts",
        "data": [
            "はい、撮れたよ〜！",
            "シェアする？するならイエスボタン、しないならノーボタンを押してね！",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b7.m4a",
    },
    {
        "cmd": "pause",
        "data": "",
    },
    {
        "cmd": "yes-no",
        "data": [1, 4],
    },
    {
        "cmd": "tweet",
        "data": "",
    },
    {
        "cmd": "texts",
        "data": [
            "シェアしたよ、僕の一言コメントもチェックしてね",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b8.m4a",
        "next": 5,
    },
    {
        "cmd": "texts",
        "data": [
            "シェアはしないんだね、わかったよ",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b9.m4a",
        "next": 3,
    },

    {
        "cmd": "texts",
        "data": [
            "・・・！！",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b15.m4a",
    },
    {
        "cmd": "texts",
        "data": [
            "今日は来てくれてありがとう！また遊ぼうね！！",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b16.m4a",
    },

    {
        "cmd": "pause",
        "data": "",
    },
    # {
    #     "cmd": "sleep",
    #     "data": 10,
    # },
]

scenario = [
    # １時間経過
    {
        "cmd": "texts",
        "data": [
            "そろそろ、美味しいご飯と一緒に写真を撮ろうよ！撮るならイエスボタン、撮らないならノーボタンを押してね！",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b11.m4a",
    },
    {
        "cmd": "audio",
        "data": "assets/b6.m4a",
    },
    {
        "cmd": "pause",
        "data": "",
    },
    {
        "cmd": "yes-no",
        "data": [1, 16],
    },
    {
        "cmd": "texts",
        "data": [
            "いいね！じゃあ、上のカメラを見て、美味しそうな顔をして！",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b19.m4a",
    },
    {
        "cmd": "photo",
        "data": "",
    },
    {
        "cmd": "audio",
        "data": "assets/b21.m4a",
    },
    {
        "cmd": "texts",
        "data": [
            "はい、撮れたよ〜！",
            "シェアする？するならイエスボタン、しないならノーボタンを押してね！",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b7.m4a",
    },
    {
        "cmd": "pause",
        "data": "",
    },
    {
        "cmd": "yes-no",
        "data": [1, 4],
    },
    {
        "cmd": "tweet",
        "data": "",
    },
    {
        "cmd": "texts",
        "data": [
            "シェアしたよ、僕の一言コメントもチェックしてね",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b8.m4a",
        "next": 3,
    },
    {
        "cmd": "texts",
        "data": [
            "シェアはしないんだね、わかったよ",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b9.m4a",
    },
    {
        "cmd": "texts",
        "data": [
            "それじゃあ、またねー",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b17.m4a",
        "next": 3,
    },

    {
        "cmd": "texts",
        "data": [
            "最後に記念撮影っていうのもアリかもね。",
        ],
    },
    {
        "cmd": "audio",
        "data": "assets/b13.m4a",
    },

    # {
    #     "cmd": "sleep",
    #     "data": 5,
    # },
    {
        "cmd": "pause",
        "data": "",
    },
]

with open("assets/scenario.json", "wt") as f:
    json.dump(scenario, f, indent=2, ensure_ascii=False)
