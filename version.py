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
            version = bump_major(
