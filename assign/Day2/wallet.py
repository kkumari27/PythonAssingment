def wallet(balance):
    def deposit(amount):
        nonlocal balance
        balance = balance + amount
        print(amount, " deposited to wallet. New Balance: ", balance)

    def spend(amount):
        nonlocal balance

        if amount <= balance:
            balance = balance - amount
            print(amount, " deducted from wallet. New Balance: ", balance)
        else:
            print("Insufficient Balance")

    def show():
        print("Available Balance: ", balance)

    def transfer(wal, amount):
        nonlocal balance
        if amount <= balance:
            balance = balance - amount
            dic = wal
            dic["deposit"](amount)
            print(amount, " deducted from wallet. New Balance: ", balance)

    d1 = {"deposit": deposit, "spend": spend(), "show": show, "transfer": transfer}
    return d1


d1 = wallet(1000)
d1["transfer"](wallet(40), 500)
d1["show"]()
d1["deposit"](400)
d1["spend"](900)
