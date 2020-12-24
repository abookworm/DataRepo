# coding: utf-8
import sys
import os
import re

def main():

    # 获取当前路径名称
    file_path = sys.path[0]
    # print(file_path)

    # 输出文件名
    file = "E:/aGitbook/filelist.txt"

    with open(file, 'a') as f:
        f.write(file_path)
        f.write("\n")

    # 遍历当前路径下的文件
    for filenames in os.listdir(file_path):
        if(re.match(r'.*\.md$', filenames)):
            # 获取名称
            file_name = re.match(r'(.*)\.md$', filenames).group(1)
            # 拼接字符串
            file_list = "* [%s](./%s)" % (file_name, filenames)

            with open(file, 'a') as f:
                f.write(file_list)
                f.write("\n")


if __name__ == "__main__":
    main()
    print("Well Done!")
