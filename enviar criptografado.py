
import socket
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES

UDP_IP = "127.0.0.1"
UDP_PORT = 7777

data = b"ja nao estou mais perdido o joao me ajudou:"
key = b64decode('ABEiM0RVZneImQARIjNEVQ==')

cipher = AES.new(key, AES.MODE_CFB)
ct_raw = cipher.encrypt(data)
iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_raw).decode('utf-8')
result = bytes(json.dumps({'iv':iv,'ct':ct,'aluno':'binhao aqui'}),'utf-8')
print (result)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
sock.sendto(result, (UDP_IP, UDP_PORT))