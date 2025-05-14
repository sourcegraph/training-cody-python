def calculate_area(radius):
    area = 3.14159 * radius * radius
    return area

def calculate_area_with_diameter(diameter):
    radius = diameter / 2
    return calculate_area(radius)

def calculate_circumference(radius):
    circumference = 2 * 3.14159 * radius
    return circumference

def calculate_sector_area(radius, angle_degrees):
    # Calculate area of a sector with given angle in degrees
    angle_radians = angle_degrees * (3.14159 / 180)
    sector_area = (angle_radians / 2) * radius * radius
    return sector_area

def print_area(radius):
    area = calculate_area(radius)
    print("The area of a circle with radius", radius, "is", area)

def print_circle_properties(radius):
    area = calculate_area(radius)
    circumference = calculate_circumference(radius)
    diameter = radius * 2
    
    print(f"Circle with radius {radius}:")
    print(f"  - Diameter: {diameter}")
    print(f"  - Circumference: {circumference:.2f}")
    print(f"  - Area: {area:.2f}")


if __name__ == "__main__":
    r = 5
    print_area(r)
    
    # Example using the new functions
    print("\nCalculating with diameter:")
    diameter = 10
    print(f"The area of a circle with diameter {diameter} is {calculate_area_with_diameter(diameter):.2f}")
    
    print("\nCalculating sector area:")
    angle = 45  # 45 degrees
    print(f"The area of a {angle}° sector with radius {r} is {calculate_sector_area(r, angle):.2f}")
    
    print("\nComplete circle properties:")
    print_circle_properties(r)