import argparse


def main(number, character):
    print(character * number)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Print in the console the character that you want as many times as you want')
    parser.add_argument('number', type=int, help='A number')
    parser.add_argument('-c', type=str, help='A character', default='#')

    args = parser.parse_args()

    main(args.number, args.c)
