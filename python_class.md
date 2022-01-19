class Student:
    def __init__(self): #コンストラクタ（初期化メソッド）もしこれがなかったらprint(a002.name)でエラーが出る。
        self.name = "" #アトリビュート（クラスの中での変数）
    
    def avg(self, math, english): #メソッド
        print((math+english)/2))

a001 = Student() #インスタンス（実態）とクラスの呼び出し（このクラス使うよという宣言）
a001.name = "sato"
print(a001.name)

a002 = Student()
print(a002.name) #空白だけが表示される

"""
https://www.youtube.com/watch?v=F5guF1y7G48
キノコードより
"""
