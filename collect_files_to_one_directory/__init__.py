import os
import time

target_walk_path = "D:\\My Documents\\下载"

global_files_list = []


def walk(path):
    global_files_list.clear()
    if not os.path.exists(path):
        return -1
    for root, dirs, names in os.walk(path):
        for filename in names:
            if os.path.splitext(filename)[1] == '.rmvb':
                full_file_path = os.path.join(root, filename)
                global_files_list.append(full_file_path)
                print(full_file_path)  # 路径和文件名连接构成完整路径


while (1):

    walk(target_walk_path)
    time.sleep(2)

    if len(global_files_list) == 0:
        print("休眠15秒")
        time.sleep(15)
