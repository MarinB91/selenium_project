from data_functions import short_intro

import os
import csv


def folder():
    """Checks if folder for saving data exists, creates if not. Returns constructed path to the folder"""
    user = os.getlogin()
    path = os.path.join('C:/Users', user, 'headlines_tracker')
    if not os.path.exists(path):
        os.mkdir(path)
    return path


def file(data):
    """Checks if first time saving scraped data. If so, creates CSV file and adds headers. If not, appends existing."""
    path = folder()
    summary = short_intro(data)
    os.chdir(path)
    inner_path = path + '/headlines.csv'
    if not os.path.exists(inner_path):
        with open('headlines.csv', 'w', newline='') as csv_file:
            new_csv_file = csv.writer(csv_file)
            new_csv_file.writerow(['Title', 'Author', 'Short_Summary'])
            new_csv_file.writerow([data[0:2], summary])
    else:
        with open('headlines.csv', 'a', newline='') as csv_file:
            updated_csv_file = csv.writer(csv_file)
            updated_csv_file.writerow([data[0], data[1], summary])
