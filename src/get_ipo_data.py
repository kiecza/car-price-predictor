import requests
import pandas as pd
from src.config import get_api_key

def get_ipo_calendar():
    """
    Funkcja pobierająca dane IPO z API FMP
    """
    api_key = get_api_key()
    url = f"https://financialmodelingprep.com/api/v3/ipo_calendar?apikey={api_key}"

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"API error: {response.status_code} - {response.text}")

    data = response.json()
    if "ipoCalendar" not in data:
        raise ValueError("Brak danych IPO w odpowiedzi API.")

    df = pd.DataFrame(data["ipoCalendar"])
    return df


def save_ipo_data(df, path="data/ipo_raw.csv"):
    """
    Zapisuje dane IPO do pliku CSV
    """
    df.to_csv(path, index=False)
    print(f"Zapisano {len(df)} rekordów do {path}")
