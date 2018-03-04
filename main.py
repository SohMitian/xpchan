import twicon as tc

xpchan = tc.twicon() # インスタンス生成
serch_list = xpchan.serch() # エゴサ結果をjsonで返す
xpchan.rt(serch_list) # エゴサjsonからNGワード以外をRT