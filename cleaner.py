import numpy as np

from data_service import data, path_file


def clean_sector(sector: np.ndarray) -> None:
    median_sec: np.ndarray = np.nanmedian(sector)
    for row_sec in range(10):
        for col_sec in range(10):
            temp = sector[row_sec, col_sec]
            if np.isnan(temp) or (temp > (median_sec + 10)) or (temp < (median_sec - 10)):
                sector[row_sec][col_sec] = median_sec


def clean_all_sectors(all_sectors: np.ndarray) -> None:
    row: np.ndarray = all_sectors.shape[0]
    column: np.ndarray = all_sectors.shape[1]

    for sector_row in range(row):
        for sector_column in range(column):
            sector_ = all_sectors[sector_row][sector_column]

            clean_sector(sector_)


if __name__=="__main__":
    all_sec: np.ndarray = data.reshape(12, 10, 14, 10).transpose(0, 2, 1, 3)
    print(f"Total amount nan in the file {path_file.name}={np.isnan(all_sec).sum()}")
    clean_all_sectors(all_sec)
    print(f"Total amount nan in the file {path_file.name}={np.isnan(all_sec).sum()}")
