import math

def main ():

    names = ["#1 Picnic","#1 Tall", "#2","#2.5","#3 Cylinder","#5","#6Z","#8Z Short","#10","#211","#300","#303"]
    Radiuses = [6.83,7.78,8.73,10.32,10.79,13.02,5.40,6.83,15.72,6.83,7.62,8.10]
    heights = [10.16,11.91,11.59,11.91,17.78,14.29,8.89,7.62,17.78,12.38,11.27,11.11]

    for i in range(len(names)):
        name = names[i] 
        radius = Radiuses[i]
        height = heights[i]

        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        print (f" {name} {storage_efficiency:.2f}")


def compute_volume(radius, height):
    volume = (math.pi* radius**2)* height
    return volume

def compute_surface_area(radius,height):
    surface_areaa = (2 * math.pi * radius) * (radius + height)
    return surface_areaa

def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency

if __name__ == "__main__":  
    main()







