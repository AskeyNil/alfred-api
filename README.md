# Alfred Workflow Python Api


本项目用来构建 Alfred Wordflow 中 Script Filter JSON Format

计划完成：
- [x] Items 创建
  - [x] Item 类
  - [x] Icon 类
  - [x] Type 枚举
  - [x] Mod 类
    - [x] cmd
    - [x] ctrl
    - [x] alt
    - [ ] 暂时只知道这三个
  - [x] Text 类
- [ ] Variables 创建
- [ ] export 输出
  - [x] 只有 Items 的输出
  - [ ] 添加 Varibales 的输出





## 安装

### 将本项目 clone 到你的插件目录
``` bash
git clone https://github.com/AskeyNil/alfred_api.git
```

## 使用

使用前请了解 json 各个参数的作用：

https://www.alfredapp.com/help/workflows/inputs/script-filter/json/

### 构建 item
``` python 
from alfred_api import *

Item("我是标题", "我是副标题")
```

如果只有这两个参数，在 Alfred 上也是可以显示的

### 构建 icon
``` python
Icon("icon.png", Icon.Type.FILEICON)
```

第一个参数是图片路径，第二个参数是类型

> 这里我没有太弄明白官方两个参数的含义 fileicon | filepath
>
> 该参数可以缺省，我目前显示的效果就是 workflow 的图片

### 构建 Mod
``` python 
Mod("我是小标题", "传递的参数", Mod.Type.CMD)
```

目前有三个参数可选:
1. Mod.Type.ALT
2. Mod.Type.CMD
3. Mod.Type.CTRL

### 构建 Text
``` python
Text("我是文字内容", Text.Type.COPY)
```

目前有两个参数可选
1. Text.Type.COPY
2. Text.Type.LARGETYPE

实际测试，
1. 给 COPY 参数，按 cmd + c 得到设置的数值
2. 不给 COPY 参数，按 cmd + c 没有任何反应
3. 给 LARGETYPE 参数，按 cmd + l 显示设置的数值
4. 不给 LARGETYPE 参数，按 cmd + l 显示当前的指令


### 输出结果

``` python

item = Item("我是标题", "我是副标题")
export([item])
```





