class bajra:
    name="bajra"
    seed_required_per_acre=45 # in kg
    avg_yield_per_acre=14 # in quintals
    msp=2425 # in rs per quintal
    seed_rate= 48 # in rs/kg
    miscelaneous_cost_per_acre= 15400 # in rs include water, fertilizer, labor etc
    def __init__(self):
        self.moisture_content= 75 # in percentage , can be fetched by the sensor
        try:
            self.area_in_acres=float(input("enter the area in acres: "))
        except :
            print("Invalid input. Please enter a valid number.")
        self.seed_required= self.seed_required_per_acre * self.area_in_acres
        self.yield_amount= self.avg_yield_per_acre * self.area_in_acres
        self.revenue= self.msp * self.avg_yield_per_acre * self.area_in_acres
        self.cost= self.seed_rate * self.seed_required_per_acre* self.area_in_acres + self.miscelaneous_cost_per_acre * self.area_in_acres
        self.profit= (self.msp * self.avg_yield_per_acre * self.area_in_acres) - (self.cost)
    def calculate_seed_required(self):
        print(f"seed required for {self.area_in_acres} acres is {self.seed_required} kg")

    def calculate_yield(self):
        
        print(f"expected yield for {self.area_in_acres} acres is {self.yield_amount} quintals")

    def calculate_revenue(self):
        
        print(f"expected revenue for {self.area_in_acres} acres is {self.revenue} rs")

    def calculate_cost(self):
        
        print(f"estimated cost for {self.area_in_acres} acres is {self.cost} rs")
    def calculate_profit(self):
        
        print(f"estimated profit for {self.area_in_acres} acres is {self.profit} rs")
bajra_farm = bajra()
bajra_farm.calculate_seed_required()
bajra_farm.calculate_yield()
bajra_farm.calculate_revenue()
bajra_farm.calculate_cost()
bajra_farm.calculate_profit()