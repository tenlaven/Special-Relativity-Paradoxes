from decimal import *

# Set 'Decimal' context
ec = DefaultContext.copy()
ec.prec = 4
ec.clamp = 1
ec.rounding = ROUND_HALF_UP


# Functions
def coordDiff(xf, xi, tf, ti):
	"""
	Calculate changes in distance (dx) and time (dt)
	final(x, t) - initial(x, t)
	"""
	dx = xf - xi
	dt = tf - ti
	return dx, dt


def getGamma(velocity):
	"""
	Calculate gamma
	Gammas used for Twin project: 29/20 (1.45) and 1218/1282 (3.205)
	Gamma used for Ladder project:
	"""
	v = ec.power(velocity, 2)
	gamma = ec.divide(1, ec.sqrt(ec.subtract(1, v)))
	return gamma


def addVelocity(v, c):
	"""
	Calculate new velocity for rocket's return from target
	Velocities used for Twin project: 21/29 (0.72 of C) and 1218/1282 (0.95 of C)
	Velocity used for Ladder project: 3/5 (0.60 of C)
	"""
	u = ec.divide(ec.multiply(2, ec.multiply(v, c)), ec.add(ec.power(c, 2), ec.power(v, 2)))
	return u


def getSpaceIntv(tup):
	"""
	Spacelike Spacetime Intervals
	Calculates change in distance and time
	from given coordinates (dx, dt)
	Spacelike interval calculation: √((dx)^2 - (dt)^2)
	"""
	x, t = Decimal(tup[0]), Decimal(tup[1])
	slint = ec.sqrt(ec.subtract(ec.power(x, 2), ec.power(t, 2)))
	return slint


def getTimeIntv(tup):
	"""
	Timelike Spacetime Intervals
	Calculates change in distance and time
	from given coordinates (dx, dt)
	Timelike interval calculation: √((dt)^2 - (dx)^2)
	"""
	x, t = tup
	tlint = ec.sqrt(ec.subtract(ec.power(t, 2), ec.power(x, 2)))
	return tlint


def getCoords(velocity, gamma, *args):
	"""
	Lorentz Transformations:
	Velocity, Gamma, Coordinates(x, t OR dx, dt)
	"""
	v = velocity
	g = gamma
	x, t, dx, dt = args

	if (x and t) is not None and (dx and dt) is None:
		dx = ec.multiply(g, ec.subtract(x, ec.multiply(v, t)))
		dt = ec.multiply(g, ec.subtract(t, ec.multiply(v, x)))
		return dx, dt
	elif (dx and dt) is not None and (x and t) is None:
		x = ec.multiply(g, ec.add(dx, ec.multiply(v, dt)))
		t = ec.multiply(g, ec.add(dt, ec.multiply(v, dx)))
		return x, t
	else:
		return None, None
