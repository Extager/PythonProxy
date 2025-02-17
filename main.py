import socks

class Proxy:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def connect(self):
        s = socks.socksocket()
        s.set_proxy(socks.SOCKS5, self.ip, self.port)
        print(f"Connecting to {self.ip}:{self.port}")


def main():
    proxy = Proxy('127.0.0.1', 9050)
    proxy.connect()


if __name__ == '__main__':
    main()