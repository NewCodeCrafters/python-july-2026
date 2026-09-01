class HotelRoom:

    def __init__(self, room_number, room_type, price_per_night, max_occupancy):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.max_occupancy = max_occupancy
        self.is_available = True
        self.current_guest = None

    def book_room(self, guest):
        if self.is_available:
            self.current_guest = guest
            self.is_available = False
            print("Room", self.room_number, "has been booked by", guest)
        else:
            print("Sorry, room", self.room_number, "is already booked.")

    def check_out(self):
        if not self.is_available:
            print(self.current_guest, "has checked out of room", self.room_number)
            self.current_guest = None
            self.is_available = True
        else:
            print("Room is already available.")

    def check_availability(self):
        return self.is_available

    def calculate_stay_cost(self, nights):
        return self.price_per_night * nights

    def change_price(self, new_price):
        if new_price > 0:
            self.price_per_night = new_price
            print("Price changed successfully.")
        else:
            print("Price must be greater than 0.")

    def get_room_status(self):
        if self.is_available:
            return "Available"
        else:
            return "Occupied"



single_room = HotelRoom(101, "Single", 20000, 1)
double_room = HotelRoom(102, "Double", 35000, 2)
suite_room = HotelRoom(103, "Suite", 60000, 4)



single_room.book_room("John")
double_room.book_room("Mary")


single_room.book_room("Peter")



print(single_room.get_room_status())
print(double_room.get_room_status())
print(suite_room.get_room_status())



cost = single_room.calculate_stay_cost(3)
print("John's stay cost is:", cost)


suite_room.change_price(70000)

single_room.check_out()

print("Room 101 available:", single_room.check_availability())

    




















