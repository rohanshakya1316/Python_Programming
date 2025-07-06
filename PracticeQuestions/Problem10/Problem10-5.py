# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Metro Railways.
from random import randint

class Train: 
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare
        self.booked_seats = 0
    
    def book_ticket(self):
        if self.booked_seats < self.seats:
            self.booked_seats += 1
            print(f"Ticket booked successfully for {self.name}. Seat No. {self.booked_seats}")
        else:
            print(f"Sorry, no seats available!")
    
    def get_status(self):
        available_seats = self.seats - self.booked_seats
        print(f"Train: {self.name}")
        print(f"Total Seats: {self.seats}")
        print(f"Booked Seats: {self.booked_seats}")
        print(f"Available Seats: {available_seats}")
    
    def get_fare_info(self):
        print(f"The fare for {self.name} is Rs. {self.fare}")


metro_train = Train("Metro Express", randint(5, 100), randint(100, 500))

while True: 
    print("\n--- Metro Railway Booking System ---")
    print("1. Book Ticket")
    print("2. Check Seat Status")
    print("3. Get Fare Information")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        metro_train.book_ticket()
    elif choice == '2':
        metro_train.get_status()
    elif choice == '3':
        metro_train.get_fare_info()
    elif choice == '4':
        print("Thank you for using Metro Railway Booking System!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
    