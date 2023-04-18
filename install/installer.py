import os


reqPath = os.path.join('install','requirements.txt')
os.system(f'pip3 install -r {reqPath}')