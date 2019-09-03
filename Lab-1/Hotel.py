class Hotel:
    def __init__(self, name, amount_of_rooms, amount_of_visitors):
        self.name = name
        self.amount_of_rooms = amount_of_rooms
        self.amount_of_visitors = amount_of_visitors

    def __repr__(self):
        return str(self.__dict__)
