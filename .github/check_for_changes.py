import os
import subprocess
import sys


def main():
    base_ref = os.environ.get('GITHUB_BASE_REF')
    head_ref = os.environ.get('GITHUB_HEAD_REF')
    print(f"Base ref {base_ref}")
    print(f"Head ref {head_ref}")
    # Debug: Check the current working directory
    current_dir = os.getcwd()
    print(f"Current working directory: {current_dir}")

    # Debug: Check the contents of the current directory
    contents = os.listdir(current_dir)
    print(f"Contents of current directory: {contents}")

    # Debug: List all files and directories recursively from the current directory
    # for root, dirs, files in os.walk(current_dir):
    #     for name in dirs:
    #         print(f"Directory: {os.path.join(root, name)}")
    #     for name in files:
    #         print(f"File: {os.path.join(root, name)}")

    contents2 = os.listdir('/home/runner/work/auto-pts/auto-pts/autopts')
    print(f"Check another directory: {contents2}")

    # Check if the target directory exists
    if not os.path.exists('autopts/wid/'):
        print("Target directory 'autopts/wid/' does not exist.")
        return

    try:
        result = subprocess.run(
            ['git', 'diff', '--name-only', head_ref, base_ref, '--', 'autopts/wid/'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True
        )
        result2 = subprocess.run(
            ['git', 'status'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True
        )
        print(f"git  status output: {result2}")
        # Debug: Print the result of the git diff command
        print(f"git diff output: {result.stdout}")
        changed_files = result.stdout.strip().split('\n')
    except subprocess.CalledProcessError as e:
        print(f"Error running git diff: {e.stderr}")
        changed_files = []

    # Check if the target directory exists
    if not changed_files or all(file == '' for file in changed_files):
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
