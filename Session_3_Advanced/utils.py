def calculate_bmi(height, weight):
    try:
        return round(weight / (height ** 2), 2)
    except:
        return None
