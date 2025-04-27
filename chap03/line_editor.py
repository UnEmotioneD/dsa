import sys

from ArrayList import ArrayList


def main() -> None:
    alist = ArrayList()
    while True:
        command = input(
            'MENU: [i]nsert, [d]elete, [r]eplace, [p]rint, [l]oad, [s]ave, [q]uit => '
        )
        if command == 'i':
            pos = int(input(' Row to insert: '))
            text = input(' Insert content: ')
            alist.insert(pos, text)

        elif command == 'd':
            pos = int(input(' Row to delete: '))
            alist.delete(pos)

        elif command == 'r':
            pos = int(input(' Row to replace: '))
            text = input(' Replace content: ')
            alist.replace(pos, text)

        elif command == 'p':
            print('Line Editor')
            for line in range(alist.size):
                print('[%2d] ' % line, end='')
                print(alist.get_entry(line))
            print()

        elif command == 'q':
            sys.exit()

        elif command == 'l':
            filename = './chap03/test.txt'
            with open(filename, 'r') as infile:
                for line in infile:
                    alist.insert(alist.size, line.rstrip('\n'))

        elif command == 's':
            filename = './chap03/test.txt'
            with open(filename, 'w') as outfile:
                for i in range(alist.size):
                    outfile.write((alist.get_entry(i) or '') + '\n')


if __name__ == '__main__':
    main()
