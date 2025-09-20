import socket
import csv
from threading import Thread
from queue import Queue

# Renkler
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Yaygın port listesi
common_ports = [21, 22, 23, 25, 53, 67, 68, 80, 110, 135, 139, 143,
                161, 443, 445, 3306, 3389, 5900, 8080]

# Port servis veritabanı
port_servisleri = {
    20: "FTP (Data)", 21: "FTP (Control)", 22: "SSH", 23: "Telnet",
    25: "SMTP", 53: "DNS", 67: "DHCP", 68: "DHCP", 80: "HTTP",
    110: "POP3", 135: "RPC", 139: "NetBIOS", 143: "IMAP", 161: "SNMP",
    443: "HTTPS", 445: "SMB", 3306: "MySQL", 3389: "RDP", 5900: "VNC",
    8080: "HTTP-Proxy"
}

queue = Queue()
open_ports = []
closed_count = 0

# TCP port tarayıcı
def tcp_scan(hedef, port):
    global closed_count
    try:
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.settimeout(0.5)
        sonuc = soket.connect_ex((hedef, port))
        if sonuc == 0:
            try:
                soket.send(b'HEAD / HTTP/1.0\r\n\r\n')
                banner = soket.recv(1024).decode().strip()
            except:
                banner = port_servisleri.get(port, "Bilinmeyen servis")
            servis = port_servisleri.get(port, banner)
            print(f"{GREEN}[TCP] {port} portu AÇIK → {servis}{RESET}")
            open_ports.append({'Port': port, 'Protocol': 'TCP', 'Service': servis})
        else:
            closed_count += 1
        soket.close()
    except:
        closed_count += 1

# UDP port tarayıcı
def udp_scan(hedef, port):
    global closed_count
    try:
        soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        soket.settimeout(0.5)
        soket.sendto(b'', (hedef, port))
        try:
            data, _ = soket.recvfrom(1024)
            servis = port_servisleri.get(port, "Bilinmeyen servis")
            print(f"{GREEN}[UDP] {port} portu AÇIK → {servis}{RESET}")
            open_ports.append({'Port': port, 'Protocol': 'UDP', 'Service': servis})
        except socket.timeout:
            closed_count += 1
        soket.close()
    except:
        closed_count += 1

# Thread fonksiyonu
def worker(hedef, protocol):
    while not queue.empty():
        port = queue.get()
        if protocol == 'TCP':
            tcp_scan(hedef, port)
        else:
            udp_scan(hedef, port)
        queue.task_done()

# Kullanıcıdan bilgiler
hedef = input("Hedef IP veya domain: ").strip()
hedef = hedef.replace("http://", "").replace("https://", "").replace("/", "")

print("Port listesi seçenekleri:")
print("1- Common ports (21,22,23,25,53,80...)")
print("2- Tüm portlar (1-1024)")
secim = input("Seçiminiz (1/2): ")

if secim == '1':
    port_list = common_ports
else:
    port_list = list(range(1, 1025))

protocol = input("TCP veya UDP taraması (TCP/UDP/Her ikisi için 'BOTH'): ").upper()
thread_sayisi = int(input("Kaç thread kullanılacak (örn: 50): "))

# Queue doldur
for port in port_list:
    queue.put(port)

# Tarama başlat
threads = []
if protocol in ['TCP', 'BOTH']:
    for _ in range(thread_sayisi):
        t = Thread(target=worker, args=(hedef, 'TCP'))
        t.start()
        threads.append(t)
if protocol in ['UDP', 'BOTH']:
    for _ in range(thread_sayisi):
        t = Thread(target=worker, args=(hedef, 'UDP'))
        t.start()
        threads.append(t)

queue.join()

# Tarama özeti
print(f"\n[+] Tarama tamamlandı!")
print(f"[+] Açık port sayısı: {len(open_ports)}")
print(f"[+] Kapalı port sayısı: {closed_count}")

# CSV kaydet
with open('tarama_sonucu.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Port', 'Protocol', 'Service']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in open_ports:
        writer.writerow(row)

print("[+] Açık portlar 'tarama_sonucu.csv' dosyasına kaydedildi.")
