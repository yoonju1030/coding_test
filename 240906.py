def solution(phone_book):
    answer = True
    for idx in range(len(phone_book)):
        check = list(filter(lambda x: x.startswith(phone_book[idx]),phone_book[]))
        if len(check) > 1:
            answer = False
            break
    return answer
