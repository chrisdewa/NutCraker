from nutcraker import MD5Breaker

if __name__ == '__main__':
    target = MD5Breaker.md5('chris')
    print(f'Trying to break: {target}')
    pwd = MD5Breaker(target).attack()
    print(pwd or 'Password not found')