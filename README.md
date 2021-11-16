- [xlparser](#xlparser)
  - [安装](#安装)
  - [使用](#使用)
    - [命令行示例](#命令行示例)
    - [python 调用示例](#python-调用示例)
    - [转任何类型的文件](#转任何类型的文件)
    - [保存任何类型的文件](#保存任何类型的文件)
    - [Csv 文件处理](#csv-文件处理)
    - [Zip 文件处理](#zip-文件处理)
  - [Required](#required)

[English](README.en.md)

# xlparser
将 excel(xlsx/xls/csv) 转到其他的格式(csv, xlsx, json).

> Warning: 如果你遇到问题，最好在issue 提交明确的报错信息。

[![](https://img.shields.io/pypi/pyversions/xlparser.svg?longCache=True)](https://pypi.org/pypi/xlparser/)
[![](https://img.shields.io/pypi/v/xlparser.svg?maxAge=36000)](https://pypi.org/pypi/xlparser/)

## 安装

    pip install xlparser

如果想过滤字段，结合[xcut](https://github.com/ahuigo/xcut) 使用更方便

    pip install xcut

## 使用

    $ xlparser -h
    xlparser [options] INFILE [OUTFILE]\n
        options:\n
            -h       For help.\n

### 命令行示例
将 xlsx 转成 csv

    $ xlparser source.xlsx new.csv 

将 csv 转成 xlsx

    $ xlparser source.csv new.xlsx 

将 csv 转成 json

    $ xlparser source.csv new.json

将 xlsx 转成 csv(标准输出)

    $ xlparser source.xlsx | head 

    $ xlparser src.xlsx | tee test.csv
    name, score
    "李雷,韩梅",15
    小花,16

xcut 命令结合

    $ xlparser src.xlsx | xcut --from-csv -f name 
    name
    "李雷,韩梅"
    小花

    $ xlparser src.xlsx | xcut --from-csv -f score,name
    score,name
    15,"李雷,韩梅"
    16,小花

### python 调用示例

#### 转任何类型的文件
`parse` any type of file to rows:

    >>> from xlparser import parse, saveCsv
    >>> rows = parse('some.xlsx')
    >>> list(rows)
    [['foo', 'bar'], ['看', '我', '变']]

The `parse` function supports the following file formats: .csv, .xls, .xlsx .

#### 保存任何类型的文件
Save rows to csv

    >>> from xlparser import parse, saveCsv
    >>> rows = [['foo', 'bar'], ['看', '我', '变']]
    >>> saveCsv(rows, 'test.csv')

Save rows to xlsx

    >>> saveXlsx(rows, 'test.xlsx')

#### Csv 文件处理

    >>> from xlparser import *

    >>> rows = [('foo','bar'), ('看','我','变')]
    >>> saveCsv(rows, 'test.csv')

    >>> list(parseCsv('test.csv'))
    [['foo', 'bar'], ['看', '我', '变']]

#### Zip 文件处理

    >>> from xlparser import loadZip
    >>> zf = loadZip('test.xlsx')
    >>> print(zf.filelist)
    ......
    >>> zf.extract('xl/media/image1.png', '/tmp')
    >>> os.rename('/tmp/'+'xl/media/image1.png', './image1.png')

### Required
1. python>=3.5
2. xlrd: required by xls
2. openpyxl>=2.5.4: required by xlsx
