from xlparser import parse, saveCsv, saveXlsx
from dateutil.parser import parse as parsetime
from datetime import datetime, date as dateType, timedelta
import os

def isCloseTime(t1:datetime, t2:datetime, tol=timedelta(milliseconds=1)):
    return abs(t1-t2)<=tol

def test_saveXlsx():

    # test list
    rows = [['foo', 'bar'], ['看', '我', '变']]
    saveCsv(rows, '/tmp/test_xlparser.csv')
    saveXlsx(rows, '/tmp/test_xlparser.xlsx')
    v = list(parse('/tmp/test_xlparser.xlsx'))[0][0]
    assert v == 'foo'

    # test dict
    rows = [{"myname":"Alex", "myage":20}]
    saveXlsx(rows, '/tmp/test_xlparser.xlsx')

    # test datetime and json
    rows = [{"start_time":datetime.now(), "pjson":{"json":1}}, ["time", "data"], [dateType(2022,1,1)]]
    saveXlsx(rows, '/tmp/test_xlparser.xlsx')
    newrow = list(parse('/tmp/test_xlparser.xlsx'))[1]
    assert isCloseTime(parsetime(newrow[0]), rows[0]['start_time'])

    # test datetime and json
    rows = [[1,23]]
    saveXlsx(rows, '/tmp/test_xlparser.xlsx')
    assert list(parse('/tmp/test_xlparser.xlsx'))[0][1] == rows[0][1]
    #os.remove('/tmp/test.csv')


def testParseEmptyXlsx():
    saveXlsx([], '/tmp/test_xlparser.xlsx')
    assert len(list(parse('/tmp/test_xlparser.xlsx'))) == 0
    
def testParseMergedXlsx():
    assert len(list(parse('./testdata/merged.xlsx'))) > 0


def testUnsupportedFile():
    try:
        parse('./1.log') 
    except Exception as e:
        msg = e.__str__()
        assert '1.log' in msg, "require unsupported msg aboult 1.log"
