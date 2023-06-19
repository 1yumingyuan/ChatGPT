from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def proxy():
    # 获取服务器IP地址
    server_ip = request.remote_addr

    # 构造访问URL
    url = f"http://chat.openai.com{request.full_path}"

    # 发起请求获取chat.openai.com的内容
    response = requests.get(url)

    # 将chat.openai.com的响应返回给用户
    return Response(response.content, content_type=response.headers['content-type'])

if __name__ == '__main__':
    app.run()
