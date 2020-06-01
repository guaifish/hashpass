# hashpass

> 哈希密码生成程序

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
