import pytest
from datetime import datetime

# All of the Acts
def validate_symbol(symbol):
    return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7

def validate_chart_type(chart_type):
    return chart_type in {'1', '2'}

def validate_time_series(time_series):
    return time_series in {'1', '2', '3', '4'}

def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_date_range(start_date, end_date):
    try:
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        return end >= start
    except ValueError:
        return False

# All of the Asserts and results!
def test_validate_symbol():
    assert validate_symbol("AAPL") is True  # Valid symbol
    assert validate_symbol("GOOG") is True  # Valid symbol
    assert validate_symbol("TSLA12") is False  # Contains numbers
    assert validate_symbol("aapl") is False  # Not uppercase
    assert validate_symbol("") is False  # Empty string
    assert validate_symbol("YOUTUBEDOTCOM") is False  # Exceeds 7 characters

def test_validate_chart_type():
    assert validate_chart_type("1") is True  # Valid chart type
    assert validate_chart_type("2") is True  # Valid chart type
    assert validate_chart_type("3") is False  # Invalid chart type
    assert validate_chart_type("A") is False  # Non-numeric character
    assert validate_chart_type("") is False  # Empty string

def test_validate_time_series():
    assert validate_time_series("1") is True  # Valid time series
    assert validate_time_series("2") is True  # Valid time series
    assert validate_time_series("5") is False  # Invalid time series
    assert validate_time_series("A") is False  # Non-numeric character
    assert validate_time_series("") is False  # Empty string

def test_validate_date_format():
    assert validate_date_format("2023-01-01") is True  # Valid date
    assert validate_date_format("2023-13-01") is False  # Invalid month
    assert validate_date_format("2023-01-32") is False  # Invalid day
    assert validate_date_format("01-01-2023") is False  # Incorrect format
    assert validate_date_format("") is False  # Empty string

def test_validate_date_range():
    assert validate_date_range("2023-01-01", "2023-01-02") is True  # Valid range
    assert validate_date_range("2023-01-02", "2023-01-01") is False  # End date earlier than start date
    assert validate_date_range("2023-01-01", "2023-01-01") is True  # Same start and end date
    assert validate_date_range("2023-01-01", "yuxyrufivuo") is False  # Invalid end date
    assert validate_date_range("invalid-date", "2023-01-02") is False  # Invalid start date

