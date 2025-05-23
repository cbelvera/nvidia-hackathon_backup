import os

output_dir = os.path.join("data", "output")


def clean_blank_lines(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cleaned_lines = [line.rstrip() for line in lines if line.strip()]

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write('\n'.join(cleaned_lines))

    print(f"Removed blank lines in: {txt_path}")


for root, _, files in os.walk(output_dir):
    for file in files:
        if file.lower().endswith(".txt"):
            txt_path = os.path.join(root, file)
            clean_blank_lines(txt_path)

print(f"\n All blank lines removed from .txt files.")