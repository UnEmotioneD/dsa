from check_brackets import CheckBrackets
from eval_post_fix import EvalPostFix
from infix_2_postfix import Infix2Postfix


def run_check_brackets(stmt):
    checker = CheckBrackets(stmt)
    print(f'{stmt} -> {checker.check_brackets()}')


def run_infix_2_postfix(infix):
    print(f'중위표기: {" ".join(infix)}')

    postfix = Infix2Postfix(infix).infix_2_postfix()
    print(f'후위표기: {" ".join(postfix)}')

    run_eval_postfix(postfix)


def run_eval_postfix(post_fix):
    result = EvalPostFix(post_fix).eval_post_fix()
    print(f'계산 결과: {result}')


if __name__ == '__main__':
    STATEMENT_1 = '{A[(i+1)] = 0;}'
    STATEMENT_2 = 'if((i == 0) && (j == 0))'
    STATEMENT_3 = 'A[(i + 1) = 0;]'

    infix1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
    infix2 = ['1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']

    print('Check brackets.')
    print('-' * 50)
    run_check_brackets(STATEMENT_1)
    run_check_brackets(STATEMENT_2)
    run_check_brackets(STATEMENT_3)
    print()
    print('Statement to infix and evaluate.')
    print('-' * 50)
    run_infix_2_postfix(infix1)
    print()
    run_infix_2_postfix(infix2)
