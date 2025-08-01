# `os` is used for interacting with the operating system
# `shutil` is used for moving files and directories (shell utilities)
import os
import shutil
from PIL import Image, ImageEnhance, ImageFilter

user_path = r"C:\Users\LENOVO\Downloads"

# Here, the `r` prefix is used to treat the string as a raw string literal, 
# which is useful for Windows paths.
pdf = r"C:\Users\LENOVO\OneDrive\Documents\PDF"
txt = r"C:\Users\LENOVO\OneDrive\Documents\Text"
word = r"C:\Users\LENOVO\OneDrive\Documents\Word"
img = r"C:\Users\LENOVO\OneDrive\Pictures"
video = r"C:\Users\LENOVO\Videos"
music = r"C:\Users\LENOVO\Music"

# List all files in the user-specified directory
files = os.listdir(user_path)

def moving_directory(destination):
    global file, user_path, destination_path
    
    # Construct the full path for the source and destination
    # by joining the user path with the file name
    source_path = os.path.join(user_path, file)
    destination_path = os.path.join(destination, file)

    try:
        shutil.move(source_path, destination_path)
        print(f"\n{source_path} → {destination_path}")
        print(f"✅ Moved {file} to {destination}")
    except PermissionError:
        print(f"❌ Permission denied: {source_path}. Close the file and try again.")
    except FileNotFoundError:
        print(f"❌ File not found: {source_path} or {destination_path}")
    except Exception as e:
        print(f"❌ Unexpected error with {file}: {e}")

for file in files:
    if file.endswith(".pdf"):
        moving_directory(pdf)

    elif file.endswith(".txt"):
        moving_directory(txt)

    elif file.endswith(".docx") or file.endswith(".doc"):
        moving_directory(word)

    elif file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        moving_directory(img)

        user_command = input(f"\nDo you want to edit {file}? (yes/no): ").strip().lower()

        if user_command == 'yes':
            try:
                with Image.open(destination_path) as image:
                    corrected_image = image.convert("RGBA")

                    # Enhance the image
                    enhancer = ImageEnhance.Contrast(corrected_image)
                    enhanced_image = enhancer.enhance(1.5)  # Increase contrast by 50%
                        
                    # Apply a filter
                    filtered_image = enhanced_image.filter(ImageFilter.SHARPEN)
                        
                    # Save the edited image
                    # Overwrite the original file
                    filtered_image.save(destination_path)
                    print(f"✅ Edited {file}")
            except Exception as e:
                print(f"❌ Error processing {file}: {e}")
        elif user_command == 'no':
            print(f"Skipping edit for {file}.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    elif file.endswith(".mp4") or file.endswith(".mkv"):
        moving_directory(video)

    elif file.endswith(".mp3") or file.endswith(".wav"):
        moving_directory(music)