from PIL import Image, ImageEnhance, ImageFilter
import os

img = r"C:\Users\LENOVO\OneDrive\Pictures"

files = os.listdir(img)

for file in files:
    if file.endswith((".jpg", ".jpeg", ".png")):
        file_path = os.path.join(img, file)
        try:
            with Image.open(file_path) as image:
                # Enhance the image
                enhancer = ImageEnhance.Contrast(image)
                enhanced_image = enhancer.enhance(1.5)  # Increase contrast by 50%
                
                # Apply a filter
                filtered_image = enhanced_image.filter(ImageFilter.SHARPEN)
                
                # Save the edited image
                # Overwrite the original file
                filtered_image.save(file_path)
                print(f"✅ Edited {file}")
                
        except Exception as e:
            print(f"❌ Error processing {file}: {e}")