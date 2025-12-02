guest = ['Jesus Christ', 'Lemmi Kilmister', 'Jack Ma', 'John Snow']
removed_guests = []

removed_guests.append(guest.pop())  # John Snow
print(f"Текущие гости: {guest}")

removed_guests.append(guest.pop())  # Jack Ma
print(f"Текущие гости: {guest}")

print(f"Sorry {removed_guests[0]}, there is no room at the dinner table.")
print(f"Sorry {removed_guests[1]}, there is no room at the dinner table.")