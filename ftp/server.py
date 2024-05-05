from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def start_ftp_server():
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "password", ".", perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(("127.0.0.1", 21), handler)
    server.serve_forever()

if __name__ == "__main__":
    start_ftp_server()

