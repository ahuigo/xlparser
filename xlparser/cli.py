#!/usr/bin/env python3
import click
import sys
import os
import json
from sys import argv
from xlparser import *

if len(argv) <= 1:
    quit("xlparser --help")

if '-d' in argv:
    debug = print
else:
    debug = lambda *arg: 1


@click.command()
@click.option('-h', is_flag=True, help='Print help usage')
@click.option('-d', is_flag=True, help='Debug mode')
@click.argument('args', nargs=-1)
def main(args, **kw):
    """
    Usage: 
        xlparser [options] <src_file> [<out_file>]\n
            options:\n
                -h       For help.\n
        # From xlsx to csv.\n
        $ xlparser source.xlsx new.csv \n

        # From csv to xlsx.\n
        $ xlparser source.csv new.xlsx \n

        # From csv to json.\n
        $ xlparser source.csv new.json\n

        # From csv to stdout.\n
        $ xlparser source.xlsx | head \n
    """
    if 'h' in kw and kw['h']:
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        ctx.exit()
    if len(args)<=1:
        args = args[0],'-'
    file, outfile, *_ = args
    try:
        rows = parse(file)
        debug(f'Convert xlsx from {argv[1]}')
    except BaseException as e:
        if kw['d']:
            raise e
        else:
            sys.stderr.write(f'\033[41m{e}!\033[0m\n')
        quit(1)

    if outfile.endswith('.json'):
        json.dump(list(rows), open(outfile,'w'), ensure_ascii=False)
    elif outfile.endswith('.xlsx'):
        saveXlsx(rows, outfile)
    else:
        if outfile == '-': 
            outfile = sys.stdout
        saveCsv(rows, outfile)
    sys.stderr.write('\033[94m Done!\033[0m\n')

if __name__ == '__main__':
    main()
