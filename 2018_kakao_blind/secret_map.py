def solution(n, arr1, arr2):
    answer = []
    for row1, row2 in zip(arr1, arr2):
        passwords = ""
        row = row1 | row2

        count = 0
        while count < n:
            curr_p = "#" if row % 2 == 1 else " "
            passwords = "%s%s" % (curr_p, passwords)
            row = row // 2
            count += 1
        answer.append(passwords)
    return answer
