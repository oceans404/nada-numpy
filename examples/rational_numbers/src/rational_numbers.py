from nada_dsl import *
import nada_algebra as na


def nada_main():
    # We define the number of parties
    parties = na.parties(3)

    # We use na.SecretRational to create a secret rational number for party 0
    a = na.SecretRational("my_input_0", parties[0])

    # We use na.SecretRational to create a secret rational number for party 1
    b = na.SecretRational("my_input_1", parties[1])

    # This is a compile time rational number
    c = na.Rational(1.2)

    # The formula below does operations on rational numbers and returns a rational number
    # It's easy to see that (a + b - c) is both on numerator and denominator, so the end result is b
    out_0 = ((a + b - c) * b) / (a + b - c)

    return [
        Output(out_0.value, "my_output_0", parties[2]),
    ]