from flask import Flask, jsonify
from flask_cors import CORS  # 解决跨域问题

app = Flask(__name__)
CORS(app)  # 允许前端访问后端

# 定义一个测试接口
@app.route('/api/test', methods=['GET'])
def test_api():
    print("前端点击了按钮！")  # 后端控制台打印
    return jsonify({"message": "后端收到请求啦！"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # 启动后端，端口5000