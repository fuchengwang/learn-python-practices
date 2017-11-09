def find_person(qq, strU):
    return qq.get(strU, 'Not Found')


if __name__ == '__main__':
    qq = {
        'xiaoyun': '888888',
        'xiaohong': '5555555',
        'xiaoteng': '11111',
        'xiaoyi': '12341234',
        'xiaoyang': '1212121'
    }

    user = input()
    print(find_person(qq, user))
