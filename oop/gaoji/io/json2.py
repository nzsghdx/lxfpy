import json
# json_str不是一个dict啊,报错说是dict,很迷
# 还是看得不够仔细,原来等号后面还有单引号..
json_str='{"score": 80, "name": "Bob", "age": 20}'
print(json_str)
print(json.loads(json_str))
