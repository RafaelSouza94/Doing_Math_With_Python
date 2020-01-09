from sympy import FiniteSet, pi

def time_period(length, g):
	pi_value = float(pi)
	T = 2 * pi_value * (length / g) ** 0.5
	return T

if __name__ == '__main__':
	L = FiniteSet(15, 18, 21, 22.5, 25)	# length in cm
	g_values = FiniteSet(9.8, 9.78, 9.83)
	print('{0:^15}{1:^15}{2:^15}'.format('Length(cm)', 'Gravity(m/s^2)', 'Time Period(s)'))

	for elem in L * g_values:	# cartesian product of the two sets
		l = elem[0]
		g = elem[1]
		t = time_period(l / 100, g)	# calculation in m
		print('{0:^15}{1:^15}{2:^15.3f}'.format(float(l), float(g), float(t))) 
