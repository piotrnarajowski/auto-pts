import os
import subprocess
import sys


def main():
    # Debug: Check the current working directory
    print(f"Current working directory: {os.getcwd()}")

    # Debug: Check the contents of the current directory
    print(f"Contents of current directory: {os.listdir(os.getcwd())}")

    try:
        result = subprocess.run(
            ['git', 'diff', '--name-only', 'HEAD^', 'HEAD', '--', 'autopts/wid/'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True
        )
        # Debug: Print the result of the git diff command
        print(f"git diff output: {result.stdout}")
        changed_files = result.stdout.strip().split('\n')
    except subprocess.CalledProcessError as e:
        print(f"Error running git diff: {e.stderr}")
        changed_files = []

    if not changed_files or changed_files == ['']:
        print("No changes detected in autopts/wid directory.")
        changed_files = []

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

        # Debug: Print the formatted filenames
    print(f"Formatted filenames: {filenames}")

    with open('changed_files_formatted.txt', 'w') as f:
        f.write(' '.join(filenames))


if __name__ == "__main__":
    main()
