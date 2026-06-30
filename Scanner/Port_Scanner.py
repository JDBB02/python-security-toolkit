import socket

def scan_single_port():

    target = input("\nEnter a hostname or IP address: ")

    try:
        port = int(input("Enter the port to scan: "))
    except ValueError:
        print("Please enter a valid port number.")
        return

    print(f"\nScanning {target}:{port}...")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"✅ Port {port} is OPEN")
    else:
        print(f"❌ Port {port} is CLOSED")

    sock.close()
def scan_port_range():
    target = input("Host: ")
    try:
        starting_port = int(input("Starting Port: \n"))
        end_port = int(input("Ending port: \n"))
        if starting_port > end_port:
            print("The starting port has to be less than or equal to the end port\n")
            return
    except ValueError:
        print("Please enter a valid port number")
        return
    
    
    
    for port in range(starting_port, end_port + 1):
        print(f"\rScanning port {port}...", end="", flush=True)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"\n✅ {port} OPEN")

        sock.close()

    print("\nScan complete!")