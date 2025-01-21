import os
import shutil
import subprocess

def run_sys(path, name):
    if os.path.exists(path):
        shutil.copytree(path, '虚拟机/'+name)
        os.chdir(f'虚拟机/{name}')
        subprocess.call(['python', 'BGDOS-SYSTEM-MAIN.PY'])
    else:
        print('找不到系统!')
