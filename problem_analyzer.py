from pathlib import Path

from data_service import data

import numpy as np


def analyze_sensors_problems():
    sensors: np.ndarray = data.reshape(12, 10, 14, 10).transpose(0, 2, 1, 3)

    num_row_sensors: np.ndarray = sensors.shape[0]
    num_column_sensors: np.ndarray = sensors.shape[1]

    SCRIPT_DIR: Path = Path(__file__).resolve().parent
    output_path: Path = SCRIPT_DIR / "results" / "sensors_problems.csv"

    sector_index: int = 0
    list_data: list[tuple] = []

    for row in range(num_row_sensors):
        for col in range(num_column_sensors):
            sector = sensors[row, col]
            median_sen = np.nanmedian(sensors)
            nan_count = np.isnan(sector).sum()

            too_low_count = (sector < (median_sen - 10)).sum()
            too_high_count = (sector > (median_sen + 10)).sum()

            invalid_count = too_high_count + too_low_count + nan_count
            tuple_data = (sector_index, nan_count, too_low_count, too_high_count, invalid_count)
            sector_index += 1
            list_data.append(tuple_data)

    data_sort: np.ndarray = np.array(
        list_data,
        dtype=None
    )

    np.savetxt(
        output_path,
        data_sort,
        delimiter=",",
        header="sector_index,nan_count,too_low_count,too_high_count,invalid_count",
        fmt="%d,%d,%d,%d,%d",
        comments="",
    )

    print(f"The file {output_path.name} has been created successfully")


if __name__ == "__main__":
    analyze_sensors_problems()
