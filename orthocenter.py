#!/usr/bin/python

import sys

# Find the orthocenter of a triangle

# The orthocenter of a triangle is where
# the altitude of all three sides meet


def get_points():
	points = []
	points.append(get_point('first'))
	points.append(get_point('second'))
	points.append(get_point('third'))
	return points


def get_point(position):
	point = []
	point.append(input('Enter '+position+' x coord: '))
	point.append(input('Enter '+position+' y coord: '))
	return point

def slope(a,b):
	return float(a[1] - b[1]) / (a[0] - b[0])

def inverse(a):
	return float(1 / a * -1)

# This function, used to calculate the orthocenter (zx, zy) of
# the triangle, begins with writting the altitude running through 
# any given point of the triangle in point-slope form as 
# zy - y1 = m(zx - x1),which can be rewritten in y intercept form as
# y = m(zx - x1) + y1. Here, x1 and y1 represent the x and y coordinates 
# of any of point on the triangle. First, zx is solved for by setting 
# the y intercept equations for the first two points equal to each other.
# This results in the equation m1(zx - x1) = m2(zx - x2), which can be 
# rewritten as zx = (m1x1 - m2x2 + y2 - y1) / (m1 - m2). Once zx is 
# calculated, it's pluged back into the y-int equation to solve for zy

def orthocenter(points):
	a = points[0]
	b = points[1]
	c = points[2]
	maz = inverse(slope(b,c))
	mbz = inverse(slope(a,c))
	zx = float((maz*a[0] - mbz*b[0] -a[1] + b[1]) / (maz - mbz))
	zy = float(maz*(zx-a[0]) + a[1])
	return [zx, zy]
	
print orthocenter(get_points())

