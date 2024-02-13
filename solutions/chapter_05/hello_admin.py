usernames = ['Edgar', 'Julian', 'Robert', 'Elisa', 'Axel', 'admin']
today_logins = [1, 1, 2, 3, 7, 5]

for i, username in enumerate(usernames):

    if username == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        if today_logins[i] > 1:
            print(f'Hello again, {username}')
        print(f'Greetings {username}!')

if not usernames:
    print('We need to find some users!')
