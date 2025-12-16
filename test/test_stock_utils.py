from stock_utils import moving_average

def test_moving_average_window3():
    values = [1, 2, 3, 4]
    ma = moving_average(values, 3)
    assert ma == [None, None, 2.0, 3.0]
