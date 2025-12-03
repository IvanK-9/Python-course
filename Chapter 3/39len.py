guest = ['Jesus Christ', 'Lemmi Kilmister', 'Jack Ma', 'John Snow']
removed_guests = []

removed_guests.append(guest.pop())  # John Snow
print(f"Current: {guest}")

removed_guests.append(guest.pop())  # Jack Ma
print(f"Current: {guest}")

print(f"Sorry {removed_guests[0]}, there is no room at the dinner table.")
print(f"Sorry {removed_guests[1]}, there is no room at the dinner table.")


print(len(guest))
#print(len(removed_guests))