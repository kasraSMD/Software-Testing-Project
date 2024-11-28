def calculate_area_and_perimeter(length, width):
    if length < 0 or width < 0:
        raise ValueError("the length and width should be positive")
    else:
        area = 0
        perimeter = 0
        area = length * width
        perimeter = 2 * (length + width)
        return area, perimeter