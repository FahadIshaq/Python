class EllipticCurvePoint:
    """A class representing a point on an elliptic curve."""

    def __init__(self, x, y, curve):
        self.x = x
        self.y = y
        self.curve = curve

    def is_at_infinity(self):
        """Check if the point is at infinity (the identity element)."""
        return self.x is None and self.y is None

    def __eq__(self, other):
        if self.is_at_infinity() or other.is_at_infinity():
            return self.is_at_infinity() and other.is_at_infinity()
        return (self.x, self.y) == (other.x, other.y)

    def __add__(self, other):
        if self.is_at_infinity():
            return other
        if other.is_at_infinity():
            return self
        if self.x == other.x and self.y == other.y:
            return self._double()
        elif self.x == other.x:
            return EllipticCurvePoint(None, None, self.curve)  # Point at infinity
        else:
            return self._add_different(other)

    def _double(self):
        if self.y == 0 or self.is_at_infinity():
            return EllipticCurvePoint(None, None, self.curve)  # Point at infinity

        m = (3 * self.x**2 + self.curve.a) / (2 * self.y)
        x3 = m**2 - 2 * self.x
        y3 = m * (self.x - x3) - self.y
        return EllipticCurvePoint(x3, y3, self.curve)

    def _add_different(self, other):
        m = (other.y - self.y) / (other.x - self.x)
        x3 = m**2 - self.x - other.x
        y3 = m * (self.x - x3) - self.y
        return EllipticCurvePoint(x3, y3, self.curve)

class EllipticCurve:
    """A class representing an elliptic curve of the form y^2 = x^3 + ax + b."""

    def __init__(self, a, b):
        self.a = a
        self.b = b

def ecc_point_multiplication(P, n):
    """Function to perform elliptic curve point multiplication."""
    Q = EllipticCurvePoint(None, None, P.curve)  # Start with the point at infinity
    while n > 0:
        if n % 2 == 1:
            Q = Q + P
        P = P._double()
        n //= 2
    return Q

# Example test case
curve = EllipticCurve(a=2, b=3)
P = EllipticCurvePoint(x=3, y=4, curve=curve)
n = 2

# Calculate nP
nP = ecc_point_multiplication(P, n)
(nP.x, nP.y) if not nP.is_at_infinity() else "Point at Infinity"
