# 导入模块
from flask import Flask, render_template
import httpie

# 创建flask对象
app = Flask(__name__)
# 设置debug状态，可以让我们不用重启打开程序
app.debug = True


# 设置路由地址，如果地址为  /  就是默认地址
@app.route("/")
def index():
    # 返回字符串  该字符串会显示到主页
    return "主页"


# 设置路由地址，如果地址为  /xxx  就是需要在网址后＋index
@app.route("/hello")
def hello():
    # 返回网页 需要渲染网页,需要注意的是index.html
    # 相关的网页代码要放置到templates文件夹下
    return render_template("index.html")


# 动态路由1
@app.route("/<name>")
def say(name):
    return name

# 动态路由2
@app.route("/say2/<something>")
def say2(something):
    return something

# 动态路由3
@app.route("/say3/<n1>/<n2>")
def say3(n1,n2):
    return n1+n2

# 动态路由4
@app.route("/say4/<name>")
def say4(name):
    return render_template(name + ".html")

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000)
