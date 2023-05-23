# https://byui-cse.github.io/cse111-course/lesson05/prove.html#problem

# 05 Prove Milestone: Testing and Fixing Functions

# Semih Aydin

# Calculate water column height 

def water_column_height(tower_height, tank_height):

    w_c_height = tower_height+ ((3* tank_height)/4)

    return w_c_height

# Calculate pressure gain

def pressure_gain_from_water_height(height):

    pressure_gain = (998.2* 9.80665* height) / 1000

    return pressure_gain

# Calculate pressure gain

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    
    pressure_loss = ((-1 * friction_factor) * pipe_length * 998.2 * (fluid_velocity ** 2 )) / (2000 * pipe_diameter)

    return pressure_loss


    