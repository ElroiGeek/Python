email_id = input("Enter you email id").strip()

username = email_id[:email_id.index('@')]

domain = email_id[:email_id.index('@')+1:]


print(f"Your username: {username} and your domain name is {domain}")