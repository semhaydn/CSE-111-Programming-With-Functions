# Calculate water column height 
def water_column_height(tower_height, tank_height):
    w_c_height = tower_height + ((3 * tank_height) / 4)
    return w_c_height

# Calculate pressure gain
def pressure_gain_from_water_height(height, water_density, earth_acceleration_of_gravity):
    pressure_gain = (water_density * earth_acceleration_of_gravity * height) / 1000
    return pressure_gain

# Calculate pressure loss from pipe
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity, water_density):
    pressure_loss = ((-1 * friction_factor) * pipe_length * water_density * (fluid_velocity ** 2)) / (2000 * pipe_diameter)
    return pressure_loss

# Calculate the pressure loss from fittings
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings, water_density):
    loss_from_fittings = ((-0.04 * water_density) * (fluid_velocity ** 2) * quantity_fittings) / 2000
    return loss_from_fittings

# Calculate the Reynolds number
def reynolds_number(hydraulic_diameter, fluid_velocity, water_density, water_dynamic_viscosity):
    reynolds_number = (water_density * hydraulic_diameter * fluid_velocity) / water_dynamic_viscosity
    return reynolds_number

# Calculate pressure loss from pipe reduction
def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter, water_density):
    k = (0.1 + (50 / reynolds_number)) * (((larger_diameter / smaller_diameter) ** 4) - 1)
    loss_from_pipe_reduction = ((-1 * k) * water_density * (fluid_velocity ** 2)) / 2000
    return loss_from_pipe_reduction

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters) 11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters) 1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

EARTH_ACCELERATION_OF_GRAVITY = 9.80665
WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    density = WATER_DENSITY
    viscosity = WATER_DYNAMIC_VISCOSITY
    acceleration_of_gravity = EARTH_ACCELERATION_OF_GRAVITY

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height, density, acceleration_of_gravity)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity, density, viscosity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity, density)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles, density)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER, density)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity, density)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")

if __name__ == "__main__":
    main()




 




    