def sliceEmailAddress():
    email = input("Enter your e-mail: ")
    username = email[:email.index("@")]
    domain = email[email.index("@") + 1:]
    print(f"Your username is {username}, and your domain name is {domain}.")
