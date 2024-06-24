import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


def get_env_var(key, default_value=None):
    value = os.getenv(key)
    return value if value is not None else default_value


api_key = get_env_var("API_KEY", "")
ifttt_key = get_env_var("IFTTT_KEY", "")


def get_data(symbols=""):
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}&symbols={symbols}&prettyprint=true&show_alternative=false"
    headers = {"accept": "application/json"}

    response = requests.get(url=url, headers=headers)

    return response.text


def send_to_ifttt():
    url = f"https://maker.ifttt.com/trigger/currency_rate/json/with/key/{ifttt_key}"
    headers = {"Content-Type": "application/json"}
    data = get_currency_rate()

    if not data:
        return None

    response = requests.post(url=url, json=data, headers=headers)

    return response.text


def get_currency_rate():
    first_data = json.loads(get_data("PKR,EUR,AED"))
    second_data = json.loads(get_data("GBP,SAR,CAD"))

    try:
        if first_data["error"] or second_data["error"]:
            return None
    except KeyError:
        pass

    pkr_rate = float(first_data["rates"]["PKR"]) if first_data["rates"]["PKR"] else 1
    eur_rate = float(first_data["rates"]["EUR"]) if first_data["rates"]["EUR"] else 1
    aed_rate = float(first_data["rates"]["AED"]) if first_data["rates"]["AED"] else 1

    gbp_rate = float(second_data["rates"]["GBP"]) if second_data["rates"]["GBP"] else 1
    sar_rate = float(second_data["rates"]["SAR"]) if second_data["rates"]["SAR"] else 1
    cad_rate = float(second_data["rates"]["CAD"]) if second_data["rates"]["CAD"] else 1

    eur_rate = pkr_rate / eur_rate
    aed_rate = pkr_rate / aed_rate
    gbp_rate = pkr_rate / gbp_rate
    sar_rate = pkr_rate / sar_rate
    cad_rate = pkr_rate / cad_rate

    return {
        "PKR": round(pkr_rate, 2),
        "EUR": round(eur_rate, 2),
        "AED": round(aed_rate, 2),
        "GBP": round(gbp_rate, 2),
        "SAR": round(sar_rate, 2),
        "CAD": round(cad_rate, 2),
    }


if __name__ == "__main__":
    print(send_to_ifttt())
