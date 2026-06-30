from Scanner.Port_Scanner import scan_single_port, scan_port_range
print("Welcome to my Python security toolkit")

def menu():
    print("\n" + "=" * 40)
    print("      Python Security Toolkit")
    print("=" * 40)
    print("1. Scan a Single Port")
    print("2.Scan multiple ports")
    print("3. Exit")
    print("=" * 40)


def main():
    while True:
        menu()
        choice = input("Select an option:")

        if choice == "1":
            try:
                scan_single_port()
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            scan_port_range()
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Not a valid option")

if __name__ == "__main__":
    main()