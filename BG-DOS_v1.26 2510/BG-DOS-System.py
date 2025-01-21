import random
import time, os
import cmd
from datetime import datetime
import webbrowser
try:
    import signal
    import psutil
    import subprocess
except ModuleNotFoundError:
    os.system("pip install signal")
    os.system("pip install psutil")
    os.system('pip install subprocess')
    import signal

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[36m'
RESET = '\033[0m'
WHITE = '\033[0m'
PURPLE_RED = '\033[35m'
ORANGE = '\033[38;2;255;165;0m'
BLUE = '\033[34m'
now = datetime.now()
year = now.year
month = now.month
day = now.day
current_path = os.getcwd()
directory = 'Users'
user_name = ''
class BGDOS(cmd.Cmd):
    os.system('cls')

    print('Welcome to BG-DOS')
    print('欢迎来到BG-DOS')

    import platform

    if platform.system() == 'Linux':
        print('马勒戈壁的,抄昵马，敢用Linux打开我们的程序,你个帅比跟勾一样，用Linux让你飞起来！\n沙比，滚出去！小臂在子')
        time.sleep(2)
        quit()
    elif platform.system() == 'Mac':
        print('你是Mac用户赶紧给我滚去BG-DOS 1.4的Mac专用版, 不然杀了你!')
    else:
        print('反Linux检测已通过!')

    with open(r'System/DataFiles/user.txt', 'r') as f:
        e = f.read()
        if e == '0':
            print('你还没有注册')
            subprocess.call(['python', 'BG-DOS-OOBE.py'])
    entries = os.listdir(directory)
    folders = [entry for entry in entries if os.path.isdir(os.path.join(directory, entry))]

    foo = 1
    for fo in folders:
        print(f"[{foo}] {fo}")
        foo += 1
    print('[114514] 注册账户')

    print('请选择要登录的用户')
    fooo = input()
    try:
        fooo = int(fooo)
        try:
            user_name = folders[fooo - 1]
        except:
            if fooo != 114514:
                print('你输入的不正确!!!!')
                quit()
            else:
                subprocess.call(['python', 'BG-DOS-OOBE.py'])
        else:
            if fooo <= foo:
                with open(f'Users/{folders[fooo - 1]}/autologin.txt', 'r', encoding='utf-8') as f:
                    ff = f.read()
                    if ff == '0':
                        with open(f'Users/{folders[fooo - 1]}/password.txt', 'r', encoding='utf-8') as f:
                            passsword = f.read()
                        if passsword != 'None':
                            print('请输入密码')
                            passs = input()
                            if passs != passsword:
                                print('密码错误!')
                                print('即将退出!')
                                time.sleep(2)
                                quit()
                            else:
                                print('密码正确!')
                        else:
                            print('没有密码，登录成功')
                    else:
                        print('自动登录成功!')

    except TypeError:
        print(f'{RED}[Error 18]{RESET} 你输入的不是数字!')

    print('THE WOCAO-114514-1919810 PERSONAL COMPUTER BG-DOS VERSION 1.25')

    with open('System/Temp/now_user.txt', 'w') as f:
        f.write(user_name)

    words = ['输入help可以查看所有命令哦', '其实BG-DOS以前不长这样,现在重构了',
             '你觉得我们自己开发的BG-DOS系统值多少钱?\n1块钱?5块钱?70块钱?80块钱甚至更多!\n不它现在是免费的它现在是免费的!\n你甚至可以用它来玩扫雷,下井字棋,以及各种奇奇怪怪的小游戏\n快来下载!!!',
             '内存不是储存空间,它们两个是完全不一样的东西!', 'CanDOS的解散日期正好是BG-DOS的创立日期!',
             'BG-DOS是在2024/8/17 19时创立的哦', 'BG-DOS的全称是Beginning Disk Operating System',]
    if month == 12 and day >= 9 and day <=20:
        print(f'{RED}<勿忘国耻!>{RESET} 1937年12月13日, 发生了南京大屠杀!')
    print(f'{CYAN}<你知道吗>{RESET} {random.choice(words)}')
    print(f'{CYAN}<提示>{RESET} 输入help可以查看所有命令哦')

    blacklist = ['miniworld.exe', 'mimiworld.exe', 'mimiworld - 副本.exe']
    root_dir = 'C:/'
    prompt = f'BG-DOS{ORANGE}@{user_name}{RESET}>'
    input_cmd = ''
    #下方do_xxx 检测输入xxx时自动执行无需调用
    def do_help(self, arg):
         with open('System/help.txt','r', encoding = 'utf-8') as f:
             for line in f:
                 print(line, end = '')
         print()

    def do_about(self, arg):
        print('BG-DOS 1.25')
        print('我们的开发成员:')
        print('B站/QQ名:')
        print('BG-DOS工作室')
        print('[BG-DOS管理员] 东风Cherrier账号')
        print('[随机管理员] yzklpy')
        print('[PL-DOS管理员] ls21')
        print('QQ群:1005109089')

    def do_musicmaker(self, arg):
        with open("App/BGMusicMaker/music.py", "rb") as file:
            minesweeper = file.read().decode('utf-8')
        exec(minesweeper)

    def do_minesweeper(self, arg):
        with open("App/minesweeper.py", "rb") as file:
            minesweeper = file.read().decode('utf-8')
        exec(minesweeper)

    def do_exit(self, arg):
        exit()

    def do_cls(self, arg):
        os.system('cls')

    def do_users(self, arg):
            directory = 'Users'
            entries = os.listdir(directory)
            folders = [entry for entry in entries if os.path.isdir(os.path.join(directory, entry))]
            print()
            print('   用户名          权限')
            print('+---------------------------------------')
            for i in folders:
                if i == '114514':
                    print(f'|  114514          开发者')
                elif i == 'Guest':
                    print(f'|  Guest           访客')
                else:
                    print(f'|  {i}{(8-len(i))*' '}        管理员')
            print()
            print('           访客  管理员  开发者')
            print('系统文件操作  X     X      √')
            print('管理磁盘用户  X     √      √')
            print('进入硬核系统  X     √      √')
            print('创建文件      √     √      √')

    def do_dir(self, arg):
        def list_files_and_sizes(directory):
            items = os.listdir(directory)
            print('File Name     |     Bytes')
            for item in items:
                item_path = os.path.join(directory, item)

                if os.path.isdir(item_path):
                    pass
                elif os.path.isfile(item_path):
                    size = os.path.getsize(item_path)
                    print(f"{item_path}    {size}")
        current_directory = "."
        list_files_and_sizes(current_directory)
    def do_finddir(self, arg):
        try:
            def li(directory):
                items = os.listdir(directory)
                print('File Name     |     Bytes')

                for item in items:
                    item_path = os.path.join(directory, item)
                    if os.path.isdir(item_path):
                        pass
                    elif os.path.isfile(item_path):
                        size = os.path.getsize(item_path)
                        print(f"{item_path}    {size}")
        except:
            print('错误！肯定是你的问题！')
        dirr = input('输入要扫描的目录')
        current_directory = dirr
        li(current_directory)

    def do_bgware(self, arg):
        subprocess.call(['python', 'BGWare/bgware.py'])

    def do_tictactoe(self, arg):
        print('你要运行哪一个\n[1] 新版井字棋\n[2] 第二版井字棋\n[3] 老六版井字棋')
        eeq = input()
        if eeq == '1':
            subprocess.call(['python', 'App/TICTACTOE.PY'])
        elif eeq == '2':
            subprocess.call(['python', 'App/TICTACTOE2.PY'])
        elif eeq == '3':
            subprocess.call(['python', 'App/TICTACTOEOLD.PY'])

    def do_card(self, arg):
        subprocess.call(['python', 'App/CARD.PY'])

    def do_pymm(self, arg):
        subprocess.call(['python', 'Pymm/pymm.py'])

    def do_notepad(self, arg):
        subprocess.call(['python', 'App/Notepad.py'])

    def do_allscan(self, arg):
        print('BG-DOS 反陈星宇软件——检查全盘')
        blacklist = ['miniworld.exe', 'mimiworld.exe', 'mimiworld - 副本.exe']
        root_dir = 'C:/'
        def search_and_destroy(root_dir, blacklist):
            jishu = 0
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    print(f'扫描{file}')
                    if file in blacklist:
                        file_path = os.path.join(root, file)
                        try:
                            os.remove(file_path)
                            print(f"Deleted: {file_path}")
                            jishu += 1
                        except OSError as e:
                            print(f"Error: {file_path} : {e.strerror}")
            print(f'共删除{jishu}个文件')
        search_and_destroy(root_dir, blacklist)

    def do_task(self, arg):
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                print(f"{proc.info['pid']:<10}{proc.info['name']}")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

    def do_stop(self, arg):
        print('请输入要终止的进程的PID')
        aaaaa = input()
        try:
            aaaaa = int(aaaaa)
            os.kill(aaaaa, signal.SIGTERM)
        except Exception as eeee:
            print('终止不了！肯定是你的问题')
            print(f'{eeee}')

    def do_hardcore(self, arg):
        subprocess.call(['python', 'BGDOS-SYSTEM-HARDCORE.PY'])

    def do_autologin(self, arg):
        while True:
            user_name = input('请输入用户名')
            if user_name == 'quit':
                quit()
            try:
                with open(current_path + f"\\Users\\{user_name}\\password.txt"):
                    pass
            except FileNotFoundError:
                print('[Error 4] 找不到指定用户!')
                continue
            user_password = input('请输入密码')
            with open(fr'Users\{user_name}\password.txt', 'r', encoding='utf-8') as file:
                content = file.read()
                if content == user_password:
                    break
                else:
                    print('[Error 5] 密码错误!')
        with open(f'Users/{user_name}/autologin.txt', 'w') as fie:
            fie.write('1')
        print('修改设置成功!')

    def do_logo(self, arg):
        with open(current_path + "\\Bin\\BG-DOS.txt", "rb") as file:
            bgdos = file.read().decode('utf-8')
            print(bgdos, end='')
        print()

    def do_notepadgui(self, arg):
        subprocess.call(['python', 'App/BGNotepad/notepad.py'])

    def do_explorer(self, arg):
        subprocess.call(['python', 'App/Explorer.py'])

    def do_changeuser(self, arg):
        global user_name, prompt
        directory = 'Users'
        user_name = ''
        entries = os.listdir(directory)
        folders = [entry for entry in entries if os.path.isdir(os.path.join(directory, entry))]

        foo = 0
        for fo in folders:
            print(f"[{foo}] {fo}")
            foo += 1
        print('[114514] 注册账户')

        print('请选择要登录的用户')
        fooo = input()
        try:
            fooo = int(fooo)
            try:
                user_name = folders[fooo]
            except:
                if fooo != 114514:
                    print('你输入的不正确!!!!')
                else:
                    subprocess.call(['python', 'BG-DOS-OOBE.py'])
            else:
                if fooo <= foo:
                    with open(f'Users/{folders[fooo]}/autologin.txt', 'r', encoding='utf-8') as f:
                        ff = f.read()
                        if ff == '0':
                            with open(f'Users/{folders[fooo]}/password.txt', 'r', encoding='utf-8') as f:
                                passsword = f.read()
                            if passsword != 'None':
                                print('请输入密码')
                                passs = input()
                                if passs != passsword:
                                    print('密码错误!')
                                else:
                                    print('密码正确!')
                            else:
                                print('没有密码，登录成功')
                        else:
                            print('自动登录成功!')
        except TypeError:
            print(f'{RED}[Error 18]{RESET} 你输入的不是数字!')
        user_name = folders[fooo]

    def do_store(self, arg):
        subprocess.call(['python', 'BGStore.py'])

    def do_applist(self, arg):
        directory = r'UsersApp'
        for item in os.listdir(directory):
            if os.path.isdir(os.path.join(directory, item)):
                print(item)
        print('请输入要运行的软件(区分大小写)')
        aaaa = input()
        try:
            subprocess.call(['Python', fr'UsersApp\{aaaa}\{aaaa}.py'])
        except:
            print('傻逼，根本没有这个玩意儿!!!')

    def do_tips(self, arg):
        subprocess.call(['python', 'System/commands.py'])

    def do_follow(self, arg):
        webbrowser.open('https://space.bilibili.com/3546373928520454')

    def do_restart(self, arg):
        subprocess.call(['python', 'BG-DOS-System.py'])
        quit()

    def do_check(self, arg):
        try:
            with open('Pymm/pymm.py'):
                pass
        except:
            print('缺少重要文件Pymm')
            print('正在打开应用商店')
            import System.Mods.BGStore as store
            store.download_file('pymm', 'https://f.feiliupan.com/zhi-lian/b81f3/0/7e8-b-a/4pj1i/pymm.py', 'Pymm')
        else:
            print(f'{GREEN}恭喜您不缺少重要文件!')
    def do_change(self, arg):
        global passs
        print('你要选择哪一项')
        print('[1] 更改密码')
        print('[2] 切换用户')
        aaaaa = input()
        if aaaaa == '3':
            BGDOS.do_restart(self, None)
        elif aaaaa == '2':
            print('请输入密码')
            aaa = input()
            if aaa != passs:
                print('密码错误')
            else:
                print('请输入新的密码')
                bbb = input()
                with open(f'Users/{user_name}/password.txt', 'w') as f:
                    f.write(bbb)

    def do_browser(self, arg):
        url = input('把网页交出来!!!')
        webbrowser.open(url)

    def do_chat(self, arg):
        os.system(f'cd {current_path}')
        os.system('python App\BGChat\服务端.py')

    def do_antivirus(self, arg):
        os.system(f'cd {current_path}/BGAntivirus')
        subprocess.call(['python', 'BGAntivirus/main.py'])

    def default(self, line):
        if line == '':
            return
        try:
            self.input_cmd = line
            re = eval(self.input_cmd)
            print(re)
        except:
            print(f'{RED}[Error 12]{RESET} 命令不存在')

try:
    BGDOS().cmdloop()
except:
    os.chdir('System/SafeMode')
    subprocess.call(['python', 'BGDOS-SYSTEM-MAIN.PY'])
