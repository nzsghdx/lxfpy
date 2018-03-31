# Delete empty 

#strip用于移除指定的字符,默认为空格
#所以这里默认移除头尾的空格
def not_empty(s):
    #返回没有空格的字符(即空的字符)
    return s and s.strip()

L=list(filter(not_empty,['A','','B',None,' ']))

print(L)
