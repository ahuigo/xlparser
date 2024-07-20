import os
from subprocess import getstatusoutput

def testCliFail():
    code, msg = getstatusoutput('./xlparser/cli.py ./1.log')
    assert code>0, "need to return error code"
    assert '1.log' in msg, "require unsupported msg aboult 1.log"
