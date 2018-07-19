from setuptools import setup, find_packages
import re
version = "0.1.3"

version = re.sub(r'(\d+\.\d+\.)(\d+)', 
        lambda m: '%s%d' % (m.group(1), int(m.group(2))+1), 
        version,1)

setup(
    name='xlscsv',
    version = version,
    install_requires=[ ],
    packages=['.'],
    python_requires='>=3.5.3',
    scripts = ['xlscsv.py'],
    description = open('README.md').readlines()[1],
    long_description=open('README.md').read(),
    author = "ahuigo",
    author_email = "ahui132@qq.com",
    license = "MIT",
    url = "http://github.com/ahuigo/xlscsv",   
)

s = open('setup.py').read()
s = re.sub(r'(?<=\n)(version *= *")(\d+\.\d+\.)(\d+)"', 
    lambda m: 'version = "%s"' % (version),
    s,1)
open('setup.py', 'w').write(s)
