import re
from typing import List


class Target:
    def __init__(self, bank: float, in_price: float, out_price: float):
        self.bank = bank
        self.in_price = in_price
        self.out_price = out_price

    def get_fraction(self):
        return self.out_price / self.in_price

    def get_out_price(self):
        return self.out_price

    def get_percent(self):
        return round((self.get_fraction() - 1) * 100, 3)

    def get_bank(self):
        return round(self.bank * self.get_fraction(), 3)

    def __str__(self):
        return f"target: {self.get_out_price()}\n" \
               f"Percent: {self.get_percent()}%\n" \
               f"Bank: {self.get_bank()}"


class StrategyDeal:
    def __init__(self, bank, entry, targets, close):
        self.bank = bank
        self.entry = entry
        self.targets = [
            Target(bank, entry, t) for t in targets
        ]
        self.close = close

    def get_targets(self):
        return [t.get_out_price() for t in self.targets]

    def get_target_percents(self):
        return [t.get_percent() for t in self.targets]

    def get_target_banks(self):
        return [t.get_bank() for t in self.targets]

    def __str__(self):
        targets = "\n\n".join([f"{i} {self.targets[i]}" for i in range(len(self.targets))])
        return f"BANK: {self.bank}\nSTART_PRICE: {self.entry}\nSTOP_PRICE: {self.close}\n\n{targets}"


def deal_from_str(raw_deal: str) -> StrategyDeal:
    regex = re.compile(
        "\s*BANK:(.+)\s*Вход:(.+)\s*Таргет:(.+)\s*Выход:(.+)\s*"
    )
    m = regex.match(raw_deal)
    if m is not None:
        bank = int(m.group(1))
        entry = float(m.group(2))
        targets = [float(t) for t in m.group(3).split(";")]
        close_price = float(m.group(4))
        return StrategyDeal(bank, entry, targets, close_price)
    else:
        return None


def read_data(file_name: str) -> List[StrategyDeal]:
    with open(file_name, 'r') as file:
        lines = file.read()

    raw_deals = lines.split("-----")
    deals = []
    for raw_deal in raw_deals:
        deal = deal_from_str(raw_deal)
        if deal is not None:
            deals.append(deal)
    return deals


def write_data(file_name: str, data):
    with open(file_name, 'w') as file:
        str_deals = [str(d) for d in data]
        file.write("\n\n-----\n\n".join(str_deals))


def main():
    content = read_data('deals.txt')
    write_data('out.txt', content)


if __name__ == '__main__':
    main()
