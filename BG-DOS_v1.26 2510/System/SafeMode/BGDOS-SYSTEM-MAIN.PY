import os
import webbrowser
print('恢复')
current_path = os.getcwd()
os.system('title BG-DOS Safe Mode')
while True:
    cmd = input(r'BG-DOS安全模式>>>')
    match cmd.lower():
        case 'about':
            print('BG-DOS 1.4 Update 3')

        case 'follow':
            webbrowser.open('https://space.bilibili.com/3546373928520454')

        case 'usebook':
            with open(current_path + "\\BG_SYSTEM\\BIN\\指令说明.txt", "r", encoding="utf-8") as menu:
                for text in menu.readlines():
                    print(text)

        case 'notepad':
            with open(current_path + "\\BG_SYSTEM\\APP\\NOTEPAD.py", "rb") as file:
                notepad = file.read().decode('utf-8')
            exec(notepad)

        case 'calc':
            with open(current_path + "\\BG_SYSTEM\\APP\\CALC.py", "rb") as file:
                calc = file.read().decode('utf-8')
            exec(calc)