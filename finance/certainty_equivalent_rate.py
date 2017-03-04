#!/usr/bin/python

import sys

# Find the utility of the investment based
# on the risk aversion of the investor.
# A higher score equates to increased 
# risk-aversion. The result is the utility,
# which is the same rate of return that an 
# investor would require from a risk-free
# investment to achieve the same utility

def get_expected_return():
	return input('Enter the expected return (0-1): ')

def get_risk_aversion_score():
	return input('Enter the risk aversion score (0-10): ')

def get_standard_deviation():
	return input('Enter the standard deviation (risk) of the investment: ')

def calulate_cetainty_equivalent_rate(Er,A,sd):
	return Er - .5 * A * sd ** 2

Er = get_expected_return()
A = get_risk_aversion_score()
sd = get_standard_deviation()

print calulate_cetainty_equivalent_rate(Er,A,sd)
