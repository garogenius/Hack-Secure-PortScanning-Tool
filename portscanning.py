import socket

class PortScanner:
    def __init__(self, target_ip, start_port, end_port):
        self.target_ip = target_ip
        self.start_port = start_port
        self.end_port = end_port

    def validate_inputs(self):
        """Validate the IP address and port range."""
        try:
            # Validate IP address
            socket.inet_aton(self.target_ip)
            # Validate port range
            if not (1 <= self.start_port <= 65535 and 1 <= self.end_port <= 65535):
                raise ValueError("Ports must be in the range 1-65535.")
            if self.start_port > self.end_port:
                raise ValueError("Start port must be less than or equal to end port.")
            return True
        except socket.error:
            raise ValueError("Invalid IP address.")
        except ValueError as e:
            raise ValueError(e)

    def scan_ports(self):
        """Scan the target IP for open ports in the specified range."""
        open_ports = []
        for port in range(self.start_port, self.end_port + 1):
            try:
                # Create a socket object
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)  # Set timeout to avoid hanging
                # Attempt to connect to the port
                result = sock.connect_ex((self.target_ip, port))
                if result == 0:
                    open_ports.append(port)
                sock.close()
            except socket.error:
                continue
        return open_ports

    def display_results(self, open_ports):
        """Display the results of the port scan."""
        if open_ports:
            print(f"Open ports on {self.target_ip}:")
            for port in open_ports:
                print(f"Port {port} is open.")
        else:
            print(f"No open ports found on {self.target_ip} in the range {self.start_port}-{self.end_port}.")

def main():
    print("Basic Port Scanner")
    try:
        # Get user input
        target_ip = input("Enter the target IP address: ")
        start_port = int(input("Enter the start port: "))
        end_port = int(input("Enter the end port: "))

        # Initialize the scanner
        scanner = PortScanner(target_ip, start_port, end_port)

        # Validate inputs
        if scanner.validate_inputs():
            # Scan ports
            open_ports = scanner.scan_ports()
            # Display results
            scanner.display_results(open_ports)
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")

if __name__ == "__main__":
    main()