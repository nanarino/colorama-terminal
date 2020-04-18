# colorama-terminal

在终端有颜色地打印python变量。

## 安装依赖

第三方模块`colorama`

```bash
pip install colorama
```



## 使用

带颜色的字符串

```python
from colorama_terminal import *

# 打印紫色的你好
hello = Colormsg("helloworld").set_color('MAGENTA')
print(hello)

# 打印复杂的数据
raw_colormsg = Colormsg.from_built_in_type([{1: True}, {"2": False}])
print(raw_colormsg)

# 打印复杂的数据
_print([{1: True}, {"2": False}])

# 行为与字符串完全一致，除了__str__()方法
a = Colormsg("helloworld").set_color('RED')
b = Colormsg("helloworld").set_color('GREEN')
print(a == b)
```

其他功能

```python
from colorama_terminal import *
# 进度条
import time
for i in range(0, 101):
    time.sleep(0.02)
    proportion_bar(i / 100, 'MAGENTA')
print('OK')

# 进入交互式
shell()
```

注意，直接双击运行或者cmd中python文件名执行。



---



### 为什么选用`colorama`

因为测试电脑是win7

#### 直接使用代码

```python
'\033[1;31;40m'    #1-高亮显示 31-前景色红色  40-背景色黑色
'\033[0m'
```

在Win7的黑窗口中是无效。

#### 使用`termcolor`

```python
from termcolor import colored

print(colored("helloworld", "red"))
```

依然是无效。

#### 使用`colorama`

```python
from colorama import  init, Fore

init(autoreset=True)
print(Fore.RED + "helloworld" + Fore.RESET)
```

在Win7上终于有效了。


