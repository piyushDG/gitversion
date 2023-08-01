import re

def get_current_version():
    with open('version.txt', 'r') as file:
        return file.read().strip()

def update_version(version, commit_messages):
    # Define your rules or keywords to identify MAJOR, MINOR, or PATCH changes
    major_keywords = ['feat', 'BREAKING CHANGE']
    minor_keywords = ['feat']
    patch_keywords = ['fix']

    for commit_message in commit_messages:
        if any(keyword in commit_message for keyword in major_keywords):
            version = bump_major(version)
        elif any(keyword in commit_message for keyword in minor_keywords):
            version = bump_minor(version)
        elif any(keyword in commit_message for keyword in patch_keywords):
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


