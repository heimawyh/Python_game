# 知识点
# 1.列表填充内容
a = [i*2 for i in range(0,1)]
print(a)
# 2.字符串转化为列表
def inputNum():
    big_list = []
    my_str = input("请输入数字序号")
    my_list = []
    for i in my_str[1:]:
        my_list.append(int(i))
    for i in range(0,len(my_list),3):
        big_list.append(my_list[i:i+3])
    return  big_list
print(inputNum())