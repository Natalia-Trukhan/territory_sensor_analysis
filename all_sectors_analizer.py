from pathlib import Path

import numpy as np

from data_analyzer import process_data_sectors
from data_service import data

ROOT_DIR: Path = Path.cwd()
file_path: Path = ROOT_DIR / 'results' / 'all_sectors.csv'
input_file: Path = ROOT_DIR / "results" / "sensors_analysis.csv"


def category_sectors() -> None:
    sector_list: list[tuple[int, float]] = []

    read_data: np.ndarray = np.genfromtxt(
        input_file,
        delimiter=',',
        names=True,
        dtype=None,
        encoding="utf-8"
    )

    for row in read_data:
        index: int = int(row["sector_num"])
        mean_temp: float = float(row["mean_temp"])
        sector_list.append((index, mean_temp))

    all_mean_temp: list[float] = [mean[1] for mean in sector_list]
    average_mean_temp: float = sum(all_mean_temp) / len(all_mean_temp)

    sorted_mean_temp: list[tuple[int, float]] = sorted(sector_list, key=lambda x: x[1])

    warmest_temp: list[tuple[int, float]] = sorted_mean_temp[-10:]
    coldest_temp: list[tuple[int, float]] = sorted_mean_temp[:10]

    sorted_list: list[tuple[int, float]] = sorted(sector_list, key=lambda x: abs(x[1] - average_mean_temp))
    closest_temp: list[tuple[int, float]] = sorted_list[:30]

    all_indexes_category: list[tuple[int, str]] = []

    for index, _ in warmest_temp:
        row = (index, "the warmest sector")
        all_indexes_category.append(row)

    for index, _ in coldest_temp:
        row = (index, "the coldest sector")
        all_indexes_category.append(row)

    for index, _ in closest_temp:
        row = (index, "the closes sector to mean temp")
        all_indexes_category.append(row)

    data_write = np.array(
        all_indexes_category,
        dtype= [('idx', 'i4'), ('cat', 'U50')]
    )

    np.savetxt(
        file_path,
        data_write,
        delimiter=',',
        header="sector_index,category",
        comments="",
        fmt="%d,%s"
    )

    print(f"The file {file_path.name} has been created")


if __name__ == "__main__":
    all_sec: np.ndarray = data.reshape(12, 10, 14, 10).transpose(0, 2, 1, 3)
    process_data_sectors(all_sec)
    category_sectors()
