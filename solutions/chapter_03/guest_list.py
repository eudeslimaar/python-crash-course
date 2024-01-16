participants = [
    "Mario",
    "Luigi",
    "Yoshi",
    "Bowser",
    "Toad",
    "Peach"
]

invitation_message = "You are invited to dinner!"


def send_invite(guests, invitation):
    for guest in guests:
        print(f"Hello {guest}, {invitation}")


send_invite(participants, invitation_message)

