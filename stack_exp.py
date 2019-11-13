from stack import Stack

def infix_to_postfix(infixexp):
    return None






def eval_postfix(str):
# postfix 계산하기
# 이미 postfix로 변환된 값을 계산만 하면 됨
    return None

def expr_test(infix):
    postfix = infix_to_postfix(infix)
    result = eval_postfix(postfix)
    print("'%s' => '%s' = %f" % (infix, postfix, result))


if __name__ == '__main__':
    expr_test("4 + 3 - 2")
    expr_test("4 + 3 - 4 / 2")
    expr_test("1 + 2 * 3 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )")
    expr_test("( 1 + 2 ) * 3 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )")
    expr_test("( 3 + 5 * 2 ) * ( 3 - 1 )")

# 실행 결과: 
# '4 + 3 - 2' = > '4 3 + 2 -' = 5.000000
# '4 + 3 - 4 / 2' = > '4 3 + 4 2 / -' = 5.000000
# '1 + 2 * 3 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )' = > '1 2 3 * + 4 2 4 5 2 + - / * -' = 9.666667
# '( 1 + 2 ) * 3 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )' = > '1 2 + 3 * 4 2 4 5 2 + - / * -' = 11.666667
