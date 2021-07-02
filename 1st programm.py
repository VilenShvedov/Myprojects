a, b, c = input('Please enter sides A, B and C. Split with space. ').split(', ')
a, b, c = float(a),float(b), float(c)
half_perimetr = (float(a) + float(b) + float(c)) / 2
triangle_area = (half_perimetr * (half_perimetr - a) * (half_perimetr - b) * (half_perimetr - c)) ** 0.5

print(half_perimetr)





