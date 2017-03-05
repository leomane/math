#!/usr/bin/python

import sys

# Find the centroid of a triangle

# The centroid of a triangle is where the
# bisecting lines of all three sides meet

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

def inverse(m):
	return float(1 / m * - 1)

def midpoint(a,b):
	x = float(a[0] + b[0]) / 2
	y = float(a[1] + b[1]) / 2
	return [x,y]

# A line consists of a point and a slope
# The first two elements of the array are 
# the x and y coordinates. The third element
# is the slope of the line 

def intersection(ab,cd):
	zx = float((ab[2]*ab[0] - cd[2]*cd[0] - ab[1] + cd[1]) / (ab[2] - cd[2]))
	zy = float(ab[2]*(zx-ab[0]) + ab[1])
	return [zx,zy]

# First, find the midpoint of line AB, then find the slope
# of the line that passes through the midpoint and the third 
# vertex of the trianglge. Repeat for line AC, then find the
# intersection between the two bisecting lines

def centroid(points):
	a = points[0]
	b = points[1]
	c = points[2]

	mid_ab = midpoint(a,b)
	m_ab_bisect = slope(mid_ab,c)
	ab_bisect = [c[0], c[1], m_ab_bisect]
	
	mid_ac = midpoint(a,c)
	m_ac_bisect = slope(mid_ac,b)
	ac_bisect = [b[0], b[1], m_ac_bisect]

	return intersection(ab_bisect, ac_bisect)

print centroid(get_points())

