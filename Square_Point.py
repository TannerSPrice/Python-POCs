def square_point(x, y, z):
    x_squared = x * x
    y_sqaured = y * y
    z_squared = z * z
    #return all three values:
    return x_squared, y_sqaured, z_squared

three_squared, four_squared, five_squared = square_point(3, 4, 5)

print("three squared is:" , three_squared, "\n""four squared is:" , four_squared, "\n""five squared is:" ,five_squared)
