# -*- coding:utf-8 -*-
# time: 2020/11/16
"""兼容Win7的在终端有颜色地打印python变量"""
__author__ = 'nanarino'

import sys
from decimal import Decimal
#Compatible module of terminal color for Win7 and more
from colorama import init, Fore
init(autoreset=False)


#Connot set attributes of built-in/extension type
def print(obj, max_deep=3, r=False):
    deep = 0
    def _print(*args):
        nonlocal deep
        deep += 1
        args = list(args)
        for i, arg in enumerate(args[:]):
            if isinstance(arg, bool):
                args[i] = Fore.GREEN + str(arg) + Fore.RESET
            elif isinstance(arg, str):
                args[i] = Fore.YELLOW + "\'" + str(arg) + "\'" + Fore.RESET
            elif isinstance(arg, (int, float, complex, Decimal,)):
                args[i] = Fore.CYAN + str(arg) + Fore.RESET
            #print 'list' 'tuple' 'set' or 'dict' directly will lose color by calling '__repr__'
            elif isinstance(arg, tuple):
                if deep > max_deep:
                    args[i] = '(...,)'
                else:
                    args[i] = '('
                    for j in arg:
                        args[i] += _print(j) + ', '
                    args[i] = (args[i][:-1] or '(') + ')'
            elif isinstance(arg, list):
                if deep > max_deep:
                    args[i] = '[...,]'
                else:
                    args[i] = '['
                    for j in arg:
                        args[i] += _print(j) + ', '
                    args[i] = (args[i][:-2] or '[') + ']'
            elif isinstance(arg, set):
                if deep > max_deep:
                    args[i] = '{...,}'
                else:
                    args[i] = ''
                    for j in arg:
                        args[i] += _print(j) + ', '
                    args[i] = ['set()', '{' + args[i][:-2] + '}'][bool(args[i])]
            elif isinstance(arg, dict):
                if deep > max_deep:
                    args[i] = '{:...,}'
                else:
                    args[i] = '{'
                    for j, k in arg.items():
                        args[i] += _print(j) + ': ' + _print(k) + ', '
                    args[i] = (args[i][:-2] or '{') + '}'
            elif args[i] is None:
                args[i] = Fore.MAGENTA + 'None' + Fore.RESET
            elif isinstance(arg, BaseException):
                args[i] = Fore.RED + repr(arg) + Fore.RESET
            else:
                args[i] = str(arg)
        deep -= 1
        return args[0]

    if r:
        return _print(obj)
    sys.stdout.write(_print(obj))
    sys.stdout.write('\n')
            


class Colormsg(str):
    '''带颜色的消息类 默认是白色'''
    color = 'WHITE'

    def __init__(self, msg:str):
        self._msg = msg
        super().__init__()

    def set_color(self, color: str):
        '''设置colorama支持的字体前景色名 全部大写'''
        self.color = color
        return self

    def __str__(self):
        return f'{getattr(Fore, self.color)}{super().__str__()}{Fore.RESET}'

    @staticmethod
    def from_built_in_type(o):
        '''内置类型转带颜色的真实字符串'''
        return print(o, r=True)


def shell():
    '''进入交互式'''
    while 1:
        try:
            ex = input('>>> ')
        except EOFError:
            quit()
        try:
            try:
                print(eval(ex))
            except SyntaxError as e:
                exec(ex)
        except Exception as e:
            print(e)


def proportion_bar(proportion: float, color: str):
    '''直接在CMD中打印的进度条

        Args:
            proportion: 进度比 0-1
            color: colorama支持的字体前景色名 全部大写
    '''
    num = int(proportion * 25)
    sys.stdout.flush()
    sys.stdout.write('\r%s%s' % (Colormsg("█" * num).set_color(color), "█" *
                                 (25 - num)))
    sys.stdout.flush()
    sys.stdout.write('\t% 4d%%' % (100 * proportion))


if __name__ == "__main__":
    sys.stdout.write('开始启动...\n')
    import time
    for i in range(0, 101):
        time.sleep(0.02)
        proportion_bar(i / 100, 'MAGENTA')
    sys.stdout.write('\n启动完成。\n')
    shell()