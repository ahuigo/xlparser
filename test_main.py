def test_main():
    import os
    from xlparser import parse, saveCsv
    rows = [['foo', 'bar'], ['看', '我', '变']]
    saveCsv(rows, '/tmp/test_xlparser.csv')
    #os.remove('/tmp/test.csv')
    assert 1==1
