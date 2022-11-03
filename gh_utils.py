from github3 import login


def two_factor_callback():
    return input("Enter 2FA code: ").strip() or two_factor_callback()


def enter_login_details():
    return (input("Enter username: ").strip(), input("Enter password: ").strip())


username, password = enter_login_details()
print(username)
print(password)
gh = login(
    username, password, two_factor_callback=two_factor_callback
)  # , two_factor_callback=two_factor_callback())

print(gh.me())
