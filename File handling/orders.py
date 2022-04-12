def open_and_print(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file.readlines():
                print(line.rstrip('\n'))

    except FileNotFoundError:
        print("File not found")
        raise

    finally:
        print("\nComplete")


def write_to_file(file_name, order_item):
    try:
        with open(file_name, 'a') as file:
            file.write(f"{order_item}\n")

    except FileNotFoundError:
        print("File not found.")
        raise


if __name__ == "__main__":
    # open_and_print("order.txt")
    # open_and_print("details.txt")
    write_to_file("order.txt", "testing again")
