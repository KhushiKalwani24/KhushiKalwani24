from datetime import datetime

readme_path = "README.md"

# Load README
with open(readme_path, "r", encoding="utf-8") as f:
    readme = f.read()

# Replace placeholder text with updated info
new_readme = readme.replace(
    "<!--STATS-->", 
    f"⏳ Last updated on {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC"
)

# Save back
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(new_readme)
