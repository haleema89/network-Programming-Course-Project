
from asyncio import start_server
import socket
import json

HOST = "127.0.0.1"
PORT = 5050

def recv_json(sock):
    return json.loads(sock.recv(4096).decode())

def main():
    name = input("Enter your name: ")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.send(name.encode())

        while True:
            print("""
1. headlines_country
2. headlines_category
3. headlines_keywords
4. headlines_all
5. sources_country
6. sources_category
7. sources_language
8. sources_all
0. Quit
""")
            opt = input("Option: ").strip()

            if opt == "0":
                break

            param = input("Parameter (or Enter): ")
            client.send(f"{opt}|{param}".encode())

            data = recv_json(client)
            print(data)

            idx = input("Index (Enter to skip): ")
            if idx:
                client.send(idx.encode())
                full = recv_json(client)
                print(full)

if __name__ == "__main__":
    main()