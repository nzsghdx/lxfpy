# 使用with语句,不用手动的关闭:f.close()
with open('./test.txt','r') as f:
#    print(f.readline())
#    print(f.readline())
#    print(f.readline())
#    print(f.readlines())
#    print(f.read())

    # 这里和read方法是同样的效果,把末尾的'\n'删掉
    for line in f.readlines():
        print(line.strip())
