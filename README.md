# 狗屁不通文章生成器
# BullshitGenerator

*以下部分来自[原版 Readme](https://github.com/menzi11/BullshitGenerator/blob/master/README.md)*

---

偶尔需要一些中文文字用于GUI开发时测试文本渲染. __本项目只做这一项, 请勿用于其他任何用途__.

Needs to generate some texts to test if my GUI rendering codes good or not. so I made this.

本项目为python3版本, 还有由suulnnka修改在线版, 使用更加方便:
https://suulnnka.github.io/BullshitGenerator/index.html

下一步计划:
1. 防止文章过于内容重复
1. 加入更多啰嗦话.
1. 加入马三立<开会迷>里的内容
1. 加入手写体直接渲染出图片的功能(__仅仅用于测试本人的打印机是否工作正常, 请勿做它用__).

----

## 关于Pull requests:

鄙人每个requests都会仔细阅读, 但因近期事情较多, merge未必及时, 毕竟是业余项目, 请大家见谅. 如果未来实在更新不及时, 也欢迎有志之士替代本人继续本项目.

## 关于中文变量名:

平时撸码鄙人是不写中文变量名的, 本项目中的中文变量名只是最开始瞎写的时候边写语料边写代码时懒得切英文输入法了. 不过既然如此就保持吧!

## 关于生成算法

鄙人才疏学浅并不会任何自然语言处理相关算法. 而且目前比较偏爱简单有效的方式达到目的方式. 除非撞到了天花板, 否则暂时不会引入任何神经网络等算法. 不过欢迎任何人另开分支实现更复杂, 效果更好的算法. 不过除非效果拔群, 否则鄙人暂时不会融合.

---

这个分支用 PHP 实现了“狗屁不通文章生成器”，并且加入了**渲染图片**的功能。

参考原 repo 的 [Issue #39](https://github.com/menzi11/BullshitGenerator/issues/39)，添加了由 [@acdzh](https://github.com/acdzh) 收集的大量名言。

可以对参数自定义：

| 参数名 | 说明 | 示例 |
| --- | --- | --- |
| `word` | 文章的主题 | 学生会退会 |
| `length` | 文章的字数 | 1000 |
| `width` | 生成图片的宽度。文章默认以纯文本形式输出，设定此项则以图片形式输出 | 500 |
| `fontsize` | 图片上的字号 | 16 |

* 图片宽度上限为 1024 像素
* 字数上限为 65536 字（以文本输出）或 2048 字（以图片输出）

~~不设定上限的话我的服务器说不定就要炸了⊂彡☆))∀`)~~

输出纯文本示例：[https://i.akarin.dev/bullshit/?word=膜蛤&length=6000](https://i.akarin.dev/bullshit/?word=膜蛤&length=6000)

输出图片示例：[https://i.akarin.dev/bullshit/?word=膜蛤&length=500&width=640&fontsize=16](https://i.akarin.dev/bullshit/?word=膜蛤&length=500&width=640&fontsize=16)

![](https://i.akarin.dev/bullshit/?word=膜蛤&length=500&width=640&fontsize=16)