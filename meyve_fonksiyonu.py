def fruit_by_color(color):
    color = color.lower()
    
    if color == "red":
        return "apple"
    elif color == "yellow":
        return "banana"
    elif color == "green":
        return "kiwi"
    else:
        return "Unknown color"