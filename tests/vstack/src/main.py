from nada_dsl import *
import nada_algebra as na


def nada_main():
    parties = na.parties(3)

    a = na.array([3], parties[0], "A")
    b = na.array([3], parties[1], "B")

    return a.vstack(b).output(parties[2], "my_output")
