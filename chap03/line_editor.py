import sys

from .ArrayList import ArrayList


def main() -> None:
    arr_list = ArrayList()
    while True:
        command = input('MENU: [i]nsert, [d]elete, [r]eplace, [p]rint, [l]oad, [s]ave, [q]uit => ')
        if command == 'i':
            pos = int(input(' Row to insert: '))
            text = input(' Insert content: ')
            arr_list.insert(pos, text)

        elif command == 'd':
            pos = int(input(' Row to delete: '))
            _ = arr_list.delete(pos)

        elif command == 'r':
            pos = int(input(' Row to replace: '))
            text = input(' Replace content: ')
            arr_list.replace(pos, text)

        elif command == 'p':
            print('Line Editor')
            for line in range(arr_list.size):
                print(f'[{line:2d}] ', end='')
                print(arr_list.get_entry(line))
            print()

        elif command == 'q':
            sys.exit()

        elif command == 'l':
            filename = './chap03/test.txt'
            with open(filename, 'r') as infile:
                for line in infile:
                    arr_list.insert(arr_list.size, line.rstrip('\n'))

        elif command == 's':
            filename = './chap03/test.txt'
            with open(filename, 'w') as outfile:
                outfile.writelines(
                    (arr_list.get_entry(i) or '') + '\n' for i in range(arr_list.size)
                )


if __name__ == '__main__':
    main()
