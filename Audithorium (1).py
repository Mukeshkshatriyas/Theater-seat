print("Auditorium")
Audi = []
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
for i in range(n):
    row = []
    for j in range(m):
        number = str(i)+str(j)
        row.append(number)
    Audi.append(row)

def display():
    print("\nCurrent Seating Arrangement:")
    for row in Audi:
        for seat in row:
            print(seat, end=" ")
        print()

def update(action):
    seat = input("Enter seat number: ")
    for i in range(n):
        for j in range(m):
            if Audi[i][j] == seat or (action == "cancel" and Audi[i][j] == "X" and f"{i}{j}" == seat):
                Audi[i][j] = "X" if action == "buy" else f"{i}{j}"
                print(f"Seat {seat} {'bought' if action == 'buy' else 'cancelled'}.")
                return
    print("Seat not found.")
while True:
    display()
    print("\nMenu:\n1. Buy a Seat\n2. Cancel a Booking\n3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        update("buy")
    elif choice == '2':
        update("cancel")
    elif choice == '3':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")