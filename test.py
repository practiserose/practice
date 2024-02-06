
password = 'AishaRose@123'
pass_attempt = 0
pass_limit = 3
while pass_attempt < pass_limit:
    pas = input("Enter password: ")
    pass_attempt += 1
    if pas == password:
        print("Login Successful")
        break

else:
    print("Account blocked, contact admin for assistance")



