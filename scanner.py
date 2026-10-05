import socket
import time


def get_target():
    while True:
        target = input("Enter authorized IP address or hostname: ").strip()

        if not target:
            print("Target cannot be empty.")
            continue

        try:
            resolved_ip = socket.gethostbyname(target)
            return target, resolved_ip
        except socket.gaierror:
            print("Invalid or unreachable hostname/IP address.")


def get_port_range():
    while True:
        try:
            start_port = int(input("Enter starting port: "))
            end_port = int(input("Enter ending port: "))

            if not 1 <= start_port <= 65535:
                print("Starting port must be between 1 and 65535.")
                continue

            if not 1 <= end_port <= 65535:
                print("Ending port must be between 1 and 65535.")
                continue

            if start_port > end_port:
                print("Starting port cannot be greater than ending port.")
                continue

            return start_port, end_port

        except ValueError:
            print("Please enter valid port numbers.")


def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))

            if result == 0:
                try:
                    service = socket.getservbyport(port, "tcp")
                except OSError:
                    service = "Unknown"

                return service

    except socket.error:
        pass

    return None


print("=" * 50)
print("LOCAL NETWORK SECURITY PORT SCANNER")
print("=" * 50)
print("Authorized security testing only.\n")

target_name, target_ip = get_target()
start_port, end_port = get_port_range()

print(f"\nTarget: {target_name}")
print(f"Resolved IP: {target_ip}")
print(f"Port Range: {start_port}-{end_port}")
print("\nScanning...\n")

start_time = time.time()
open_ports = 0

for port in range(start_port, end_port + 1):
    service = scan_port(target_ip, port)

    if service:
        print(f"[OPEN] Port {port:<5} Service: {service}")
        open_ports += 1

elapsed_time = time.time() - start_time

print("\n" + "=" * 50)
print("SCAN COMPLETE")
print("=" * 50)
print(f"Open ports: {open_ports}")
print(f"Scan time: {elapsed_time:.2f} seconds")
