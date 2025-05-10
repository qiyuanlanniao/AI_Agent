# 使用官方的Python基础镜像
FROM python:3.11.4

# 安装依赖
COPY requirements.txt .
RUN pip install -r requirements.txt

# 安装turnserver和redis-server
RUN apt-get update && apt-get install -y coturn redis-server

#设置Coturn的配置文件
COPY turnserver.conf .

#设置redis
COPY redis.conf .

#设置redis的数据目录
VOLUME /data

WORKDIR /app

#复制代码到容器
COPY . /app

#设置开放端口
EXPOSE 8000 3478 6379


#启动服务
CMD ["sh","-c","turnserver -c turnserver.conf --listening-ip=0.0.0.0 --listening-port=3478 & redis-server redis.conf --protected-mode no & sleep 3 && uvicorn server:app --host 0.0.0.0 --port 8000"]