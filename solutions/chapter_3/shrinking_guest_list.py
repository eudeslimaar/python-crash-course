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
apology_message = "Unfortunately, we can only invite two people for dinner."


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

send_message(participants, apology_message)

while len(participants) > 2:
    removed_guest = participants.pop()
    print(f"Sorry, {removed_guest}. You're no longer invited to dinner.")

send_message(participants, invitation_message)

del participants[:]
print("Guest list: ", participants)

