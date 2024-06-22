def write_file(file_name: str, file_content: str):
    """Write file_content to file_name with.txt extension."""
    with open(f"{file_name}.txt", "w") as f:
        f.write(file_content)

def append_file(file_name: str, file_content: str):
    """Append file_content to file_name with.txt extension."""
    with open(f"{file_name}.txt", "a") as f:
        f.write(file_content)

def read_file(file_name: str):
    """Read file_name with.txt extension and return content."""
    with open(f"{file_name}.txt", "r") as f:
        file_content = f.read()
    return file_content

# Example usage
write_file(file_name="logfile", file_content="Log 1: 5 bananas added")
append_file(file_name="logfile", file_content="Log 2: 3 bananas subtracted")

print(read_file(file_name="logfile"))
# Output:
# Log 1: 5 bananas added
# Log 2: 3 bananas subtracted