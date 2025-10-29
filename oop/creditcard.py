from BankDetails import BankDetail
class creditcards(BankDetail):
    def __init__(self,custid,cust_name,bal,creditscore,status):
        super().__init__(custid,cust_name,bal)
        self.creditscore=creditscore
        self.status=status

    def welcome_message(self):
        print(f'Welcome to SBI,{self.cust_name}')

    def display_ccdetails(self):
        print(f'{self.creditscore}-{self.status}')