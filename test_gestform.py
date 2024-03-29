import pytest

from gestform import evaluate_number


@pytest.mark.parametrize(
    "input_number, expected_output",
    [
        (3, "Geste"),
        (-9, "Geste"),
        (5, "Forme"),
        (-25, "Forme"),
        (15, "Gestform"),
        (-45, "Gestform"),
        (7, "7"),
        (-88, "-88"),
    ],
)
def test_evaluate_number(input_number, expected_output):
    assert evaluate_number(input_number) == expected_output
