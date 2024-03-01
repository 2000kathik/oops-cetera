def main():
    name = get_name()
    clg = get_clg()
    print(f"{name} from {clg}")

def get_name():
    return input("name: ")

def get_clg():
    return input("clg: ")

if __name__ == "__main__":
    main()