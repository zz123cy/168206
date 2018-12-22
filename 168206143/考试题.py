print("A：我没有偷钻石。")
print("B：D就是罪犯。")
print("C：B是盗窃这块钻石的罪犯。")
print("D：B有意诬陷我。")

for Crime in ['A','B','C','D']:
    if(1==(Crime!='A')+(Crime=='D')+(Crime=='B')+(Crime!='D')):
        print("罪犯是：",Crime)
