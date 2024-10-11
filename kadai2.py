import random

hands={0:"グー",1:"チョキ",2:"パー"}

def winner(a_hand,b_hand):
    # 勝敗の判定
    if a_hand == b_hand:
        return "引き分け"
    elif (a_hand == 0 and b_hand == 1) or (a_hand == 1 and b_hand == 2) or (a_hand == 2 and b_hand == 0):
        return "Aの勝ち"
    else:
        return "Bの勝ち"
    
def janken():
    a_score=0
    b_score=0
    round_num=1
    
    while a_score < 2 and b_score < 2:
        print(f"ラウンド{round_num}:")
        a_hand = random.randint(0, 2)
        b_hand = random.randint(0, 2)
        result = winner(a_hand, b_hand)
        print(f"Aの手: {hands[a_hand]} v.s. Bの手: {hands[b_hand]} → {result}")
        
        if result == "Aの勝ち":
            a_score += 1
        elif result == "Bの勝ち":
            b_score += 1
            
        print(f"現在のスコア: A {a_score} - B {b_score}\n")
        round_num += 1
    
    # print(f"Aの手: {hands[a_hand]} v.s. Bの手: {hands[b_hand]} → {result}")
    if a_score == 2:
        print("最終結果: Aの勝利!")
    else:
        print("最終結果: Bの勝利!")
    
janken()




