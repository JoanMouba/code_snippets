#  Author: Joan Mouba - joan.mouba@gmail.com
#  Goal: Rename the files so that they are ordered
#  Applications: Order list of data to process/read/watch in ascending order

from pathlib import Path

target_path = Path("./files_to_rename")
file_prefix = "chap"

for file in list(target_path.glob("*.txt")):
    print(file)
    file_name_mid_text = file.stem.rsplit(" ", 2)[0]
    file_name_mid_text = file_name_mid_text.strip()
    file_num = file.stem.split()[-1][1:].zfill(2)
    file_ext = file.suffix
    new_name = f"{file_prefix} {file_num} {file_name_mid_text}{file_ext}"
    file.rename(file.with_name(new_name))
    print(f"{file.name} ==> {new_name}")
