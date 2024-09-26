supported_currencies = ("USD", "EUR", "JPY", "GBP", "CAD", "CHF", "AUD", "NZD", "SEK", "NOK", "DKK", "INR", "CNY", "BRL", "RUB", "ZAR", "KRW", "MXN", "TRY")

def is_currency_supported(currency: str) -> bool:
    """
    Checks if a given currency is supported.

    Args:
        currency: The currency to check.

    Returns:
        True if the currency is supported, False otherwise.
    """

    if not isinstance(currency, str):
        raise ValueError("Currency must be a string")

    currency = currency.upper()
    return currency in supported_currencies









def main():
    ...


if __name__ == "__main__":
  main()