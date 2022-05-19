# weballurl
## 获取指定网站所有url

weballurlr 可以递归获取一个网站的所有href标签下的url，多个层级均可获取。获取时判断url是否为本站地址

- Type some Markdown on the left
- See HTML in the right
- ✨Magic ✨

## 注意
- 适用于python3.6以上
- 调用传入http://xxx or https://xxx即可运行返回结果
- 根据网站的大小时间长短不一样
、

## 安装

```sh
pip install xx
```

## 使用
```
from weballurl.geturl import geturl
b = geturl()
a = b.startres('https://blog.csdn.net/weixin_41194129/article/details/110459615', 'csdn.net')
print(a)
```
## License

MIT

MIT License
Copyright (c) 2022 zyg0531
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
