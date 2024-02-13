current_users = ['Az0ra', 'user01234', 'aline45', 'bryan089', 'anon508']
new_users = ['anton242', 'Az0ra', 'vil234', 'bryan089', 'oliv4r1923']

lowercase_current_users = [user.lower() for user in current_users]


for user in new_users:
    if user.lower() in lowercase_current_users:
        print(f'Sorry, the username "{user}" already exists. Please choose a new one!')
    else:
        print(f'The name "{user}" is available!')
