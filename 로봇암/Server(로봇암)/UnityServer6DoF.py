import socket
import time

# 서버 설정
HOST = '0.0.0.0'
PORT = 12345

# 소켓 객체 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 주소 재사용 설정
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# IP와 PORT를 바인드
server_socket.bind((HOST, PORT))

# 서버 시작
server_socket.listen()
print("서버 시작, 포트:", PORT)

client_socket, addr = server_socket.accept()
print("연결된 클라이언트:", addr)

# 초기 6 DOF 좌표
x, y, z = 0, 0, 0
roll, pitch, yaw = 0, 0, 0

while True:
    # 이 부분에서 6 DOF 좌표값을 업데이트 할 수 있습니다.
    # 예를 들면, x += 1

    # 6 DOF 좌표를 문자열로 변환
    x+=1
    y+=1
    message = f"{x},{y},{z},{roll},{pitch},{yaw}"
    client_socket.sendall(message.encode())
    print("보낸 데이터:", message)

    time.sleep(1)

# 소켓 종료
client_socket.close()
server_socket.close()
