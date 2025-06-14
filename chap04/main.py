from expression_evaluator import ExpressionEvaluator


def main() -> None:
    evaluator = ExpressionEvaluator()

    infix1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
    infix2 = ['1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']

    postfix1 = evaluator.infix_2_postfix(infix1)
    postfix2 = evaluator.infix_2_postfix(infix2)

    result1 = evaluator.eval_post_fix(postfix1)
    result2 = evaluator.eval_post_fix(postfix2)

    print(f'중위표기: {infix1}')
    print(f'후위표기: {postfix1}')
    print(f'계산 결과: {result1}')
    print()
    print(f'중위표기: {" ".join(infix2)}')
    print(f'후위표기: {" ".join(postfix2)}')
    print(f'계산 결과: {result2}')


if __name__ == '__main__':
    main()
