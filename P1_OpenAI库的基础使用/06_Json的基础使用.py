import json

d = {
    "name": "小明",
    "age": 11,
    "gender": "男"
}

print(str(d))

s = json.dumps(d, ensure_ascii=False)            # 把python数据结构转换为Json字符串
print(s)


l = [
    {
        "name": "小明",
         "age": 11,
        "gender": "男"
    },
    {
        "name": "小明",
        "age": 11,
        "gender": "男"
    },
    {
        "name": "小明",
        "age": 11,
        "gender": "男"
    },
]

print(json.dumps(l, ensure_ascii=False))

json_str = '{"name": "小明", "age": 11, "gender": "男"}'
json_array_str = '[{"name": "小明", "age": 11, "gender": "男"}, {"name": "小明", "age": 11, "gender": "男"}, {"name": "小明", "age": 11, "gender": "男"}]'

res_dict = json.loads(json_str)                  # 把Json字符串转换为python数据结构
print(res_dict, type(res_dict))

res_list = json.loads(json_array_str)
print(res_list, type(res_list))