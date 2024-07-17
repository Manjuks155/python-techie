import types


class Bank:
    bank_city = "Bengaluru"

    def __init__(self, bank_name, bank_code):
        self.bank_name = bank_name
        self.bank_code = bank_code

    def get_bank_instance_details(self):
        print(f"bank city is : {self.bank_city}")
        print(f"bank name is : {self.bank_name}")
        print(f"bank code is : {self.bank_code}")
        # self.bank_city = "Gauribidanur"
        # self.__class__.bank_city = 'Mysore'
        Bank.bank_city = "Mysore"

    @classmethod
    def get_bank_class_details(self):
        print(f"bank city is : {self.bank_city}")
        print(f"bank name is : {self.bank_name}")
        print(f"bank code is : {self.bank_code}")

    @staticmethod
    def get_bank_static_details(self):
        print(f"bank city is : {self.bank_city}")
        print(f"bank name is : {self.bank_name}")
        print(f"bank code is : {self.bank_code}")


hdfc_bank = Bank('HDFC', 55)
hdfc_bank.get_bank_instance_details()
print("_____________________________________________________________________")
hdfc_bank.get_bank_instance_details()
print("_____________________________________________________________________")
# hdfc_bank.get_bank_class_details()
# hdfc_bank.get_bank_static_details()

axis_bank = Bank('AXIS', 100)
axis_bank.get_bank_instance_details()
print("_____________________________________________________________________")
axis_bank.get_bank_instance_details()
