import os
import subprocess
import sys


def run_cmd(cmd: str) -> list[str]:
    out = subprocess.check_output(cmd, text=True, shell=True)
    return out.splitlines()


def main():
    # Check if the target directory exists
    if not os.path.exists('autopts/wid/'):
        print("Target directory 'autopts/wid/' does not exist.")
        return

    try:
        if len(sys.argv) > 1:
            commit = sys.argv[1]
        else:
            commit = 'HEAD'
        if len(sys.argv) > 2:
            upstream = sys.argv[2]
        else:
            upstream = 'origin/master'
        mb = run_cmd(f"git merge-base {upstream} {commit}")
        upstream = mb[0]

        result = subprocess.run(
            ['git', 'diff', '--name-only', upstream, commit, '--', 'autopts/wid/'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True
        )

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
