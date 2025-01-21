while 1:
    print('BG-DOS 提示')
    print('[0] 退出')
    print('[1] 注册用户')
    a = input()
    if a == '1':
        print('注册用户您只需要在登录时输入114514即可')
        print('然后输入用户名和密码')
        print('您可以选择不设置密码,输入None即可,但需要注意大小写')
        print('等待OOBE完成后,即可开机时找到')
    if a == '0':
        break