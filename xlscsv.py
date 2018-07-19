#!/usr/local/bin/python3
import openpyxl
import csv
from sys import argv
from datetime import datetime, timedelta
from dateutil.parser import parse as strptime
__all__ = ["parseXls", 'toCsv'] 
'''
Format time
'''
def getCellValue(cell):
    debug(cell.value, type(cell.value),cell.row,cell.column,cell.data_type,cell.style, cell.style_id)
    if cell.data_type in ['xxx']: # 's'
        if type(cell.value) == str:
            d = strptime(cell.value).strftime('%Y%m%d')
        elif type(cell.value) == int:
            d = (datetime(1900,1,1)+timedelta(days=cell.value))
        else:
            d = cell.value
        value = d.strftime('%Y%m%d')
    else:
        value = cell.value
        value = cell.value.replace("\n", '\n') if type(cell.value) is str else cell.value
    return value

def isInValid(cell):
    return cell.value==None and cell.style_id in [62,64]

'''
parse xlsx, xls
'''
def parseXls(src):
    if src.endswith('.xls'):
        return parseXlsOld(src)
    wb = openpyxl.load_workbook(src)
    sh = wb.active
    #maxl = len(next(sh.rows))

    rows = []
    for r in sh.rows:
        if r[0].style_id == 64:
            continue;
        debug('---')
        row = [getCellValue(cell) for cell in r if not isInValid(cell)]
        if(any(row)):
            debug(row)
            rows.append(row)
    return rows

def parseXlsOld(src):
    from xlrd import open_workbook
    sh = open_workbook(filename).sheets()[0]
    rows = []
    for r in range(sh.nrows):
        row = [v if str(v).isdigit() else v  for v in sh.row_values(r)]
        rows.append(row)
    return rows

def toCsv(rows, dest):
    with open(dest, 'w') as f:
        c = csv.writer(f)
        [c.writerow(row) for row in rows]

if '-d' in argv:
    debug = print
else:
    debug = lambda *arg:1

if __name__ == '__main__':
    if len(argv)<3:
        print('Usage:\n$ xlsx2csv.py from.xlsx to.csv')
        quit()

    # Xls2csv
    rows = parseXls(argv[1])
    [print(row) for row in (rows)]
    debug(f'Convert xlsx from {argv[1]} to {argv[2]}' )
    #rows = toCsv(rows, argv[2])

'''
import openpyxl
import csv
from sys import argv

wb = openpyxl.load_workbook('2.xlsx', guess_types = True)
sh = wb.active
r = sh.rows[3]
a = r[0]
'''
