


def fun(s):
    # return True if s is a valid email, else return False
    try:
        user_name, url = s.split("@")
        website, ext = url.split(".")
    except ValueError:
        return False
    
    # Check the validity
    if not user_name.replace("-", "").replace("_", "").isalnum():
        return False
    if not website.isalnum():
        return False
    if len(ext) > 3:
        return False
    # If not anything, then
    return True




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






