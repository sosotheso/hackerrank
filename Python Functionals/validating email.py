def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, l = s.split('@')
        webSiteName, extension = l.split('.')
    except ValueError:
        return False
    if username.replace('-', '').replace('_', '').isalnum():
        if webSiteName.isalnum():
            if len(extension) <= 3:
                if extension.isalpha():
                    return True
    return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
