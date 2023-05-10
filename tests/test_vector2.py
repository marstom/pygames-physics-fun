from pygame import Vector2


def test_vector2_my():
    vec = Vector2(2.0, 2.0)

    # import ipdb;ipdb.set_trace()
    print(vec)
    vec = vec.rotate(10)  # In degrees
    print(vec)
    vec = vec.rotate(10)  # In degrees
    print(vec)

    normalized = vec.normalize()  # turn direction
    print(normalized)
    assert True


def test_vector_angle():
    base = Vector2(0, 0)
    vector = Vector2(2, 6)
    angle = vector.angle_to(base)
    print(angle)
