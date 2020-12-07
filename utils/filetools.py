

def write_file(file_path, content):
    """
        方法：写入文件
        参数：
            - file_path:要写入的文件路径
            - content：要写入的内容
    """
    with open(file_path, 'w') as f:
        f.write(content)


def read_file(file_path):
    """
        方法：读取文件
        参数：
            - file_path:要写入的文件路径
    """
    with open(file_path,'r',encoding='utf-8') as f:
        t = f.readlines()
        new_file=[]
        for line in t:
            a=line.strip()
            new_file.append(a)

    return new_file

# 写入demo
# a = "这是测试的token"
# write_file('token.txt', a)

# 读取demo
# res = read_file('token.txt')
# print(res)