import re

def get_current_version():
    with open('version.txt', 'r') as file:
        return file.read().strip()

def update_version(version, commit_messages):
    # Define regular expressions to match MAJOR, MINOR, and PATCH changes
    major_regex = re.compile(r'^\s*feat:|^BREAKING CHANGE', re.IGNORECASE)
    minor_regex = re.compile(r'^\s*feat:', re.IGNORECASE)
    patch_regex = re.compile(r'^\s*fix:', re.IGNORECASE)

    for commit_message in commit_messages:
        if major_regex.search(commit_message):
            version = bump_major(version)
        elif minor_regex.search(commit_message):
            version = bump_minor(version)
        elif patch_regex.search(commit_message):
            version = bump_patch(version)

    return version

def bump_major(version):
    major, minor, patch = map(int, version.split('.'))
    return f"{major + 1}.0.0"

def bump_minor(version):
    major, minor, patch = map(int, version.split('.'))
    return f"{major}.{minor + 1}.0"

def bump_patch(version):
    major, minor, patch = map(int, version.split('.'))
    return f"{major}.{minor}.{patch + 1}"

def main():
    current_version = get_current_version()
    commit_messages = [
        "feat: Add new feature XYZ",
        "fix: Fix issue ABC",
        "docs: Update documentation for XYZ"
        # Replace this list with the actual commit messages from your Git repository
    ]
    new_version = update_version(current_version, commit_messages)

    with open('version.txt', 'w') as file:
        file.write(new_version)

if __name__ == "__main__":
    main()



