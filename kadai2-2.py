import random

# 手を表す辞書
hands = {0: "グー", 1: "チョキ", 2: "パー"}

# 勝敗の判定を行う関数（複数人対応）
def winner(player_hands):
    unique_hands = set(player_hands.values())
    
    # 引き分けの判定（全員が同じ手、または3種類の手が全て存在する場合）
    if len(unique_hands) == 1 or len(unique_hands) == 3:
        return "引き分け"
    
    # 勝利手を決定（グー > チョキ > パー > グー）
    if 0 in unique_hands and 1 in unique_hands:  # グーがチョキに勝つ
        winning_hand = 0
    elif 1 in unique_hands and 2 in unique_hands:  # チョキがパーに勝つ
        winning_hand = 1
    else:  # パーがグーに勝つ
        winning_hand = 2

    # 勝つ手を出したプレイヤーをリストに追加
    winners = [player for player, hand in player_hands.items() if hand == winning_hand]
    
    return f"{', '.join(winners)}の勝ち"

# 任意の人数でじゃんけんを行う関数
def janken(num_players=3):
    player_hands = {}
    
    # 各プレイヤーの手をランダムに決定
    for i in range(1, num_players + 1):
        player_hands[f"プレイヤー{i}"] = random.randint(0, 2)
    
    # 各プレイヤーの手を表示
    hands_display = [f"{player}: {hands[hand]}" for player, hand in player_hands.items()]
    print(" v.s. ".join(hands_display))
    
    # 勝者の判定
    result = winner(player_hands)
    
    # 結果の表示
    print(f"結果 → {result}")

# 実行
janken(5)  # 例えば5人でじゃんけんを行う場合