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

def solution2(n, arr1, arr2):
    answer = []
    for row1, row2 in zip(arr1, arr2):
        row = bin(row1|row2)[2:]
        password = row.rjust(n, " ")
        password = password.replace("1", "#")
        password = password.replace("0", " ")
        answer.append(password)
    return answer

if __name__ == '__main__':
    n = 6
    arr1 = [46, 33, 33 ,22, 31, 50]
    arr2 = [27 ,56, 19, 14, 14, 10]

    print (solution(n, arr1, arr2))
    print (solution2(n, arr1, arr2))
    #["######", "### #", "## ##", " #### ", " #####", "### # "
