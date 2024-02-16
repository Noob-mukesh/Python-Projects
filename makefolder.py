import os


start_day = 2
end_day = 102


for day_num in range(start_day, end_day+1):
    dir_name = f"Day{day_num}"
    os.makedirs(dir_name, exist_ok=True)
    with open(f"{dir_name}/{dir_name}.py", "w") as readme_file:
        readme_file.write("""#Credits to Mukesh
# GitHub: @noob-mukesh
# Telegram: @mr_sukkun""")
    
    with open(f"{dir_name}/README.md", "w") as readme_file:
        readme_file.write("""<!-- # Credits to Mukesh
# GitHub: @noob-mukesh
# Telegram: @mr_sukkun
-->""")
    

print("Directories created with README.md and Day.py files in each folder.")
