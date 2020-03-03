def solution(array):

    soloNumber = 0

    for number in array:

        soloNumber = soloNumber ^ number

    return soloNumber


res = solution([1,2,3,4,3,2,1])

print(res)


'''
    Give a array of number, there aways
    a pair of same numbers, except for one
    find the except.

    But the memory must be constant
    and the complexity must be O(n)


    example:

    [1,2,3,2,1] => 3

    [1,2,3,4,4,3,1,2,9] => 9

    Solution:

    To solve in O(n) you must to use the operator
    XOR, because this operator will cancel same pairs
    of numbers in binary:

    111 XOR 111 = 000

    And for diferents numbers XOR will aply sum operator
    or minus

    111 XOR 101 = 010

    So if the entire array have equals numbers except one
    the operator XOR will cancel the pairs of because of the
    association rule:

    7 ^ 1 ^ 2 ^ 3 ^ 2 ^ 1 ^ 3 => 7 ^ 1 ^ 1 ^ 2 ^ 2 ^ 3 ^ 3

    7 ^ (1 ^ 1) ^ (2 ^ 2) ^ (3 ^ 3) = > 7 ^ (0) ^ (0) ^ (0)

    7 ^ (0)

    And any number XOR with zero is the number:

    7

'''
