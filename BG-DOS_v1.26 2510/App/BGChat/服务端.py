import socketserver


# 1. 继承一个类
class sqServer(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        print('小傻逼们，聊天服务器已上线......')

        while True:

            # 接收客户端数据
            client_data=self.request.recv(1024)
            print(client_data.decode('utf-8'))

            # 发送消息给客户端
            send_data=input('请输入内容：')
            self.request.sendall(send_data.encode('utf-8'))
        self.request.close()


# 2. 创建服务
server=socketserver.ThreadingTCPServer(('192.168.3.17',7777),sqServer)

# 3. 保持在线
server.serve_forever()
