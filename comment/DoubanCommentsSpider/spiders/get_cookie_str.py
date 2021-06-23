# coding:utf-8

# 功能：cookie string ==> python dict
# 用法：把从网站中复制的cookie字符串替换到main函数中,即可得到对应的字典字符串
# 注意：这是个独立的脚本，直接运行就OK了
# 本来想用cookie模拟登陆的,没成功，脚本就先留着吧

def string_to_dict(cookie):
    item_dict = {}
    items = cookie.split(';')
    for item in items:
        try:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            item_dict[key] = value
        except (IndexError, UnboundLocalError):
            print("\nplease input a correct cookie string!")
            exit()
    return item_dict


if __name__ == "__main__":
    console_in = input("please input cookie string:\n")
    console_out = string_to_dict(console_in)
    print("your python dict:\n", console_out)
