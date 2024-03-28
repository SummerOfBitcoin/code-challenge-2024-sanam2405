def generate_output():

    # File path
    file_path = "../output.txt"

    # Writing content into the file (overwriting if it already exists)
    with open(file_path, "w") as file:
        # file.write()
        pass


def main():
    print("Hello SoB! I am Manas!")
    generate_output()


if __name__ == "__main__":
    main()
