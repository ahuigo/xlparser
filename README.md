# Xlscsv
Convert xlsx/xls to csv

## Install

    pip install xlscsv
    pip3 install xlscsv

## Usage
### CLI Usage

    $ xlscsv.py src.xlsx dest.csv

### Module Usage

    from xlscsv import parseXls, toCsv

    rows = parseXls('some.xlsx')
    toCsv(rows, 'to.csv')

## Required
1. python>=3.5
2. xlrd: required by xls
2. openpyxl: required by xlsx
