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

