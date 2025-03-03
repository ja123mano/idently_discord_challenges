import requests_cache
from datetime import timedelta

def convert_currency(from_currency: str, to_currency: str, amount: float) -> float:
    """
    Convert an `amount` of a selected `from_currency` to a selected `to_currency`.

    Parameters
    ----------
    from_currency : str
        Symbol of currency to be converted.
    to_currency : str
        Symbol of currency the amount is to be converted.
    amount : float
        Quantity of currency to convert.

    Returns
    -------
    float
        The total of the converted currency.
    """

    response: requests_cache.AnyResponse = session.get(api_url).json()["rates"]

    if "EUR" not in (from_currency, to_currency) and (from_currency not in response.keys() or to_currency not in response.keys()):
        print("Please select a valid symbol of currency. Valid symbols are:")
        print(", ".join(response.keys()))
        return -1

    amount: float = float(amount)
    if from_currency == "EUR": return amount*response[to_currency]
    elif to_currency == "EUR": return amount/response[from_currency]
    else: return amount*(response[to_currency]/response[from_currency])

def main() -> None:
    """
    Main function of the currency converter.
    
    Verifies the correct modules are installed, then proceeds to ask the user
    the currencies that are involved in the conversion and the amount to convert.
    """

    try:
        global session
        session = requests_cache.CachedSession(cache_name="latest_currencies", expire_after=timedelta(hours=1))
    except ModuleNotFoundError:
        print(f"Please install the module 'requests_cache' to execute this program")
    else:
        global api_url
        api_url = "https://api.frankfurter.dev/v1/latest"
        
        from_cur: str = None
        to_cur: str = None
        amount_cur: str = None
        converted_currency: float = 0.0
        print("CURRENCY CONVERTER")
        print("To stop the program press 'q' at any time")
        print("-----------------------------------------\n")
        
        while True:
            from_cur = input("Symbol of currency to convert = ").upper()
            if from_cur.lower() == "q": break

            to_cur = input("Symbol of converted currency = ").upper()
            if to_cur.lower() == "q": break

            amount_cur = input("Amount of currency to convert = $")
            if amount_cur.lower() == "q": break

            converted_currency = convert_currency(from_cur, to_cur, amount_cur)
            if converted_currency != -1:
                print(f"${float(amount_cur): .3f} {from_cur} = ${converted_currency: .3f} {to_cur}")
            
            print("-----------------------------------------\n")

    return None

if __name__ == "__main__":
    main()