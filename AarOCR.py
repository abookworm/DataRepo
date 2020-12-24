# coding=utf-8

import sys
import json
import base64
import re
import os

# 导入Python3 模块
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.parse import quote_plus


# 防止https证书校验不正确
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Python3 应用标识
IS_PY3 = sys.version_info.major == 3

# Baidu AI 
API_KEY = 'fUr6iukVECdKe4llMB4KvTN1'

SECRET_KEY = 'TxtW3oNqG765lRGGtuoAcXZnVUWVrPCM'

OCR_URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"

"""  TOKEN start """
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'


def fetch_token():
    """
    Function: 获取 Token
    return: None
    """
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print(err)
    if (IS_PY3):
        result_str = result_str.decode()

    result = json.loads(result_str)

    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not 'brain_all_scope' in result['scope'].split(' '):
            print ('please ensure has check the  ability')
            exit()
        return result['access_token']
    else:
        print ('please overwrite the correct API_KEY and SECRET_KEY')
        exit()


def fetch_filelist():
    """
    Function: 获取当前路径文件列表
    return: fileslist
    """


def read_file(image_path):
    """
    Function: 读取文件
    return: 文件流
    """
    # f = None
    # try:
    #     f = open(image_path, 'rb')
    #     return f.read()
    # except:
    #     print('read image file fail')
    #     return None
    # finally:
    #     if f:
    #         f.close()
    with open(image_path, "rb") as f:
        return f.read()


# 调用远程服务
def request(url, data):
    """"
    Function: 调用远程服务
    return: None
    """
    req = Request(url, data.encode('utf-8'))
    # has_error = False
    try:
        f = urlopen(req)
        result_str = f.read()
        if (IS_PY3):
            result_str = result_str.decode()
        return result_str
    except URLError as err:
        print(err)


def save_file(filename, text):
    """
    Function: 保存文件识别内容到文档
    @Parm filename: 识别文件名称 
    @Parm text: 识别内容
    return: None    
    """
    # 获取程序文件目录
    filepath = sys.path[0]

    # 构建文件
    file = "%s/file_content.txt" % filepath

    # 写入文件
    with open(file, "a") as f:
        f.write(filename)
        f.write("\n")
        f.write(text)
        f.write("\n" * 2)

    print("Well Done!")


def OCR(image_file):
    """
    Function: 图像识别
    """
    # 获取access token
    token = fetch_token()

    # 拼接通用文字识别高精度url
    image_url = OCR_URL + "?access_token=" + token
    # print("image_url: ", image_url)

    # 读取图片
    file_content = read_file(image_file)
    # print("file_content: ", file_content)

    # 调用文字识别服务
    result = request(image_url, urlencode({'image': base64.b64encode(file_content)}))

    # 解析返回结果
    text = ""
    result_json = json.loads(result)
    for words_result in result_json["words_result"]:
        text = text + words_result["words"]

    # 打印文字
    print(text)

    # 保存文本
    save_file(image_file, text)


def main():
    """
    Function: 主函数
    Return: None
    """
    # 获取当前文件路径
    filepath = sys.path[0]

    for filename in os.listdir(filepath):
        # print(filename)
        # 匹配图片文件
        if(re.match(r'.*.[png, jpg]$', filename)):
            print(filename)

            # 构建完整路径
            image_file = "%s/%s" % (filepath, filename)
            # print(image_file)

            # 识别图片文本
            OCR(image_file)
        else:
            print("文件 %s 不符合识别格式" % filename)


if __name__ == '__main__':
    main()