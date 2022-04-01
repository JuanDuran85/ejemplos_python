"""_summary_

    Working with libraries argparse, os, and collections

    Library argparse: The argparse module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. (https://docs.python.org/3/library/argparse.html)

"""

import argparse
import os
from collections import ChainMap

def main() -> None:
    app_defaults: dict = {
        'username':'admin',
        'password':'1234'
    }

    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username')
    parser.add_argument('-p', '--password')
    args = parser.parse_args()
    
    command_line_arguments: dict = {'key': value for _,value in vars(args).items() if value}
    chain: ChainMap = ChainMap(command_line_arguments, os.environ, app_defaults)
    print(chain['username'])
    
if __name__ == '__main__':
    main()
    os.environ['username'] = 'test'
    main()