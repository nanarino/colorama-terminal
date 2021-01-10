# colorama-terminal

在终端有颜色地打印python变量。

## 安装依赖

第三方模块`colorama`

```bash
pip install colorama
```



## 使用

带颜色的字符串 Colormsg类

```python
import colorama_terminal as ct

# 打印紫色的你好
hello = ct.Colormsg("helloworld").set_color('MAGENTA')
print(hello)

# 打印复杂的数据
raw_colormsg = ct.Colormsg.from_built_in_type([{1: True}, {"2": False}])
print(raw_colormsg)

# 打印复杂的数据
ct.print([{1: True}, {"2": False}])
```

其他功能  print  proportion_bar shell函数

```python
from colorama_terminal import * #内置的print被覆盖了
# 进度条
import time
for i in range(0, 101):
    time.sleep(0.02)
    proportion_bar(i / 100, 'MAGENTA')
print('\nOK')

# 进入交互式
shell()
```

注意，直接双击运行或者cmd中python文件名执行。
