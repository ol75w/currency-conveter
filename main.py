import requests

api="https://api.exchangerate.fun/latest"

def get_exchange_rate(from_currency, to_currency):
    try:
        response = requests.get(
            api,
            params={"base": from_currency},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        rates = data["rates"]

        if to_currency not in rates:
            print("Invalid input or currenct!")
            return None
        return rates[to_currency]
    
    except requests.exceptions.RequestException:
        print("Unable to connect to exchange rate service!")
        return None

    except (KeyError, ValueError):
        print("Invalid response recived from api!")
        return None

def convert_currency(amount, rate):
    return amount * rate

def main():
    print("\n=====Currency Coverter======")

    while True:
        try:
            amount = float(input("\nEnter amount: "))

            if amount <= 0:
                print("Amount must be greater than Zero!")
                continue
            break
        except ValueError:
            print("Please enter a valid Number")

    from_currency = input("From Currency: ").strip().upper()
    to_currency = input("To Currency: ").strip().upper()
    if not from_currency or not to_currency:
        print("Currency codes can not be empty.")
        return
    if from_currency == to_currency:
        print(f"\n{amount:.2f} {from_currency} = {amount:.2f} {to_currency}")
        return
    rate = get_exchange_rate(from_currency, to_currency)
    if rate is None:
        return
    result = convert_currency(amount, rate)
    print("\n===== CONVERSION RESULT =====")
    print(f"Amount: {amount:.2f} {from_currency}")
    print(f"Exchange rate: 1 {from_currency} = {rate} {to_currency}")
    print(f"Converted amount: {result:.2f} {to_currency}")


if __name__ == "__main__":
    main()