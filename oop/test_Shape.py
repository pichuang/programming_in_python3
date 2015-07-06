__author__ = 'root'

from oop import Shape


def test_Shape():
    test_point = Shape.Point(100, 200)
    print("Repr: {0}".format(repr(test_point)))
    print("Str: {0}".format(str(test_point)))
    print("Distance_from_origin: {0}".format(test_point.distance_from_origin()))

    test_point.y = 500
    print("Repr: {0}".format(repr(test_point)))
    print("Str: {0}".format(str(test_point)))
    print("Distance_from_origin: {0}".format(test_point.distance_from_origin()))

def test_eval():
    test_point = Shape.Point(100, 200)
    print("Repr: {0}".format(repr(test_point)))
    eval_string = eval(test_point.__module__ + "." + repr(test_point))  # Ouput: Shape.
    print("Eval: {0}".format(eval_string))

def test_Circle():
    test_point = Shape.Point(100, 200)
    test_circle = Shape.Circle(10, 100, 200)
    print("Distance_from_origin by Class Point: {0}".format(test_point.distance_from_origin()))
    print("Distance_from_origin by Class Circle: {0}".format(test_circle.distance_from_origin()))


if __name__ == "__main__":
    # test_Shape()
    # test_eval()
    test_Circle()