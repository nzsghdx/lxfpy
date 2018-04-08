## XML

>比json复杂,而且用的也越来越少了,大佬说有必要了解一下.

操作xml有两种方法:dom和sax.
1.dom会把整个xml读入内存,解析为树,缺点是占用内存大,解析慢,优点是可以任意遍历树的节点.
2.sax是流模式,边读边解析,占用内存小,解析快,缺点是我们需要自己处理事件.

python中使用sax解析xml通常关心的事件是start_emement,end_element,char_data.

>每天不git push一下浑身难受,嗯,哪怕之为了push更新了一句话,然而现在已经00:00了,sad.
