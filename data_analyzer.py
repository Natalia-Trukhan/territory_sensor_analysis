from pathlib import Path

import numpy as np

from cleaner import clean_all_sectors
from data_service import data

ROOT_DIR: Path = Path.cwd()
file_p: Path = ROOT_DIR / 'results' / 'sensors_analysis.csv'

list_array: list[tuple[int, float, float, float, float, float]] = []


def analyze_sector(sector: np.ndarray, sector_number: int) -> None:
    min_temperature: float = np.min(sector)
    max_temperature: float = np.max(sector)
    mean_temperature: float = np.mean(sector)
    median_temperature: float = np.median(sector)
    temperature_range: float = (max_temperature - min_temperature)
    list_array.append(
        (sector_number,
         min_temperature,
         max_temperature,
         mean_temperature,
         median_temperature,
         temperature_range)
    )


def process_data_sectors(all_sectors: np.ndarray) -> None:
    clean_all_sectors(all_sectors)
    sec_num: int = 1
    for r in range(len(all_sectors)):
        for c in range(len(all_sectors[r])):
            sec = all_sectors[r][c]
            analyze_sector(sec, sec_num)
            sec_num += 1


    data_temp: np.ndarray = np.array(list_array, dtype=None)

    np.savetxt(
            file_p,
            data_temp,
            header="sector_num,min_temp,max_temp,mean_temp,median_temp,temp_range",
            delimiter=',',
            fmt='%d,%.2f,%.2f,%.2f,%.2f,%.2f',
            comments='',
    )

if __name__ == "__main__":
    all_sec: np.ndarray = data.reshape(12, 10, 14, 10).transpose(0, 2, 1, 3)
    process_data_sectors(all_sec)
    print(f"The file {file_p.name} has been processed.")
