# xlparser
Parse excel(xlsx/xls/csv) to other format(csv, xlsx, json).

> Warning: some old versions of xls are not supported.

[![](https://img.shields.io/pypi/pyversions/xlparser.svg?longCache=True)](https://pypi.org/pypi/xlparser/)
[![](https://img.shields.io/pypi/v/xlparser.svg?maxAge=36000)](https://pypi.org/pypi/xlparser/)

## Install

    pip install xlparser
    pip3 install xlparser

## Usage

    $ xlparser -h
    xlparser [options] INFILE [OUTFILE]\n
        options:\n
            -h       For help.\n

Examples:

        # From xlsx to csv.\n
        $ xlparser source.xlsx new.csv \n

        # From csv to xlsx.\n
        $ xlparser source.csv new.xlsx \n

        # From csv to json.\n
        $ xlparser source.csv new.json\n

        # From xlsx to stdout.\n
        $ xlparser source.xlsx | head \n

        $ xlparser src.xlsx | tee test.csv
        name, score
        "李雷,韩梅",15
        小花,16

        $ xlparser src.xlsx | xcut --from-csv -f name 
        name
        "李雷,韩梅"
        小花
        $ xlparser src.xlsx | xcut --from-csv -f score,name
        score,name
        15,"李雷,韩梅"
        16,小花

### CLI Usage
Convert xlsx to csv

    $ xlparser src.xlsx test.csv; 
    $ cat test.csv
    name, age
    李雷,15
    小花,16

Convert csv to json

    $ xlparser test.csv test.json
    [["name", "age"], ["李雷", "15"], ["小花", "16"]]

### Module Usage

### Parse any type of file
`parse` any type of file to rows:

    >>> from xlparser import parse, saveCsv
    >>> rows = parse('some.xlsx')
    >>> list(rows)
    [['foo', 'bar'], ['看', '我', '变']]

The `parse` function supports the following file formats: .csv, .xls, .xlsx .

### Save to any type of file
Save rows to csv

    >>> saveCsv(rows, 'test.csv')

Save rows to xlsx

    >>> saveXlsx(rows, 'test.xlsx')

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
