import os
import sys

def main():
    try:
        with open('changed_files.txt', 'r') as f:
            changed_files = f.readlines()
    except FileNotFoundError:
        print("changed_files.txt not found. No changes detected.")
        return

    # filenames = [os.path.splitext(os.path.basename(file.strip()))[0].upper() for file in changed_files]

    filenames = []

    for file in changed_files:
        stripped_file = file.strip()
        base_name = os.path.basename(stripped_file)
        name_wo_ext, ext = os.path.splitext(base_name)

        if name_wo_ext == "__init__":
            continue

        if name_wo_ext == "gatt_client":
            name_wo_ext == "gatt_cl"

        upper_name = name_wo_ext.upper()
        filenames.append(upper_name)

    with open('changed_files_formatted.txt', 'w') as f:
        f.write(' '.join(filenames))


if __name__ == "__main__":
    main()
