import os

# Folder to check
output_dir = os.path.join("data", "output")

files_checked = 0
files_with_blanks = 0

for root, _, files in os.walk(output_dir):
    for file in files:
        if file.lower().endswith(".txt"):
            txt_path = os.path.join(root, file)
            
            with open(txt_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            has_blank_lines = any(not line.strip() for line in lines)

            files_checked += 1
            if has_blank_lines:
                files_with_blanks += 1
                print(f"❗ Blank lines found in: {txt_path}")
            else:
                print(f"✅ No blank lines: {txt_path}")

print(f"\n🔍 Checked {files_checked} .txt files.")
print(f"🧹 Files with blank lines: {files_with_blanks}")