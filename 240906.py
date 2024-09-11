def solution(phone_book):
    res = 0
    phone_book.sort()
    for phone in phone_book:
        check = phone[:-1]
        check_list = [phone[:idx] for idx in range(1, len(phone))]
        res = len(list(set(check_list).intersection(phone_book)))
        if res > 0:
            break
    if res == 0:
        return True
    else:
        return False
    # answer = False
    # for idx in range(len(phone_book)):
    #     target = phone_book[:idx] + phone_book[idx+1:]
    #     # check = list(filter(lambda x: x.startswith(phone_book[idx]),phone_book))
    #     # target_str = "-".join(target)
    #     answer = phone_book[idx].startswith(tuple(target))
    #     if answer == True:
    #         break
    # return not answer

phone_book = ["12","123","1235","567","88"]	
answer = solution(phone_book)
print(answer)