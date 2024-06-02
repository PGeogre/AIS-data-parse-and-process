import os
import csv
from datetime import datetime


def convert_txt_to_csv(txt_file, csv_file):
    with open(txt_file, 'r') as txt_file:
        lines = txt_file.readlines()

        if len(lines) < 1024:
            print(f"Skipping conversion for {txt_file}. Line count is less than 1024.")
            return  # Skip conversion


        rows = [line.strip().split(',')[:5] for line in lines]
        header = ['date', 'lat', 'lon', 'sog', 'cog']

        with open(csv_file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)

            for row in rows:
                date_str = row[0]
                timestamp = datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S').timestamp()

                processed_row = [timestamp] + [value if value else '0' for value in row[1:]]

                writer.writerow(processed_row)


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


input_folder = 'E:/ais/txt2csv/txt'

output_folder = 'E:/ais/txt2csv/csv'

convert_folder_to_csv(input_folder, output_folder)
