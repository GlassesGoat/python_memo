from datetime import datetime
today = datetime.now().strftime("%Y年%m月%d日")
test = "おはようございます。今日は{}です。".format(today)
print(test)

"""
Pythonの文字列フォーマット　format()メソッドの使い方
https://gammasoft.jp/blog/python-string-format/
"""
