import os
import csv
'''
def convert_txt_to_csv(txt_file, csv_file):
    with open(txt_file, 'r') as txt_file:
        lines = txt_file.readlines()
        rows = [line.strip().split(',') for line in lines]
        header = ['date', 'lat', 'lon', 'sog', 'cog']

        with open(csv_file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)
            writer.writerows(rows)

def convert_folder_to_csv(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        relative_path = os.path.relpath(root, input_folder)
        output_subfolder = os.path.join(output_folder, relative_path)

        if not os.path.exists(output_subfolder):
            os.makedirs(output_subfolder)

        for file in files:
            if file.endswith('.txt'):
                txt_file = os.path.join(root, file)
                csv_file = os.path.join(output_subfolder, file[:-4] + '.csv')
                convert_txt_to_csv(txt_file, csv_file)

# 指定输入文件夹和输出文件夹的路径
input_folder = 'D:/ais/parsedata'

output_folder = 'D:/ais/rawdata'

# 将输入文件夹中的txt文件转换为csv文件并保存到输出文件夹
convert_folder_to_csv(input_folder, output_folder)

'''

'''
# CSV转化
import os
import csv
from datetime import datetime

# 定义文件夹路径
folder_path = "D:/ais/rawdata"

# 获取文件夹中的所有子文件夹
subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]

# 遍历每个子文件夹
for subfolder in subfolders:
    # 获取子文件夹中的所有CSV文件
    csv_files = [f.path for f in os.scandir(subfolder) if f.is_file() and f.name.endswith(".csv")]

    # 遍历每个CSV文件
    for csv_file in csv_files:
        # 读取CSV文件
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)


        if len(rows) < 1024:
            os.remove(csv_file)
        else:

            new_rows = []
            for row in rows:
                date_str = row[0]
                try:

                    datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S")
                    new_row = [datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S").timestamp()] + row[1:5]
                    new_rows.append(new_row)
                except ValueError:

                    continue

            # 将处理后的数据写入新的CSV文件
            with open(csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(new_rows)


'''
import csv
import pandas as pd

# 定义CSV文件路径
csv_file_path = "566255000_data.csv"

# 读取CSV文件
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

# 将CSV数据加载到Pandas的DataFrame中
df = pd.DataFrame(rows)

# 检查每列的数据类型
column_types = df.dtypes

# 打印每列的数据类型
print(column_types)
