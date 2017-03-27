import json
import csv
import sys


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    attr_table = []
    point_table = []
    with open('nba.csv', 'r') as input_file:
        csv_reader = csv.reader(input_file)
        for index, line in enumerate(csv_reader):
            if index == 0:
                for attribute_name in line:
                    attribute = {}
                    attribute['name'] = attribute_name
                    if attribute_name == 'pf' or attribute_name == 'turnover':
                        attribute['order'] = 'ascending'
                    else:
                        attribute['order'] = 'descending'
                    attr_table.append(attribute)
            else:
                if index == 1:
                    for attr_index, attr_value in enumerate(line):
                        if isfloat(attr_value) and attr_table[attr_index]['name'] != 'year':
                            attr_table[attr_index]['type'] = 'ordinal'
                            attr_table[attr_index]['maxValue'] = -sys.maxint - 1
                        else:
                            attr_table[attr_index]['type'] = 'nominal'
                point = {}
                for attr_index, attr_value in enumerate(line):
                    if attr_table[attr_index]['type'] == 'ordinal':
                        if attr_value.isdigit():
                            point[attr_table[attr_index]['name']] = int(attr_value)
                        else:
                            print attr_index, attr_value, attr_table[attr_index]
                            point[attr_table[attr_index]['name']] = float(attr_value)
                        attr_table[attr_index]['maxValue'] = max(attr_table[attr_index]['maxValue'], point[attr_table[attr_index]['name']])
                    else:
                        point[attr_table[attr_index]['name']] = attr_value
                point_table.append(point)
        res = {}
        res['attributeTable'] = attr_table
        res['pointTable'] = point_table
        with open('nba.json', 'w') as output_file:
            json.dump(res, output_file)
