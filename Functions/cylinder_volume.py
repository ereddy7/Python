r =10
h =7

print("Volume of cylinder is",3.14*r*r*h)


def cylinder_volume(radius, height):
    print("radius", radius)
    print("height", height)
    """
    Calculate the volume of a cylinder.    
    Args:
        radius (float): The radius of the cylinder's base.
        height (float): The height of the cylinder.    
    Returns:
        float: The volume of the cylinder.
    """
    volume = 3.14 * radius * radius * height
    return volume

volume = cylinder_volume(r, h)
print("Volume of cylinder is", volume)

print("Volume of cylinder is", cylinder_volume(r, h))

volume = cylinder_volume(height=h,radius=r)
print("Volume of cylinder is", volume)

"""

"""
def cylinder_volume_defaultValues(radius, height=7):
    print("radius", radius)
    print("height", height)
    """
    Calculate the volume of a cylinder.    
    Args:
        radius (float): The radius of the cylinder's base.
        height (float): The height of the cylinder.    
    Returns:
        float: The volume of the cylinder.
    """
    volume = 3.14 * radius * radius * height
    return volume

print("Volume of cylinder wih default values", cylinder_volume_defaultValues(10))
