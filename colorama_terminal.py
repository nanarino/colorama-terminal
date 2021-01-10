# -*- coding:utf-8 -*-
# time: 2021/01/10
__author__ = 'nanarino'

import sys
from decimal import Decimal
from colorama import init, Fore
from functools import reduce
init(autoreset=False)


class Colorstr(str):
    '''带颜色的字符串类'''
    def __init__(self, msg):
        self._msg = str(msg)
        super().__init__()

    @staticmethod
    def from_built_in_type(o: object):
        '''由内置类型生成实例'''
        return Colorstr(print(o, raw=True))

    def __add__(self, other):
        return Colorstr(str(self) + str(other))

    def __radd__(self, other):
        return Colorstr(str(other) + str(self))

    def __mul__(self, other):
        return Colorstr(super().__mul__(other))

    def __rmul__(self, other):
        return self.__mul__(other)


class Colormsg(Colorstr, str):
    '''可以设置颜色的消息类 默认白色'''
    color = 'WHITE'

    def set_color(self, color: str):
        '''设置colorama支持的字体前景色名 全部大写'''
        self.color = color
        return self

    def __str__(self):
        return getattr(Fore, self.color) + super().__str__() + Fore.RESET

    def __mul__(self, other):
        return Colormsg(self._msg * other).set_color(self.color)

    def __getitem__(self, item):
        return Colormsg(super().__getitem__(item)).set_color(self.color)


def print(*objects,
          sep=' ',
          end: str = '\n',
          prefix: str = '',
          max_deep: int = 3,
          raw: bool = False,
          flush: bool = False) -> Colorstr:
    """花里胡哨输出的print 如果raw为True会把将要输出的内容返回"""
    deep = 0

    def to_color_str(o):
        if isinstance(o, Colorstr): return o
        if o is None: return Colormsg('None').set_color('MAGENTA')
        if isinstance(o, bool): return Colormsg(o).set_color('GREEN')
        if isinstance(o, str): return Colormsg(repr(o)).set_color('YELLOW')
        if isinstance(o, (
                int,
                float,
                complex,
                Decimal,
        )):
            return Colormsg(o).set_color('CYAN')
        if isinstance(o, BaseException):
            return Colormsg(repr(o)).set_color('RED')
        nonlocal deep
        deep += 1
        if isinstance(o, tuple):
            if deep > max_deep:
                ret = '(...,)'
            else:
                ret = '('
                for j in o:
                    ret += to_color_str(j) + ', '
                ret = (ret[:-1] or '(') + ')'
        elif isinstance(o, list):
            if deep > max_deep:
                ret = '[...,]'
            else:
                ret = '['
                for j in o:
                    ret += to_color_str(j) + ', '
                ret = (ret[:-2] or '[') + ']'
        elif isinstance(o, set):
            if deep > max_deep:
                ret = '{...,}'
            else:
                ret = ''
                for j in o:
                    ret += to_color_str(j) + ', '
                ret = ['set()', '{' + ret[:-2] + '}'][bool(ret)]
        elif isinstance(o, dict):
            if deep > max_deep:
                ret = '{:...,}'
            else:
                ret = '{'
                for j, k in o.items():
                    ret += to_color_str(j) + ': ' + to_color_str(k) + ', '
                ret = (ret[:-2] or '{') + '}'
        else:
            ret = repr(o)
        deep -= 1
        return ret

    ret = reduce(lambda rets, o: rets + sep + to_color_str(o), objects,
                 Colorstr(''))[len(str(sep)):]
    if raw: return ret
    sys.stdout.write(str(prefix + ret + end))
    if flush: sys.stdout.flush()


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
    print(Colormsg("█").set_color(color) * num + "█" * (25 - num) +
          '\t% 4d%%' % (100 * proportion),
          prefix='\r',
          end='',
          flush=True)


if __name__ == "__main__":
    print(Colormsg('开始启动...'))
    import time
    for i in range(0, 101):
        time.sleep(0.02)
        proportion_bar(i / 100, 'MAGENTA')
    print(Colormsg('\n启动完成。'))
    shell()