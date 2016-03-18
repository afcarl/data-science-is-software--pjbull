import tempfile
import unittest

import numpy as np
import pandas as pd

from build_features import gimme_the_mean, remove_invalid_data


class TestBuildFeatures(unittest.TestCase):
    def setUp(self):
        self.file = tempfile.NamedTemporaryFile(delete=True)
        self.path = self.file.name

        rand_df = pd.DataFrame({'a': np.random.normal(0, 1, 100),
                                'b': np.random.normal(0, 1, 100)})

        rand_df.to_csv(self.path)

    def test_remove_invalid_data(self):
        df = remove_invalid_data(self.path)
        self.assertEqual(df.shape, (100, 2))

    def test_gimme_the_mean(self):
        data = [0]*10
        actual = gimme_the_mean(data)
        self.assertEqual(actual, 0)

    def test_gimme_the_mean_expected_fail(self):
        data = "i am a string"

        with self.assertRaises(TypeError):
            gimme_the_mean(data)

    def tearDown(self):
        # close temp file (it is removed automatically)
        self.file.close()

if __name__ == '__main__':
    unittest.main()
