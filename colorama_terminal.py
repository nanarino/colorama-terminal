#Compatible module of terminal color for Win7 and more
from colorama import init, Fore
init(autoreset = True)

#Connot set attributes of built-in/extension type
def _print(*args, r = False):
    args = list(args)
    for i, arg in enumerate(args[:]):
        if isinstance(arg, bool):
            args[i] = Fore.GREEN + arg.__str__() + Fore.RESET
        elif isinstance(arg, str):
            args[i] = Fore.YELLOW + "\'" + arg.__str__() + "\'" + Fore.RESET
        elif isinstance(arg, (int, float, complex)) or str(type(arg)) == "<class 'decimal.Decimal'>":
            args[i] = Fore.CYAN + arg.__str__() + Fore.RESET
        #print 'list' 'tuple' 'set' or 'dict' directly will lose color by calling '__repr__'
        elif isinstance(arg, tuple):
            args[i] = '('
            for j in arg:
                args[i] += _print(j,r = True) + ', '
            args[i] = (args[i][:-1] or '(') + ')'
        elif isinstance(arg, list):
            args[i] = '['
            for j in arg:
                args[i] += _print(j,r = True) + ', '
            args[i] = (args[i][:-2] or '[') + ']'
        elif isinstance(arg, set):
            args[i] = ''
            for j in arg:
                args[i] += _print(j,r = True) + ', '
            args[i] = ['set()','{' + args[i][:-2] + '}'][bool(args[i])]
        elif isinstance(arg, dict):
            args[i] = '{'
            for j,k in arg.items():
                args[i] += _print(j,r = True) + ': ' + _print(k,r = True) + ', '
            args[i] = (args[i][:-2] or '{') + '}'
        elif args[i] is None:
            args[i] = Fore.MAGENTA + 'None' + Fore.RESET
        elif isinstance(arg, BaseException):
            args[i] = Fore.RED + arg.__repr__() + Fore.RESET
        else:
            args[i] = arg.__str__()
    if r:
        return args[0]
    else:
        print(*args)

#return color string
class Colorexec():
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def __str__(self):
        return getattr(Fore, self.color) + self.name + Fore.RESET

if __name__ == "__main__":
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