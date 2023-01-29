# coding: utf-8
# @Author: 4C69
# @Time: 2023/1/29 18:01


"""
用户视图层
"""

# 0、退出
def sign_out():
    print('退出功能')


# 1、注册功能
def register():
    print('注册功能')


# 2、登录功能
def login():
    print('登录功能')


# 3、充值功能
def recharge():
    print('充值功能')


# 4、转账功能
def transfer():
    print('转账功能')


# 5、提现功能
def widthdraw():
    print('提现功能')


# 6、查看余额
def check_balance():
    print('查看余额')


# 7、查看流水
def check_flow():
    print('查看流水')


# 8、购物功能
def shopping():
    print('购物功能')


# 9、查看购物车
def check_shopping_cart():
    print('查看购物车')


# 10、退出账号
def login_out():
    print('退出账号')


# 11、管理员功能
def admin():
    print('管理员功能')


#函数字典
func_dic = {
    '0': ('退出', sign_out),
    '1': ('注册功能', register),
    '2': ('登录功能', login_out),
    '3': ('充值功能', recharge),
    '4': ('转账功能', transfer),
    '5': ('提现功能', widthdraw),
    '6': ('查看余额功能', check_balance),
    '7': ('查看流水', check_flow),
    '8': ('购物功能', shopping),
    '9': ('查看购物车', check_shopping_cart()),
    '10': ('账号功能', login_out),
    '11': ('管理员功能', admin),
}



#主程序
def main():
    while True:
        print('购物管理系统'.center(20,'='))
        for num in func_dic:
            print(f'{num} {func_dic.get(num)[0]}'.center(20,' '))
        print('我是有底线的'.center(20, '='))
        opt = input('请输入功能编号:').strip()
        if opt not in func_dic:
            print('此功能不存在！')
            continue
        func_dic.get(opt)[1]()