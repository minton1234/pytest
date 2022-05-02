# テスト容易性: 高い　重要度: 高い
# 1~100の数字をプリントし、3の倍数の時はFiz、5の倍数の時はBaz、15の倍数の時はFizBazを表示

# []数を文字列に変換する
# []1を渡すと文字列1を返す -> 仮実装
# []2を渡すと文字列2を返す -> 三角測量

# []3の倍数の時は数の代わりにFizに変換する
# []5の倍数の時は数の代わりにBazに変換する　->明白な実装

# テスト容易性: 低い 重要度: 低い

class Fizbaz(object):
    def __init__(self) -> None:
        pass


    def convert(db, num) -> int:
        
        if num % 3 ==0:
            return "Fiz"

        elif num % 5 ==0:
            return "baz"

        else:
            num=str(num)
            return num
