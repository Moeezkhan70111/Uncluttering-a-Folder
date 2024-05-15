import os

def rename_files(folder_name, file_type):
    try:
        i = 1
        files = os.listdir(folder_name)
        for file in files:
            if file.endswith(file_type):
                os.rename(f"{folder_name}/{file}", f"{folder_name}/{i}{file_type}")
                i += 1
    except FileNotFoundError:
        print("Folder not found.")

print("\t\tUncluttering Folder by Renaming and Organizing\n")
print("Which type of Files you want to unclutter?\n")
file_types = [".img", ".pdf", ".txt", ".py", ".jpg", ".png", ".webp", ".jpeg", ".mp3", ".mp4", ".exe", ".zip", ".rar", ".aac"]

for index, file_type in enumerate(file_types, start=1):
    print(f"{index}- {file_type}")

inp = int(input("Enter Your Choice Please: "))

print("Please Put Your Folder Name: ")
folder_name = input()

if inp >= 1 and inp <= len(file_types):
    file_extension = file_types[inp - 1]
    rename_files(folder_name, file_extension)
else:
    print("Invalid Input")
