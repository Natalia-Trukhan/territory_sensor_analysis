from pathlib import Path

import numpy as np

def read_file(filename) -> np.ndarray:
    data_read = np.genfromtxt(
        filename,
        delimiter=",",
        dtype=None,
        invalid_raise=False,
        encoding="utf-8",
    )
    return data_read

PROJECT_ROOT: Path = Path.cwd()
path_file: Path = PROJECT_ROOT/'data_files'/'sensors.csv'
data: np.ndarray = read_file(path_file)
if __name__ == "__main__":
    print(f"The type={data.dtype}")
    print(f"The matrics format={data.shape}")
    print(f"The number of dimentions={data.ndim}")
    print(data)
    print()

    sectors: np.ndarray = data.reshape(12, 10, 14, 10).transpose(0, 2, 1, 3)
    print(f"""The row sectors: 
    {sectors[0]}
    
    Sector:
    {sectors[0][0]}
    
    The row sensors of sector:
    {sectors[0][0][0]}
    
    The one detector:
    {sectors[0][0][0][0]}
    """, )



