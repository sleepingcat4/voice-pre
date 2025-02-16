import os
import shutil
import hashlib

src_dir = "/storage/voice/voices"
dest_dir = "/storage/voice/rname-voice"

os.makedirs(dest_dir, exist_ok=True)

count = 0

for folder in os.listdir(src_dir):
    folder_path = os.path.join(src_dir, folder)
    
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith(".mp3"):
                new_filename = f"{folder}_{file}"
                hash_value = hashlib.sha256(new_filename.encode()).hexdigest() + ".mp3"
                src_file = os.path.join(folder_path, file)
                dest_file = os.path.join(dest_dir, hash_value)
                
                shutil.copy2(src_file, dest_file)
                print(f"Copied: {file} → {hash_value}")
                
                count += 1

print(f"Total copied: {count}")
