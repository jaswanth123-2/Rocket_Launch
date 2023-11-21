import time

class RocketLaunchSimulator:
    
    def __init__(self): #Initializing rocket parameters
        
        #values of starting stage of rocket
        self.stage = "Pre-Launch"
        self.fuel = 100  
        self.altitude = 0
        self.speed = 0
        
        self.f = 10  # Fuel consumption rate
        self.a = 10  # Altitude increment per time step
        self.s = 1000  # speed
        
        self.go = 0  # to indicate if pre-launch checks are successful

    def reset(self):
        # Reset rocket parameters for a new launch
        self.stage = "Pre-Launch"
        self.fuel = 100
        self.altitude = 0
        self.speed = 0
        self.go = 0

        
        
    def pre_launch_checks(self):
        # Perform pre-launch checks
        fuel_decision = 1
        power_decision = 1
        structural_decision = 1
        range_safety_decision = 1
        weather_decision = 1

        if all(i == 1 for i in [fuel_decision, power_decision, structural_decision, range_safety_decision, weather_decision]):
            print("All systems are 'Go' for launch.")
            self.go = 1  # Set the flag to indicate successful checks
        else:
            print("Pre-Launch checks failed. Re-initiating checks.")
            self.pre_launch_checks()  # Re-initiate checks if any decision is not favorable

            
            
        
    def launch(self):
        # Initiate launch if pre-launch checks are successful
        if self.go == 1:
            self.stage = 1
            self.update_status()
            self.simulate_flight()
        else:
            print("Pre-Launch is not initialized")

            
            
    def simulate_flight(self):
        
        
        # Simulate the rocket's flight
        while self.stage != "Mission Failed" and self.fuel > 0:
            self.update_status()
            time.sleep(1)  # Simulating the time passage

            
        if self.stage == "Mission Failed":
            print("Mission Failed due to insufficient fuel.")
        else:
            print("Orbit achieved! Mission Successful.")

            
            
    def update_status(self):
        # Update rocket status during flight
        if self.stage != "Mission Failed" and self.fuel - self.f >= 0:
            self.fuel -= self.f
            self.altitude += self.a
            self.speed = self.s
            print(f"Stage: {self.stage}, Fuel: {self.fuel}%, Altitude: {self.altitude} km, Speed: {self.speed} km/h")
            self.stage += 1  # Increment the stage
        else:
            self.fuel = 0
        if self.fuel == 0 and self.stage < 9:
            self.stage = "Mission Failed"

            
            
    def fast_forward(self, seconds):
        # Simulate rocket status after fast forwarding for a given number of seconds
        simulated_stage = 0
        simulated_fuel = 100
        simulated_altitude = 0
        simulated_speed = 0

        for i in range(seconds):
            simulated_stage += 1
            simulated_fuel -= self.f
            simulated_altitude += self.a
            simulated_speed = self.s

        if simulated_fuel >= 0:
            print(f"Result after {seconds} seconds - Stage: {simulated_stage}, Fuel: {simulated_fuel}%, Altitude: {simulated_altitude} km, Speed: {simulated_speed} km/h")
        else:
            print("The following command is out of time")


def main():
    rocket_simulator = RocketLaunchSimulator()

    while True:
        user_input = input("Enter a command: ")
        if user_input == "start_checks":
            rocket_simulator.pre_launch_checks()
        elif user_input == "launch":
            rocket_simulator.launch()
        elif user_input.startswith("fast_forward"):
            try:
                seconds = int(user_input.split()[1])
                rocket_simulator.fast_forward(seconds)
            except (ValueError, IndexError):
                print("Invalid, fast_forward. Please use 'fast_forward X' where X is the number of seconds.")
        elif user_input == "reset":
            rocket_simulator.reset()
        elif user_input == "exit":
            print("Exiting the rocket simulator. Goodbye!")
            break
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()
