'''Write a script that prompts the user for:

A file_name where it should write the content.
The content that should go in the file. The script should keep accepting lines of text until the user enters an empty line.
After the user enters an empty line, write all of the lines to the file and end the script. '''

#!/usr/bin/env python3.6

def get_file_name(reprompt=False):
    if reprompt:
        print("Please enter a file name.")

    file_name = input("Destination file name: ").strip()
    return file_name or get_file_name(True)

file_name = get_file_name()

print(f"Please enter your content. Entering an empty line will write the content to {file_name}:\n")

with open(file_name, 'w') as f:
    eof = False
    lines = []

    while not eof:
        line = input()
        if line.strip():
            lines.append(f"{line}\n")
        else:
            eof = True

    f.writelines(lines)
    print(f"Lines written to {file_name}")
