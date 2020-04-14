import sys
#Compatible module of terminal color for Win7 and more
from colorama import init, Fore
init(autoreset=False)


#Connot set attributes of built-in/extension type
def _print(*args, r=False):
    args = list(args)
    for i, arg in enumerate(args[:]):
        if isinstance(arg, bool):
            args[i] = Fore.GREEN + str(arg) + Fore.RESET
        elif isinstance(arg, str):
            args[i] = Fore.YELLOW + "\'" + str(arg) + "\'" + Fore.RESET
        elif isinstance(arg, (int, float, complex)) or str(
                type(arg)) == "<class 'decimal.Decimal'>":
            args[i] = Fore.CYAN + str(arg) + Fore.RESET
        #print 'list' 'tuple' 'set' or 'dict' directly will lose color by calling '__repr__'
        elif isinstance(arg, tuple):
            args[i] = '('
            for j in arg:
                args[i] += _print(j, r=True) + ', '
            args[i] = (args[i][:-1] or '(') + ')'
        elif isinstance(arg, list):
            args[i] = '['
            for j in arg:
                args[i] += _print(j, r=True) + ', '
            args[i] = (args[i][:-2] or '[') + ']'
        elif isinstance(arg, set):
            args[i] = ''
            for j in arg:
                args[i] += _print(j, r=True) + ', '
            args[i] = ['set()', '{' + args[i][:-2] + '}'][bool(args[i])]
        elif isinstance(arg, dict):
            args[i] = '{'
            for j, k in arg.items():
                args[i] += _print(j, r=True) + ': ' + _print(k, r=True) + ', '
            args[i] = (args[i][:-2] or '{') + '}'
        elif args[i] is None:
            args[i] = Fore.MAGENTA + 'None' + Fore.RESET
        elif isinstance(arg, BaseException):
            args[i] = Fore.RED + repr(arg) + Fore.RESET
        else:
            args[i] = str(arg)
    if r:
        return args[0]
    else:
        print(*args)


#带颜色的消息类
class Colormsg():
    def __init__(self, msg, color):
        self._msg = msg
        self.color = color

    def __str__(self):
        return getattr(Fore, self.color) + self._msg + Fore.RESET

    def __repr__(self):
        return self._msg


#进入交互式
def shell():
    while 1:
        ex = input('>>> ')
        try:
            try:
                _print(eval(ex))
            except SyntaxError as e:
                exec(ex)
        except Exception as e:
            print("Traceback (most recent call last):")
            _print(e)


#进度条
def proportion_bar(proportion, color):
    num = int(proportion * 25)
    sys.stdout.write('\r%s%s' % (Colormsg("█" * num, color), "█" * (25 - num)))
    sys.stdout.write('\t%d%%' % (100 * proportion))
    sys.stdout.flush()


if __name__ == "__main__":
    print('开始启动...')
    import time
    for i in range(0, 101):
        time.sleep(0.02)
        proportion_bar(i / 100, 'MAGENTA')
    print('\n启动完成。')
    shell()