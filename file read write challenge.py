def read_and_modify_file():
    try:
        filename = input("Enter the name of the file to read: ")
        with open(filename, "r") as infile:
            content = infile.read()
        
        # Modify content (e.g., convert to uppercase)
        modified_content = content.upper()

        output_filename = "modified_" + filename
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file was not found.")
    except PermissionError:
        print("❌ Error: Permission denied while reading or writing the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_modify_file()
