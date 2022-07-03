from testbook import testbook

def grader():
    points = 0.0
    """
    TASK 1: SGD
    """

    def test_a():
        score_a = 0.0

        try:
            with testbook('./ssnn_solved.ipynb', execute=[1, 3, 5,
                          7]) as tb1:
                if tb1.cell_output_text(7) == 'Test passed.':
                    score_a += 1
                    print('Task 1 Passed.')
        except Exception:
            print('Task 1 failed.')

        return score_a

    points_a = test_a()

    def test_b():
        score_b = 0.0

        try:
            with testbook('./ssnn_solved.ipynb', execute=[1, 3, 9, 11,
                          13]) as tb2:
                if tb2.cell_output_text(13) == 'Test passed.':
                    score_b += 1
                    print('Task 2 Passed.')
        except Exception:
            print('Task 2 failed.')

        return score_b

    points_b = test_b()

    def test_c():
        score_c = 0.0

        try:
            with testbook('./ssnn_solved.ipynb', execute=[1, 3, 11, 15,
                          17]) as tb3:
                if tb3.cell_output_text(17) == 'Test passed.':
                    score_c += 1
                    print('Task 3 Passed.')
        except Exception:
            print('Task 3 failed.')

        return score_c

    points_c = test_c()

    def test_d():
        score_d = 0.0

        try:
            with testbook('./ssnn_solved.ipynb', execute=[1, 3, 19,
                          21]) as tb4:
                if tb4.cell_output_text(21) == 'Test passed.':
                    score_d += 1
                    print('Task 4 Passed.')
        except Exception:
            print('Task 4 failed.')
        return score_d

    points_d = test_d()
    
    points = points_a + points_b + points_c + points_d

    return points

grade = grader()

print('Your score is: ',grade)
