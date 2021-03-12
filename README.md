# fisher

## 环境

安装 pipenv： `pip install pipenv`

创建虚拟环境：进入项目文件夹，输入： `pipenv install`

激活(进入)虚拟环境：`pipenv shell`

安装包：

- flask `pipenv install flask==1.0.1`



pipenv 其他常用命令

- 退出：`exit`
- 卸载包：`pipenv uninstall flask`
- 查看安装包的依赖关系：`pipenv graph`
- 查看虚拟环境的安装路径：`pipenv --venv`

 

## demo

fisher.py

```python
from flask import Flask


app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello Flask'


app.run()

```

执行 `python fisher.py` 启动服务器 

浏览器访问：`http://127.0.0.1:5000/hello`

```python
from flask import Flask, make_response


app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    headers = {
        'content-type': 'text/plain',
        'location': 'https://www.bing.com/'
    }
    response = make_response('<html></html>', 301)
    response.headers = headers
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)

```


