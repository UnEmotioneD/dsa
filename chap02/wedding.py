"""
Chapter 02
page 57

---

input()
"""


def main() -> None:
    groom: str = input('신랑의 이름을 입력하세요: ')
    bride: str = input('신부의 이름을 입력하세요: ')

    print(f'신랑 {groom} 와 신부 {bride} 의 결혼을 축하 합니다')


if __name__ == '__main__':
    main()
