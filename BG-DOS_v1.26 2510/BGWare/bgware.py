import system

print('欢迎使用BG-DOS虚拟机')
def new():
    print('新建虚拟机向导')
    print('请选择你要创建的虚拟机范围')
    print('[1] BG-DOS 1.0 ~ BG-DOS 1.1')
    print('[2] BG-DOS 1.2 ~ BG-DOS 1.13 或 PL-DOS 1.0.x')
    print('[3] BG-DOS 1.14 ~ BG-DOS 1.20 Build 1710')
    print('[4] BG-DOS 1.20 Build 1801 ~ BG-DOS 1.2x 或 PL-DOS 1.1 ~ 1.x')
    b = input()
    if b == '1' or b == '2' or b == '3':
        print('请选择系统位置(或创建空的系统)')
        print('[1] 安装系统')
        print('[2] 创建空的系统')
        c = input()
        if c == '2':
            print('即将启动系统')
            system.run_sys(None, None)
        if c == '1':
            print('请输入系统路径')
            d = input()
            print('请输入虚拟机名称')
            e = input()
            system.run_sys(d, e)

while True:
    print('[1] 新建虚拟机')
    print('[2] 打开虚拟机')
    print('[3] 退出')
    a = input()
    if a == '1':
        new()