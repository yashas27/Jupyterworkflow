from jwf.data import get_fremont_data
import pandas as pd

def test_fremont_data():
    data = get_fremont_data()
    assert all(data.columns == ['Total', 'East', 'West'])
    assert isinstance(data.index, pd.DatetimeIndex)

