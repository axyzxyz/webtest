# python3
import socket
import datetime
import re


def request(client):
    buf = client.recv(1024)
    print(buf)
    if buf:
        res = re.findall(r'GET (/.*)HTTP', buf.decode())[0]
    # if res == '/favicon.ico':
    #     return
    else:
        res = 'what?'
    print(res)

    day = datetime.datetime.now()
    day_str = str(day).split('.')[0].encode()
    client.send('HTTP/1.1 200 OK\r\n\r\n'.encode('utf-8') + '<h1>hello world!<h1>'.encode('utf-8') + day_str +
                '<p>访问链接：'.encode('gbk') + res.encode())
    return buf or 'nothong'


def main(ip='0.0.0.0', port=8000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen(5)
    cout = 1
    while cout > 0:
        con, add = sock.accept()
        request(con)
        cout += 1
        con.close()


if __name__ == '__main__':
    main(port=80)
