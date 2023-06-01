"""
Exploratory tests
"""
from pygame import Vector2
from math import acos
import math


rad_to_deg = lambda x: x *180/math.pi


def test_vector2_my():
    vec = Vector2(4.0, 3.0)

    # import ipdb;ipdb.set_trace()
    print(vec)
    vec = vec.rotate(30)  # In degrees
    print(vec)
    vec = vec.rotate(15)  # In degrees
    print(vec)

    normalized = vec.normalize()  # turn direction, normalize_ip, in place
    print(normalized)
    assert True


def test_vector_length():
    """ symbol |v| sometimes it's ||v|| and meaning is the same"""
    vec = Vector2(6, 3)

    assert math.sqrt(vec.x**2 + vec.y**2) == vec.length()




def test_vector_angle():
    """
    https://www.cuemath.com/geometry/angle-between-vectors/

    vector magnitude |v| is vector length
    |v| = sqrt(v.x^2 + v.y^2 + v.z^2)
    """
    vec_a = Vector2(6, 3)
    vec_b = Vector2(2, 6)
    angle = vec_a.angle_to(vec_b)
    print(angle)
    assert angle == 45

    # using dot product
    res = acos(vec_a.dot(vec_b) / (vec_a.length() * vec_b.length()))
    assert round(rad_to_deg(res), 0) == 45


def test_dot_product():
    """Sum of product of x and y"""
    vec = Vector2(2.0, 3.0)
    vec2 = Vector2(1.0, 3.0)
    prod = vec.dot(vec2)
    assert prod == 11.0


def test_cross():
    """
    https://www.nagwa.com/en/explainers/175169159270/
    """
    vec = Vector2(2.0, 3.0)
    vec2 = Vector2(1.0, 3.0)
    print(vec.cross(vec2)
    ...