"""
Functions moved out of the notebooks for cleaner code
"""

import polars as pl


def convert_time_to_hour_base(data, hour, time_col="time"):
    """For polars dataframes to convert timestamp to 9 am.
    Both HadUK-Grid and CEH-GEAR are base 9am-9am, but the
    data is stored differently."""
    return data.with_columns(
        pl.datetime(
            pl.col(time_col).dt.year(),
            pl.col(time_col).dt.month(),
            pl.col(time_col).dt.day(),
            hour,
            0,
            0,
        ).alias(time_col)
    )
