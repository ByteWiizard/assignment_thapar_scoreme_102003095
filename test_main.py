import pytest
from main import longest_path

def test_longest_path():
    graph1 = [
        [(1, 3), (2, 2)],
        [(3, 4)],
        [(3, 1)],
        []
    ]
    assert longest_path(graph1) == 7

    graph2 = [
        [(1, 2), (2, 1)],
        [(3, 1)],
        [(3, 5)],
        []
    ]
    assert longest_path(graph2) == 6

    graph3 = [
        [(1, 10)],
        [(2, 10)],
        [(3, 10)],
        []
    ]
    assert longest_path(graph3) == 30

    graph4 = [
        [(1, 1), (2, 1)],
        [(3, 1)],
        [(3, 1)],
        []
    ]
    assert longest_path(graph4) == 2
    # After carefull observation and mannual checking according to me the output of the graph4 (in the test_main.py) should be 2 and not 3 however it may had been mistyped as 3 Above. I am correcting the same and also the code is running according to it

    
    print("All test cases pass")

if __name__ == "__main__":
    pytest.main()
