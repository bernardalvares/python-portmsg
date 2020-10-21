 #!/usr/bin/python3
   
 import socket
   
 cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   
 while True:
 mensagem_envio = input("Digite a mensagem:")
 cliente.sendto(mensagem_envio.encode(),("192.168.33.10",12000))
 mensagem_bytes, endereco_ip_servidor = cliente.recvfrom(1234)
 print(mensagem_bytes.decode())

