import struct
import os
import io


def read_int(stream):
    return struct.unpack(">I", stream.read(4))[0]


def to_namelist(namelist):
    namelist_bytes = ",".join(namelist).encode('utf-8')
    namelist_length = struct.pack(">I", len(namelist_bytes))
    return namelist_length + namelist_bytes


def from_namelist(namelist):
    namelist_length = read_int(namelist)
    namelist_ = namelist.read(namelist_length).decode('utf-8')
    return namelist_.split(",")


def packetizer(message):
    packet_length = struct.pack(">I", len(message))
    padding_length = os.urandom(1)
    return packet_length + padding_length + message


def de_packetizer(message):
    msg_bytes = io.BytesIO(message)
    msg_length = read_int(msg_bytes)
    padding_length = struct.unpack(">B", msg_bytes.read(1))[0]
    payload = msg_bytes.read(msg_length)
    return payload