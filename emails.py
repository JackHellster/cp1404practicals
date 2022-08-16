user_email = input("Email: ")
name_email = {}
while user_email != "":
    name_email[user_email] = user_email.title().split("@")
    user_email = input("Email: ")


for email in name_email:
    print("Email: ", email)
    name_check = input(f"Is your name {name_email[email][0]}? (Y/n) ").lower()
    if name_check == "n" or name_check == "no":
        correct_name = input("Name: ")
        name_email[email] = correct_name



for email_and_name in name_email.items():
    print(f"{email_and_name}")