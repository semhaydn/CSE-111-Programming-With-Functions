# https://byui-cse.github.io/cse111-course/lesson05/prove.html#problem

# 05 Prove Milestone: Testing and Fixing Functions

from water_flow import water_column_height,pressure_gain_from_water_height
from water_flow import pressure_loss_from_pipe,pressure_loss_from_fittings,reynolds_number,pressure_loss_from_pipe_reduction
from pytest import approx
import pytest

def test_water_column_height():

    assert water_column_height(0 , 0)  == 0
    assert water_column_height(0 , 10) == 7.5
    assert water_column_height(25 , 0 ) == 25
    assert water_column_height (48.3 , 12.8) == 57.9

def test_pressure_gain_from_water_height():

    assert pressure_gain_from_water_height (0 , 998.2 , 9.80665) == approx(0 ,abs= 0.001 )
    assert pressure_gain_from_water_height ( 30.2 ,998.2 ,9.80665) == approx(295.628 , abs= 0.001)
    assert pressure_gain_from_water_height (50 ,998.2 , 9.80665) == approx( 489.450 , abs= 0.001)

def test_pressure_loss_from_pipe():
    
    assert pressure_loss_from_pipe (0.048692 , 0 , 0.018 , 1.75 ,998.2) == approx (0 , abs= 000.1)
    assert pressure_loss_from_pipe (0.048692 , 200 , 0 , 1.75 , 998.2) == approx (0 , abs= 000.1)
    assert pressure_loss_from_pipe (0.048692 , 200 , 0.018 , 0 , 998.2) == approx (0 , abs= 000.1)
    assert pressure_loss_from_pipe (0.048692 , 200 , 0.018 , 1.75, 998.2) == approx (-113.008 , abs= 000.1)
    assert pressure_loss_from_pipe (0.048692 , 200 , 0.018 , 1.65 , 998.2) == approx (-100.462 , abs= 000.1)
    assert pressure_loss_from_pipe (0.28687 , 1000 , 0.013 , 1.65 , 998.2) == approx (-61.576 , abs= 000.1)
    assert pressure_loss_from_pipe (0.28687 , 1800.75 , 0.013 , 1.65 , 998.2) == approx (-110.884 , abs= 000.1)

def test_pressure_loss_from_fittings ():
    assert pressure_loss_from_fittings (0 , 3 , 998.2) == approx (0 , abs= 0.001)
    assert pressure_loss_from_fittings (1.65 , 0 , 998.2) == approx (0 , abs= 0.001)
    assert pressure_loss_from_fittings (1.65 , 2 , 998.2) == approx (-0.109 , abs= 0.001)
    assert pressure_loss_from_fittings (1.75 , 2 , 998.2) == approx (-0.122 , abs= 0.001)
    assert pressure_loss_from_fittings (1.75 , 5 , 998.2) == approx (-0.306 , abs= 0.001)

def test_reynolds_number():
    assert reynolds_number(0.048692 , 0, 998.2 , 0.0010016) == approx (0 , 1)
    assert reynolds_number(0.048692 , 1.65, 998.2 , 0.0010016) == approx (80069 , 1)
    assert reynolds_number(0.048692 , 1.75 , 998.2 , 0.0010016) == approx (84922 , 1)
    assert reynolds_number(0.28687 , 1.65, 998.2 , 0.0010016) == approx (471729 , 1)
    assert reynolds_number(0.28687 , 1.75, 998.2 , 0.0010016) == approx (500318 , 1)

def  test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction ( 0.28687 , 0 ,1 , 0.048692 ,998.2 ) == approx( 0, abs= 0.001)
    assert pressure_loss_from_pipe_reduction ( 0.28687 , 1.65 ,471729 , 0.048692, 998.2) == approx( -163.744, abs= 0.001)
    assert pressure_loss_from_pipe_reduction ( 0.28687 , 1.75 ,500318 , 0.048692, 998.2) == approx( -184.182, abs= 0.001)
    



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

