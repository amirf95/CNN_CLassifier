import os
import random
import shutil

# ===== CONFIG =====
SOURCE_FOLDER = r"C:\Users\amirf\OneDrive\Desktop\datasets\Dataset_reorg\Train\other_mosquito"
DEST_FOLDER = r"C:\Users\amirf\Downloads\dataset\non-culex"
NUM_IMAGES = 245
EXTENSIONS = ('.png', '.jpg', '.jpeg')

# ==================

# Create destination folder if it doesn't exist
os.makedirs(DEST_FOLDER, exist_ok=True)

# Get all image files
images = [
    f for f in os.listdir(SOURCE_FOLDER)
    if f.lower().endswith(EXTENSIONS)
]

# Safety check
if len(images) < NUM_IMAGES:
    raise ValueError(f"Not enough images! Found {len(images)} images.")

# Randomly select images
selected_images = random.sample(images, NUM_IMAGES)

# Copy images
for img in selected_images:
    src_path = os.path.join(SOURCE_FOLDER, img)
    dst_path = os.path.join(DEST_FOLDER, img)
    shutil.copy2(src_path, dst_path)

print(f"✅ Copied {NUM_IMAGES} images to '{DEST_FOLDER}'")
