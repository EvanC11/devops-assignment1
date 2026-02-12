import pytest
from app import (
    kg_to_grams,
    grams_to_kg,
    kg_to_pounds,
    pounds_to_kg,
    grams_to_pounds,
    pounds_to_grams,
)

# Example cases for conversion functions
def test_kg_to_grams():
    # test that 1 kg is equal to 1000 grams
    # if this test fails, the function kg_to_grams is incorrect
    assert kg_to_grams(1) == 1000

def test_grams_to_kg():
    # test that 1000 grams is equal to 1 kg
    # if this test fails, the function grams_to_kg is incorrect
    assert grams_to_kg(1000) == 1

def test_kg_to_pounds():
    # test that 1 kg is equal to 2.20462 pounds
    # if this test fails, the function kg_to_pounds is incorrect
    assert pytest.approx(kg_to_pounds(1), rel=0.01) == 2.20462

def test_pounds_to_kg():
    # test that 2.20462 pounds is equal to 1 kg
    # if this test fails, the function pounds_to_kg is incorrect
    assert pytest.approx(pounds_to_kg(2.20462), rel=1e-5) == 1

def test_grams_to_pounds():
    # test that 1000 grams is equal to 2.20462 pounds
    # if this test fails, the function grams_to_pounds is incorrect
    assert pytest.approx(grams_to_pounds(1000), rel=1e-5) == 2.20462

