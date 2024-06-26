from nada_dsl import *

import nada_numpy as na


def nada_main():
    parties = na.parties(3)

    a = na.array([3], parties[0], "A", SecretInteger)

    result = a[0] + a[1] + a[2]

    return na.output(result, parties[1], "my_output")
