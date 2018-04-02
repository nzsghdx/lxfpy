# 文件名不能与要导入的包名相同,不然就报错了
import json
d=dict(name='Bob',age=20,score=80)
print(d)
print(json.dumps(d))
