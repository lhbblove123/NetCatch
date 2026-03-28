@echo off
echo 启动后端服务...
start "后端服务" cmd /k "cd backend && python app.py"

echo 启动前端服务...
start "前端服务" cmd /k "cd web && python -m http.server 3000"

echo 项目启动完成！
echo 前端地址：http://localhost:3000
echo 后端地址：http://localhost:5000