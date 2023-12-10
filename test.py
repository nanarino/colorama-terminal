from colorama_terminal import *

if __name__ == "__main__":
    print(Colormsg('开始测试进度条功能...'))
    import time
    for i in range(0, 101):
        time.sleep(0.02)
        proportion_bar(i / 100, 'MAGENTA')
    print(Colormsg('\n进度条功能测试完毕。'))
    shell()
