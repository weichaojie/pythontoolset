import os
import shutil
import time

# search_walk_path = "D:\\My Documents\\下载"
search_walk_path = "C:\codes\webtoolset"
target_save_path = "C:\\temp"
# search_file_type = '.rmvb'
search_file_type = '.html'
sleep_time = 180
global_files_list = ["", ""]


def walk(path):
    global_files_list.clear()
    if not os.path.exists(path):
        return -1
    for root, dirs, names in os.walk(path):
        for filename in names:
            if os.path.splitext(filename)[1] == search_file_type:
                # 路径和文件名连接构成完整路径
                full_file_path = os.path.join(root, filename)
                # 将符合条件的文件的全路径记录保存起来
                global_files_list.append((full_file_path, filename))
                print(full_file_path, filename)


def move_files_to_directory(path_name_list, target_directory):
    for (fullpath, name) in path_name_list:
        new_file_full_path = target_directory + "\\" + name
        shutil.move(fullpath, new_file_full_path)
        print(new_file_full_path)

while (1):

    # 循环遍历扫描目录
    walk(search_walk_path)
    time.sleep(2)

    if len(global_files_list) == 0:
        print("遍历目录后发现没有合适的文件后进行休眠", sleep_time, "秒，等待有文件准备好")
        time.sleep(sleep_time)
    else:
        # 有合适的文件时进行文件移动操作
        move_files_to_directory(global_files_list, target_save_path)
