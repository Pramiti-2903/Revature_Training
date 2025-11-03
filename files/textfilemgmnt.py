
import os

def create_file(filename):
    with open(filename, "w") as file:
        pass
    print(f"File '{filename}' created.")


def write_file(filename, content, append=False):
    mode = "a" if append else "w"
    with open(filename, mode) as file:
        file.write(content + "\n")
    action = "Appended to" if append else "Written to"
    print(f"{action} '{filename}'.")


def read_file(filename):
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist.")
        return
    with open(filename, "r") as file:
        print(f"Contents of '{filename}':")
        for line in file:
            print(line.strip())


def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted.")
    else:
        print(f"File '{filename}' not found.")


if __name__ == "__main__":
    filename = "sample.txt"

    create_file(filename)
    write_file(filename, "Hello ! This is line 1.")
    write_file(filename, "This is line 2.", append=True)
    read_file(filename)
    # delete_file(filename)
