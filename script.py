import os 
import shutil

src_folder= './rabraw/certificates/all'

for i in range(1,18):
    folderr_name = f'./rabraw/certificates/{i}'
    os.makedirs(folderr_name)

file_count = 0
folder_index = 1

for filename in os.listdir(src_folder) :
    src_file_path = os.path.join(src_folder, filename)
    dest_folder = f'./rabraw/certificates/{folder_index}'

    shutil.move(src_file_path, dest_folder)
    print(f'Moved {src_file_path} to folder {dest_folder}')

    file_count += 1

    if file_count >= 999 :
        file_count = 0
        folder_index += 1

print('Done')