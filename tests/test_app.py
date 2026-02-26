import pytest
from app import (
    kg_to_grams,
    grams_to_kg,
    kg_to_pounds,
    pounds_to_kg,
    grams_to_pounds,
    pounds_to_grams,
)

# Test 1: kg to grams
def test_kg_to_grams():
    assert kg_to_grams(1) == 1000
    assert kg_to_grams(2) == 2000


# Test 2: grams to kg
def test_grams_to_kg():
    assert grams_to_kg(1000) == 1
    assert grams_to_kg(500) == 0.5


# Test 3: kg to pounds
def test_kg_to_pounds():
    assert pytest.approx(kg_to_pounds(1), rel=1e-5) == 2.20462
    assert pytest.approx(kg_to_pounds(5), rel=1e-5) == 11.0231


# Test 4: pounds to kg
def test_pounds_to_kg():
    assert pytest.approx(pounds_to_kg(2.20462), rel=1e-5) == 1
    assert pytest.approx(pounds_to_kg(11.0231), rel=1e-5) == 5


# Test 5: grams to pounds
def test_grams_to_pounds():
    assert pytest.approx(grams_to_pounds(1000), rel=1e-5) == 2.20462


# Test 6: pounds to grams
def test_pounds_to_grams():
    assert pytest.approx(pounds_to_grams(2.20462), rel=1e-3) == 1000