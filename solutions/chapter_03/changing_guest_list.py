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

guest_unable_attend = "Bowser"
print(f"\n{guest_unable_attend}, can't make it to the dinner.")

new_guest = "Donkey Kong"
participants[participants.index(guest_unable_attend)] = new_guest

send_invite(participants, invitation_message)
