import sys

def enforce_structure(filepath):
    """
    Enforces the documentation structure on a given file.

    Args:
        filepath (str): The path to the file.
    """
    with open(filepath, 'r') as f:
        content = f.read()

    sections = {
        "## Core": False,
        "## Comparison": False,
        "## Trade-offs": False,
    }

    for line in content.splitlines():
        if line in sections:
            sections[line] = True

    with open(filepath, 'a') as f:
        for section, present in sections.items():
            if not present:
                f.write(f"\n{section}\n")

if __name__ == "__main__":
    for filepath in sys.argv[1:]:
        enforce_structure(filepath)
