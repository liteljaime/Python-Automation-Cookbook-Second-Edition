import argparse
import configparser
import sys
from datetime import datetime


def main(number, other_number, output):
    result = number * other_number
    print(f'[{datetime.utcnow().isoformat()}] The result is {result}', file=output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''multiply the 2 numbers provided by config file or arguments and save it into 
        a file and show the time when was executed''', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '--config', '-c', type=argparse.FileType('r'), help='config file', default='/home/jmunoz/projects/python/automation/Python-Automation-Cookbook-Second-Edition/Chapter02/config.ini')
    parser.add_argument('-o', dest='output', type=argparse.FileType('a'),
                        help='output file', default=sys.stdout)

    args = parser.parse_args()
    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)

        args.n1 = int(config['ARGUMENTS']['n1'])
        args.n2 = int(config['ARGUMENTS']['n2'])

    main(args.n1, args.n2, args.output)
