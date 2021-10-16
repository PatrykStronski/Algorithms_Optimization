from algorithms_2d import sort_points

def test_sort_points():
    x1 = (0, 1)
    x2 = (1, 1)
    x3 = (2, 1)

    f1 = 1
    f2 = 2
    f3 = 3

    unsorted = ((f1,x1), (f3, x3), (f2, x2))
    sorted_tst = ((f3, x3), (f2, x2), (f1,x1), 1)
    assert sorted_tst == sort_points(unsorted[0], unsorted[1], unsorted[2])

def test_sort_points2():
    x1 = (0, 1)
    x2 = (1, 1)
    x3 = (2, 1)

    f1 = 1
    f2 = 2
    f3 = 3

    unsorted = ((f3, x3), (f2, x2), (f1,x1))
    sorted_tst = ((f3, x3), (f2, x2), (f1,x1), 3)
    assert sorted_tst == sort_points(unsorted[0], unsorted[1], unsorted[2])