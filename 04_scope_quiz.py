pi = 3.14
# get_area_of_circle has access to the pi variable because it is in the global scope

def get_area_of_circle(raidus):
    area = pi * raidus * raidus
    return area