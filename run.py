import csv 
import json 

def csv_to_json(csv_file_path):
  data = []

  with open(csv_file_path, encoding='utf-8') as csv_file: 
    csv_reader = csv.DictReader(csv_file)
  
    for row in csv_reader: 
      data.append(row)

  return json.dumps(data)
  
if __name__ == '__main__':
  json_str = csv_to_json('comic_books.csv')
  print(json_str)