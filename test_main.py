from xlparser import parse, saveCsv, saveXlsx
def test_saveXlsx():
    import os
    from datetime import datetime, date as dateType

    # test list
    rows = [['foo', 'bar'], ['看', '我', '变']]
    saveCsv(rows, '/tmp/test_xlparser.csv')
    saveXlsx(rows, '/tmp/test_xlparser.xlsx')

    # test dict
    rows = [{"myname":"Alex", "myage":20}]
    saveXlsx(rows, '/tmp/test_xlparser.xlsx')

    # test datetime and json
    rows = [{"start_time":datetime.now(), "pjson":{"json":1}}, ["time", "data"], [dateType(2022,1,1)]]
    saveXlsx(rows, '/tmp/test_xlparser.xlsx')

    #os.remove('/tmp/test.csv')
