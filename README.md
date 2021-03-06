# hashpass

> 哈希密码生成程序

## 关于 hashpass

如果所有的网站都使用同一个密码毫无疑问是非常不安全的, 密码一旦丢失所有账号都会被一锅端. 常见的处理方法是生成随机密码, 目前有很多软件和应用可以做到, 但随机密码有个不好的地方, 密码非常难记需要有个地方储存密码, 你可以保存到云上或者本地, 但这又产生信任和丢失的问题. 于是我想用一种尽可能简单的方法, 来生成复杂同时又不需要储存的密码, 那就是记住一个盐值, 然后生成哈希密码.

## 算法

1. 将输入的域名(`domain`)与环境变量设置的盐(`HASHPASS_SALT`)进行字符串拼接
2. 拼接得到的字符串使用 `SHA-256` 算法加密
3. 然后把得到的哈希值进行 `base64` 编码
4. 截取前`length`个字符串, 返回结果

## 使用

输入域名和密码长度, 点击开始, 程序会自动复制结果到剪贴板, 直接 `CTRL + V` 即可

## 打包程序

```bash
pip install -r requirements.txt
pyinstaller -Fw main.py
```
