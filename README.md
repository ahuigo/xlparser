# xlparser
Parse excel(xlsx/xls/csv) to other format(dict, csv, json, ...).

> Warning: some old versiones of xls are not supported.

## Install

    pip install xlparser
    pip3 install xlparser

## Usage

    $ xlparser

### CLI Usage
Convert xlsx to csv

    $ xlparser.py src.xlsx | tee test.csv
    foo, bar
    看,我,变

Convert csv to json

    $ xlparser.py test.csv -json | tee test.json
    [["foo", "bar"], ["看", "我", "变"]]

### Module Usage

### parse any type of file
The `parse` function support the following file format:

    def parse(src):
        if src.endswith('.xls'):
            return parseXls(src)
        if src.endswith('.xlsx'):
            return parseXlsx(src)
        if src.endswith('.csv'):
            return parseCsv(src)

`parse` any type of file to rows:

    >>> from xlparser import parse, saveCsv
    >>> rows = parse('some.xlsx')
    >>> list(rows)
    [['foo', 'bar'], ['看', '我', '变']]

Save rows to csv

    >>> saveCsv(rows, 'test.csv')

### Csv operation

    >>> from xlparser import *

    >>> rows = [('foo','bar'), ('看','我','变')]
    >>> saveCsv(rows, 'test.csv')

    >>> list(parseCsv('test.csv'))
    [['foo', 'bar'], ['看', '我', '变']]

### Zip operation

    >>> from xlparser import loadZip
    >>> zf = loadZip('test.xlsx')
    >>> print(zf.filelist)
    ......
    >>> zf.extract('xl/media/image1.png', '/tmp')
    >>> os.rename('/tmp/'+'xl/media/image1.png', './image1.png')


## Required
1. python>=3.5
2. xlrd: required by xls
2. openpyxl>=2.5.4: required by xlsx
