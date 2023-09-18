accounts = []
transactions = []


class Transaction:
    def __init__(self, name, amount, from_account, to_account):
        self.name = name
        self.amount = amount
        self.from_account = from_account
        self.to_account = to_account


class Account:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number


def account_exists(func):
    def check_account(name, amount, from_account, to_account):

        account_nums = []
        for account in accounts:
            account_nums.append(account.account_number)

        if not (from_account in account_nums or to_account in account_nums):
            raise Exception("one of the accounts in this transaction does not exist")
        res = func
        return res

    return check_account


def positive_amount(func):
    def check_amount(name, amount, from_account, to_account):
        if amount <= 0:
            raise Exception("amount must be $1 or greater")
        res = func
        return res

    return check_amount


@account_exists
@positive_amount
def create_new_transaction(name, amount, from_account, to_account):
    new_transaction = Transaction(name, amount, from_account, to_account)
    transactions.append(new_transaction)
    return new_transaction


def create_account(name, account_number):
    new_account = Account(name, account_number)
    accounts.append(new_account)
    return new_account


def show_transactions():
    for transaction in transactions:
        print(transaction.name + " ")
        print(transaction.amount + " ")
        print(transaction.from_account + " ")
        print(transaction.to_account + " ")


if __name__ == '__main__':
    create_account("Joe", "2001022")
    create_account("Tim", "1110029")
    create_new_transaction("Joe", "200", "2001022", "1110029")
    show_transactions()
