import sys

# Define the canonical order of sections
REQUIRED_SECTIONS = [
    "## Core",
    "## Characteristics",
    "## Comparison",
    "## Trade-offs",
]

def enforce_structure(filepath):
    """
    Enforces the documentation structure on a given file,
    including the correct order of sections.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return

    # Store the content of each section found in the file
    found_sections = {}
    current_section_title = None
    current_section_content = []

    # Preserve content before the first recognized section (e.g., the H1 title)
    header_content = []

    lines = content.splitlines()
    first_section_found = False

    for line in lines:
        stripped_line = line.strip()
        is_section_header = stripped_line in REQUIRED_SECTIONS

        if is_section_header:
            if not first_section_found:
                first_section_found = True

            # If we were parsing a section, save its content before starting a new one
            if current_section_title:
                found_sections[current_section_title] = "\n".join(current_section_content).strip()

            # Start the new section
            current_section_title = stripped_line
            current_section_content = []
        else:
            if current_section_title:
                current_section_content.append(line)
            elif not first_section_found:
                header_content.append(line)

    # Save the content of the last section after the loop finishes
    if current_section_title:
        found_sections[current_section_title] = "\n".join(current_section_content).strip()

    # Reconstruct the file with sections in the correct order
    with open(filepath, 'w', encoding='utf-8') as f:
        # Write the header content (everything before the first section)
        if header_content:
            f.write("\n".join(header_content).strip())
            f.write("\n\n")

        # Write each required section and its content, in the correct order
        for section_title in REQUIRED_SECTIONS:
            f.write(f"{section_title}\n")

            section_content = found_sections.get(section_title, "")

            if section_content:
                f.write(f"\n{section_content}\n\n")
            else:
                # Add a blank line for empty sections to keep spacing consistent
                f.write("\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python enforce_structure.py <file1> <file2> ...")
    else:
        for filepath in sys.argv[1:]:
            enforce_structure(filepath)
