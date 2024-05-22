import os
import pytest
import subprocess

TESTS = [
    "base",
    "dot_product",
    "sum",
    "broadcasting_sum",
    "broadcasting_sub",
    "broadcasting_mul",
    "broadcasting_div",
    "broadcasting_vec",
    "hstack",
    "vstack",
    "reveal",
    "matrix_multiplication",
    "get_item",
    "get_attr",
    "set_item",
    "gauss_jordan",
]

EXAMPLES = [
    "dot_product",
    "matrix_multiplication",
]

TESTS = ["tests/" + test for test in TESTS] + ["examples/" + test for test in EXAMPLES]


@pytest.fixture(params=TESTS)
def testname(request):
    return request.param


def build_nada(test_dir):
    result = subprocess.run(
        ["nada", "build"], cwd=test_dir, capture_output=True, text=True
    )
    if result.returncode != 0:
        pytest.fail(f"Build failed: {result.stderr}")


def run_nada(test_dir):
    result = subprocess.run(
        ["nada", "test"], cwd=test_dir, capture_output=True, text=True
    )
    if result.returncode != 0:
        pytest.fail(f"Tests failed: {result.stderr}")


class TestSuite:

    def test_build(self, testname):
        # Get current working directory
        cwd = os.getcwd()
        try:
            # Change to specific nada project directory
            os.chdir(testname)
            # Build Nada Program
            build_nada(os.getcwd())
        finally:
            # Return to initial directory
            os.chdir(cwd)

    def test_run(self, testname):
        # Get current working directory
        cwd = os.getcwd()
        try:
            # Change to specific nada project directory
            os.chdir(testname)
            # Execute Tests on Program
            run_nada(os.getcwd())
        finally:
            # Return to initial directory
            os.chdir(cwd)


def test_client():
    import nada_algebra.client as na_client  # For use with Python Client
    import py_nillion_client as nillion
    import numpy as np

    parties = na_client.parties(3)

    assert parties is not None

    secrets = nillion.Secrets(
        na_client.concat(
            [
                na_client.array(np.ones((3, 3)), "A"),
                na_client.array(np.ones((3, 3)), "B", nillion.SecretUnsignedInteger),
            ]
        )
    )

    assert secrets is not None

    public_variables = nillion.PublicVariables(
        na_client.concat(
            [
                na_client.array(np.zeros((4, 4)), "C", nillion.PublicVariableInteger),
                na_client.array(
                    np.zeros((3, 3)), "D", nillion.PublicVariableUnsignedInteger
                ),
            ]
        )
    )

    assert public_variables is not None
