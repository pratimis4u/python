class bike_details:
    def __init__(self,b_name,b_model,b_price):
        self.b_name=b_name
        self.b_model=b_model
        self.b_price=b_price
    def display_bike(self):
        print(self.b_name)
        print(self.b_model)
        print(self.b_price)
b1=bike_details("honda","2023","1L")
b2=bike_details("kawasaki ninja","2023","2L")
b3=bike_details("mercedes","2020","3L")
b1.display_bike()
b2.display_bike()
b3.display_bike()