def bmi(weight, height):
    x = weight / (height * height)
    if x <= 18.5:
        return "Underweight"
    elif 18.5 < x <= 25.0:
        return "Normal"
    elif 25.0 < x <= 30.0:
        return "Overweight"
    else:
        return "Obese"
