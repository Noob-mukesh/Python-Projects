import os


start_day = 2
end_day = 102


# for day_num in range(start_day, end_day+1):
#     dir_name = f"Day{day_num}"
#     os.makedirs(dir_name, exist_ok=True)
#     with open(f"{dir_name}/{dir_name}.py", "w") as readme_file:
#         readme_file.write("""# GitHub: @noob-mukesh""")
    
#     with open(f"{dir_name}/README.md", "w") as readme_file:
#         readme_file.write("""<!-- GitHub: @noob-mukesh -->""")
   

# print("Directories created with README.md and Day.py files in each folder.")
# import os
# import os
# import shutil

# all_dir = os.listdir()
# for x in all_dir:
#     if x.startswith("Day") and x[3:].isdigit() and 2 <= int(x[3:]) <= 100:
#         shutil.rmtree(x)



# all_dir=os.listdir()
# for x in all_dir:
#     if x.startswith("Day") and x[3:].isdigit() and 2 <= int(x[3:]) <= 100:
#         os.rmdir(x)
# for day_num in range(start_day, end_day+1):
#     dir_name = f"Day{day_num}"
#     file_path = f"{dir_name}.py"

#     if os.path.exists(file_path):
#         os.remove(file_path)
#     else:
#         print(f"File '{file_path}' does not exist.")

