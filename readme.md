# colorama-terminal

在终端有颜色地打印python变量。



## 使用方法

- 直接用python解释器运行（打开方式没有被修改的话可以直接双击运行）

- 在cmd的python交互式运行环境中`from colorama-terminal import _print`

  使用`_print()`函数代替`print()`



## 依赖

第三方模块`colorama`

### 安装

```bash
pip install colorama
```

### 为什么选用`colorama`模块

#### 直接使用代码

```python
\033[1;31;40m    #1-高亮显示 31-前景色红色  40-背景色黑色
\033[0m 
```

在我的电脑（Win7）上是无效。

#### 使用第三方模块`termcolor`

```python
from termcolor import colored

print(colored("helloworld", "red"))
```

在我的电脑（Win7）上依然是无效。

#### 使用第三方模块`colorama`

```python
from colorama import  init, Fore

init(autoreset=True)
print(Fore.RED + "helloworld" + Fore.RESET)
```

在我的电脑（Win7）上终于有效了。



## 核心问题

### `__str__()`和`__repr__()`

python对象的`__str__()`方法在拼接颜色字符后

打印的时候再调用`__repr__()`方法

转义会出现问题导致颜色代码直接出现在终端。

而列表等元素的`__str__()`方法本身就会对每个成员调用`__repr__()`方法。

### `built-in/extension type`

无法为`built-in/extension`类型重写或拓展方法。

只能重写一个类似print()的函数。