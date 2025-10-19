# A wire is the form of Arc at an angle of 60 degrees and the radius of the arc is 42. The wire is converted into a square. Find the area of the square.


# given parameters
centre_angle = 60
radius = 42

#calculate length of arc
arc_length = (centre_angle/360)*2*3.14*radius
print("Length of arc is {} ".format(arc_length))

#assuming that arc as a square, calculate length of side of square
square_side = arc_length/4

#area of square
area = square_side*square_side
print("Area is {}".format(area))
