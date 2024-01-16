participants = [
    "Mario",
    "Luigi",
    "Yoshi",
    "Bowser",
    "Toad",
    "Peach"
]

invitation_message = "You are invited to dinner!"
new_table_message = "Good news! We found a bigger dinner table."


def send_message(guests, invitation):
    for guest in guests:
        print(f"Hello {guest}, {invitation}")


send_message(participants, invitation_message)

guest_unable_attend = "Bowser"
print(f"\n{guest_unable_attend}, can't make it to the dinner.\n")

new_guest = "Donkey Kong"
participants[participants.index(guest_unable_attend)] = new_guest

send_message(participants, new_table_message)

participants.insert(0, "Link")

new_guest_middle = "Sonic"
middle_index = len(participants) // 2
participants.insert(middle_index, new_guest_middle)

participants.append("Ryu")

send_message(participants, invitation_message)
