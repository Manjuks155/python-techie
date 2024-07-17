class Bank:
    bank_name = ""

    def __init__(self, name):
        self.bank_name = name

    def get_name(self):
        print(f"the bank name is {self.bank_name}")


class SubBank(Bank):
    def __init__(self, name, address):
        self.addr = address
        Bank.__init__(self, name)

    def get_sub_bank_details(self):
        print(f"the bank name is {self.bank_name} and the address is {self.addr}")


sub_bank = SubBank('Axis', "Bengaluru")
sub_bank.get_sub_bank_details()
