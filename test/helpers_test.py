import random
import unittest

import numpy as np


def random_point():
    # tzwhere does not work for points with more latitude!
    return random.uniform(-180, 180), random.uniform(-84, 84)


def list_of_random_points(length):
    return [random_point() for i in range(length)]


class HelperTest(unittest.TestCase):
    import timezonefinderL.helpers as helpers
    fct_dict = {
        "coord2int": helpers.coord2int,
        "inside_polygon": helpers.inside_polygon,
    }
    print('\ntesting helpers.py functions...')

    # use only numpy data structures, because the functions are reused for testing the numba helpers

    def test_inside_polygon(self):

        inside_polygon = self.fct_dict['inside_polygon']
        if inside_polygon is None:
            print('test inside polygon skipped.')
            return

        polygon_test_cases = [
            ([0.5, 0.5, -0.5, -0.5, 0.5], [0.0, 0.5, 0.5, -0.5, -0.5]),
        ]

        p_test_cases = [

            # (x,y),
            # inside
            (0, 0.000),
            #
            # # outside
            (-1, 1),
            (0, 1),
            (1, 1),
            (-1, 0),
            (1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),

            # on the line test cases
            # inclusion is not defined if point lies on the line
            # (0.0, -0.5),
            # (0, 0.5),
            # (-0.5, 0),
            # (0.5, 0),
        ]
        expected_results = [
            (True, False, False, False, False, False, False, False, False),
            # (True, True, True, True)
        ]

        n = 0
        for coords in polygon_test_cases:
            i = 0
            for x, y in p_test_cases:
                assert inside_polygon(x, y, np.array(coords)) == expected_results[n][i]
                i += 1
            n += 1

        # test for overflow:
        # make numpy overflow runtime warning raise an error
        np.seterr(all='warn')
        import warnings
        warnings.filterwarnings('error')
        # delta_y_max * delta_x_max = 180x10^7 * 360x10^7
        coords = np.array([[0.0, self.fct_dict['coord2int'](360.0), 0.0],
                           [0.0, self.fct_dict['coord2int'](180.0), self.fct_dict['coord2int'](180.0)]])
        x, y = 1, 1  # choose so (x-x_i) and (y-y_i) get big!
        assert inside_polygon(x, y, np.array(coords))


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(HelperTest)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
