import os
import socket
import struct
import io

from utils import to_namelist, from_namelist, packetizer, de_packetizer
from config import _preferred_kex, _preferred_keys, _preferred_ciphers, _preferred_macs, _preferred_compression

ADDRESS = ('localhost',22)
MSG_KEXINIT = 20

def main():
    # initial tcp handshake
    print("Connecting to socket")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(ADDRESS)

    # Version Exchange
    print()
    print("Doing Version Exchange")
    local_version = b'SSH-2.0-MySSH\r\n'
    sock.sendall(local_version)

    remote_version = sock.recv(1024)
    print("SENT     : {}".format(local_version))
    print("RECEIVED : {}".format(remote_version))

    # Key negotiation
    print()
    print("Negotiating the keys")
    kex_msg = io.BytesIO()

    kex_msg.write(struct.pack("B", MSG_KEXINIT))
    kex_msg.write(os.urandom(16))
    kex_msg.write(to_namelist(_preferred_kex))
    kex_msg.write(to_namelist(_preferred_keys))
    kex_msg.write(to_namelist(_preferred_ciphers))
    kex_msg.write(to_namelist(_preferred_ciphers))
    kex_msg.write(to_namelist(_preferred_macs))
    kex_msg.write(to_namelist(_preferred_macs))
    kex_msg.write(to_namelist(_preferred_compression))
    kex_msg.write(to_namelist(_preferred_compression))
    kex_msg.write(bytes())
    kex_msg.write(bytes())
    kex_msg.write(struct.pack("B", 0))
    kex_msg.write(struct.pack(">I", 0))

    packet = packetizer(kex_msg.getvalue())
    sock.sendall(packet)

    data = sock.recv(1024*4)
    msg = de_packetizer(data)

    print("SENT     : {}".format(packet))
    print("RECEIVED : {}".format(data))

    msg = io.BytesIO(msg)
    flag = msg.read(1)
    cookie = msg.read(16)
    kex_algos = from_namelist(msg)
    server_kex = from_namelist(msg)
    encryption_ctos = from_namelist(msg)
    encryption_stoc = from_namelist(msg)
    mac_ctos = from_namelist(msg)
    mac_stoc = from_namelist(msg)
    compression_ctos = from_namelist(msg)
    compression_stoc = from_namelist(msg)
    langs_ctos = from_namelist(msg)
    langs_stoc = from_namelist(msg)
    kex_follows = msg.read(1)

    print(struct.unpack(">B", flag)[0])
    print(cookie)
    print(kex_algos)
    print(server_kex)
    print(encryption_ctos)
    print(encryption_stoc)
    print(mac_ctos)
    print(mac_stoc)
    print(compression_ctos)
    print(compression_stoc)
    print(langs_ctos)
    print(langs_stoc)
    print(kex_follows)

    agreed_kex = list(filter(kex_algos.__contains__ , _preferred_keys))
    print(agreed_kex)

if __name__ == '__main__':

    main()