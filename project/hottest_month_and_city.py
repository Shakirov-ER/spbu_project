import argparse
import warnings
import zipfile

import pandas as pd

warnings.filterwarnings("ignore")


def parse_data(
    archive="archive.zip", filepath="GlobalLandTemperaturesByMajorCity.csv"
) -> pd.DataFrame:
    """Parse data from zip file

    Args:
        archive (str, optional): zip file path.
        filepath (str, optional): data file path in zip.

    Returns:
        DataFrame: parsed from file
    """
    with zipfile.ZipFile("archive.zip") as z:
        with z.open(filepath) as f:
            df = pd.read_csv(f, parse_dates=["dt"])

    df["year"] = df["dt"].dt.year
    df["month"] = df["dt"].dt.month

    return df


def get_hottest_month_and_city(archive: str, file: str, year: int) -> dict:
    """Get hottest month and city from data

    Args:
        archive (str): zip path
        file (str): file path in zip
        year (int): some year

    Returns:
        dict: {"hottest_month": month, "hottest_city": city}
    """
    data = parse_data(archive, file)
    data = data[data.year == year]
    grouped = data.groupby(["City", "month"])

    max_temp = grouped["AverageTemperature"].max()
    city, month = max_temp.idxmax()
    return {"hottest_month": month, "hottest_city": city}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the hottest month and city")
    parser.add_argument("archive", type=str, help="Path to the archive file")
    parser.add_argument("file", type=str, help="Path to the input csv file in archive")
    parser.add_argument("year", type=int, help="Year to filter the data")
    args = parser.parse_args()
    result = get_hottest_month_and_city(args.archive, args.file, args.year)
    print(result)
