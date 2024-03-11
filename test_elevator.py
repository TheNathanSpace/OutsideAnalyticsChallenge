import elevator

if __name__ == '__main__':
    """
    Test input/output given in problem description
    """
    output = elevator.Elevator("12", "2,9,1,32").run()
    expected = "560 12,2,9,1,32"
    assert output == expected, f"Simple input: {output}, expected {expected}"

    """
    Test more generic input/output
    """
    output = elevator.Elevator("1", "2,3,4,5,6").run()
    expected = "50 1,2,3,4,5,6"
    assert output == expected, f"Simple input: {output}, expected {expected}"

    """
    Test when no floors are given
    """
    output = elevator.Elevator("12", "").run()
    expected = "0 12"
    assert output == expected, f"Visit no floors: {output}, expected {expected}"

    """
    Test with negative floors
    """
    output = elevator.Elevator("3", "-5, 2, -1, 0").run()
    expected = "190 3,-5,2,-1,0"
    assert output == expected, f"Negative floors: {output}, expected {expected}"
