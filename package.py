#Package class / definition
class Package:
    def __init__(self, ID, address, city, state, zipcode, deadline_time, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline_time = deadline_time
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None

    def __str__(self):
        return f"ID: {self.ID} | Address: {self.address} | City: {self.city} | State: {self.state} | Zipcode: {self.zipcode} | Deadline Time: {self.deadline_time} | Weight: {self.weight} | Delivery Time: {self.delivery_time} | Status: {self.status}"

    def update_status(self, current_time):
        if self.delivery_time < current_time:
            self.status = "Delivered"
        elif self.departure_time > current_time:
            self.status = "At Hub"
        else:
            self.status = "En Route"
