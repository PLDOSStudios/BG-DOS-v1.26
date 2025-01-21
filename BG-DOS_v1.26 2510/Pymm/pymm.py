import random
import time
from datetime import datetime
from tkinter import messagebox
import subprocess
import os


def name_error():
    global lines
    print('name_error变量名错误: 在第' + str(lines) +'行, 在变量名开头应为字母而不是数字,并没有特殊符号和中文')


def start():
    global lines
    lines += 1
    c = input('<Pymm-' + str(lines) + '>')
    b.append(c.split())
    if c == 'end':
        run()
    elif c == 'exit':
        return

    if c == 'restart':
        lines = 0
        print('------------------------------------RESTART----------------------------------------------')
        b.clear()
        v.clear()
    start()

def run():
    global b, v, cch, lines
    d = 0
    co= 0
    cch = []
    loop = 0
    ln = 0
    for i in b:
        loop += 1
        if len(i) > 0:
            if i[0] == 'var':
                if len(i) > 1:
                    j = i[1]
                    if len(i) == 3:
                        v.update({j:i[2]})
                else:
                    print('语法错误!!!!')
            elif i[0] == 'pr':
                if len(i) > 1:
                    if i[1] == 'var':
                        if len(i) > 2:
                            if i[2] not in v:
                                print('找不到字符串!!!!!')
                            else:
                                print(v[i[2]])                           
                    else:
                        print(i[1])
                else:
                    print('语法错误!!!!')
            elif i[0] == 'wait':
                if len(i) > 1:
                    n = int(i[1])
                    time.sleep(n)
                    if len(i) > 2:
                        print('语法错误!!!!!!!!!!')
                else:
                    print('语法错误!!!!!!!!!!')
            elif i[0] == 'stint':
                if len(i) == 2:
                    try:
                        i[1] = int(i[1])
                        print(i[1])
                    except ValueError:
                        messagebox.showerror('Error', '不能把字符串转为数字!!!')
                    else:
                        i[1] = str(i[1])
                        print(i[1])
                elif len(i) == 3:
                    try:
                         v[i] = int(i[2])                        
                    except ValueError:
                        messagebox.showerror('Error', '不能把字符串转为数字!!!')
                    else:
                        v[i] = str(i[2])     
                else:
                    print('语法错误!!!!!!!!!!')
            elif i[0] == 'loop':
                if len(i) > 2:
                    try:
                        i[1] = int(i[1])
                        ln = i[1]
                    except ValueError:
                        messagebox.showerror('Error', '不能输入字符串!!!')
                    else:
                        for ff in range(ln):
                            b.insert(loop, i[2:])               
                else:
                    print('语法错误!!!!!!!!!!')
            elif i[0] == 'en':
                if len(i) > 3:
                    if i[1] == 'var':
                        abc = input()
                        v.update({i[2]:abc})
                        print(i[3])
                else:
                    print('语法错误!!!!!!!!!!')
            elif i[0] == 'prtime':
                print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            elif i[0] == 'r':
                if len(i) > 3:
                    if i[1] == 'num':
                        try:
                            ba = int(i[2])
                            bb = int(i[3])
                        except ValueError:
                            messagebox.showerror('Error', '不能输入字符串!!!')
                        else:
                            bbc = random.randint(ba, bb)
                            v.update({i[4]:bbc})
                    elif i[1] == 'ch':
                        try:
                            cha = random.choice(v[i[2]])
                            v.update({i[3]:cha})
                        except:
                            print('语法错误!!!!!!!!!!')
                else:
                    print('语法错误!!!!!!!!!!')
            elif i[0] == 'cr':
                if len(i) > 2:
                    if i[1] == 'list':
                        try:
                            v.update({i[2]:[]})
                        except:
                            print('语法错误!!!!!!!!!!')
                        else:
                            for dddd in i[3:]:
                                v[i[2]].append(dddd)
                else:
                    print('语法错误!!!!!!!!!!')
            elif i[0] == 'add':
                if len(i) > 2:
                    try:
                        v[i[1]].append(i[2])
                    except NameError:
                        print('找不到列表!!!')
            elif i[0] == 'del':
                if len(i) > 2:
                    try:
                        numi = int(i[2])
                        v[i[1]].pop(numi-1)
                    except NameError:
                        print('找不到列表!!!')
                    except ValueError:
                        print('不能输入字符串!!!')
                else:
                    print('语法错误!!!!!!!!!!')

            elif i[0] == 'timer':
                if len(i) > 2:
                    if i[2] == 'pr':
                        try:
                            aaaaaa = int(i[1])
                            timera = 0
                            for iiiiiiii in range(aaaaaa):
                                print(timera)
                                timera += 0.1
                                time.sleep(0.1)
                        except ValueError:
                            print('不能输入字符串!!!')
                    else:
                        print('语法错误!!!!!!!!!!')
                else:
                    print('语法错误!!!!!!!!!!')
            elif i[0] == 'sort':
                if len(i) > 2:
                    if i[1] in v:
                        if i[2] == '<':
                            try:
                                v[i[1]].sort()
                            except AttributeError:
                                print('这个玩意儿不是列表!!!排不了序!!!')
                        elif i[2] == '>':
                            try:
                                v[i[1]].sort(reverse=True)
                            except AttributeError:
                                print('这个玩意儿不是列表!!!排不了序!!!')
            elif i[0] == 'max':
                if len(i) > 2:
                    try:
                        qqqq = max(v[i[1]])
                        v[i[2]] = qqqq
                    except:
                        print('语法错误!!!!!!!!!!')
            elif i[0] == 'min':
                if len(i) > 2:
                    try:
                        pppp = min(v[i[1]])
                        v[i[2]] = pppp
                    except:
                        print('语法错误!!!!!!!!!!')
            elif i[0] == 'clear':
                if len(i) > 1:
                    try:
                        v[i[1]] = []
                    except:
                        print('语法错误!!!!!!!!!!')
                else:
                    print('语法错误!!!!!!!!!!')
            elif i[0] == 'vege':
                print('菜, 就多练')
                time.sleep(1.6)
                print('输不起, 就别玩儿')
                time.sleep(2.5)
                print('以前是以前, 现在是现在')
                time.sleep(3)
                print('你要是一直拿以前当作现在')
                time.sleep(2.5)
                print('哥们儿, 你怎么不拿你刚出生的时候对比啊?')
                time.sleep(3)
            elif i[0] == 'prbur':
                if len(i) == 4:
                    if i[2] == '=':
                        try: 
                            if i[1] == i[3]:
                                print(1)
                            else:
                                print(0)
                        except:
                            print(2)
                    elif i[2] == '<':
                        try:
                            aab = int(i[1])
                            aaab = int(i[3])
                            if i[1] < i[3]:
                                print(1)
                            else:
                                print(0)
                        except:
                            print(2)
                    elif i[2] == '>':
                        try:
                            ccb = int(i[1])
                            cccb = int(i[3])
                            if i[1] > i[3]:
                                print(1)
                            else:
                                print(0)
                        except:
                            print(2)
                else:
                    print('语法错误!!!!!!!!!!')
            elif i[0] == 'prline':
                if len(i) > 1:
                    try:
                        for i in i[1]:
                            print(i, end='')
                            if i == '/':
                                print()
                            time.sleep(0.1)
                        print()
                    except:
                        print(222222)
                else:
                    print('语法错误!!!!!!!!!!')
            elif i[0] == 'msg':
                try:
                    if i[3] == 'i':
                        messagebox.showinfo(i[1], i[2])
                    elif i[3] == '!':
                        messagebox.showwarning(i[1], i[2])
                    elif i[3] == 'x':
                        messagebox.showerror(i[1], i[2])
                    else:
                        print('找不到这个符号!!!')
                except:
                    print(222222)

            elif i[0] == 'open':
                if len(i) < 2:
                    print('你mb的,不输入玩意儿让我咋打开???')
                else:
                    if i[1] == 'whiteboard':
                        try:
                            subprocess.Popen(['Python', r'Pymm\App\Whiteboard.py'])
                        except Exception as e:
                            print('运行时出错')
        else:
            print('找不到这个函数!!!!!!!!!!')
            
                                                              
    print('运行结束啦!')
    lines = 0
        
lines = 0
b = []
cch = []
v = {}
num = ['0',  '1', '2', '3', '4', '5', '6', '7', '8', '9']
num1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
name = ['pr', 'int', 'if', 'else', 'endif', 'end', 'var', 'en', 'ok', 'help', 'start']
print('正在启动编译器……')
time.sleep(1)
print('PY - - 1.6 2024/9/24')
while True:
    current_path = os.getcwd()
    a = input('Pymm-Shell>')
    if a == 'start':
        start()
        break
    elif a[0] == 'math':
        try:
            if a[1] == 'binary' and a[2] == '2' and a[3] == '10':
                ans = int(a[4], 2)
                print(f'换算结果:{ans}')

            if a[1] == 'pow':
                ans = pow(int(a[2]), int(a[3]))
                print(f'换算结果:{ans}')
        except:
            print('运算错误!')
    elif a == 'exit':
        break
    elif a == 'help':
        with open(current_path + "\\Disks\\A\\BG_SYSTEM\\BIN\\指令说明.txt", "r", encoding="utf-8") as menu:
            for text in menu.readlines():
                print(text, end='')
            print()
    else:
        try:
            result = eval(a)
            print(f"{a} = {result}")
        except Exception as e:
            print(f"Error: {e}")
