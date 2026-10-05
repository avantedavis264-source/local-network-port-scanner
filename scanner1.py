import socket

target = input("Enter authorized IP address: ")

ports = [21, 22, 23, 25, 53, 80, 110, 443, 445, 3389]

print(f"\nScanning {target}...\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")

    sock.close()

print("\nScan complete.")