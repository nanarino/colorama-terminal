# colorama-terminal

在终端有颜色地打印python变量。



## 使用方法

先安装依赖

- 打开方式没有被修改的话可以直接双击运行，运行效果和python shell一样。

- `from colorama_terminal import _print`引入，

  使用`_print()`函数代替`print()`。
  
  cmd中python+文件名（需要设置环境变量）可以看到效果。

### 安装依赖

第三方模块`colorama`

```bash
pip install colorama
```



## 使用

注意，直接双击运行或者cmd中python文件名执行。

`conn-mssql.py`，展示mssql查询结构的示例。



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



## 核心问题

-  `__str__()`和`__repr__()`

-  `built-in/extension type`


