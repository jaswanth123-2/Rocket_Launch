# Rocket_Launch

This Python code implements a basic rocket launch simulator, providing functionalities for pre-launch checks, initiating a rocket launch, simulating the flight, and fast-forwarding through the simulation for a specified duration. The simulation considers parameters such as fuel consumption, altitude increment, and speed.
## Rocket Parameters

The rocket's initial parameters are established during initialization:

- **Stage**: Represents the current stage of the rocket, initially set to "Pre-Launch."
- **Fuel**: Denotes the available fuel for the launch, initially set to 100%.
- **Altitude**: Indicates the current altitude of the rocket, initially set to 0 km.
- **Speed**: Represents the speed of the rocket, initially set to 0 km/h.

Additionally, constant values are defined for fuel consumption rate (`f`), altitude increment per time step (`a`), and speed (`s`).

## Methods

### 1. `__init__`: 
   - Initializes the rocket's parameters.

### 2. `reset`:
   - Resets the rocket's parameters for a new launch.

### 3. `pre_launch_checks`:
   - Conducts pre-launch checks, covering fuel, power, structural, range safety, and weather considerations.
   - If all decisions are positive, sets the "go" flag to 1, indicating successful checks.

### 4. `launch`:
   - Initiates the rocket launch if pre-launch checks are successful.
   - Invokes the `simulate_flight` method.

### 5. `simulate_flight`:
   - Simulates the rocket's flight.
   - Updates the rocket's status, including stage, fuel, altitude, and speed.
   - Prints the current status during the flight.
   - Terminates the simulation if the fuel is depleted or if the mission fails.

### 6. `update_status`:
   - Updates the rocket's status during flight.
   - Decreases fuel, increases altitude, and sets the speed.
   - Prints the current status.
   - Checks for mission failure due to insufficient fuel.

### 7. `fast_forward`:
   - Simulates the rocket's status after fast-forwarding for a given number of seconds.
   - Prints the result after the specified time.

### 8. `main`:
   - Creates an instance of the `RocketLaunchSimulator`.
   - Enters a loop to receive user commands.
   - Executes the corresponding method based on the user's input.
   - Allows users to initiate pre-launch checks, launch the rocket, fast-forward, reset parameters, or exit the simulator.

## Running the Simulator

The simulator executes upon running the script. Users interact with the simulator by entering commands like "start_checks," "launch," "fast_forward X," "reset," or "exit" during the program's execution.

To exit the simulator, the user can input "exit," and the program will display "Exiting the rocket simulator. Goodbye!"
