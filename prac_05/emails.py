user_data = {}

email = input("Email: ")
while email != "":
    email_name = (email.split("@")[0]).split(".")
    full_name = (" ".join(email_name)).title()
    user_input = input(f"Is your name {full_name}?  (Y/n) ").upper()
    if (user_input == "Y") or (user_input == ""):
        user_data[email] = full_name
    else:
        user_data[email] = input("Name: ")
    email = input("Email: ")

for email in user_data:
    print(f"{user_data[email]} ({email})")