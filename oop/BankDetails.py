
class BankDetail:
    def __init__(self,cust_id,cust_name,bal):
        self.cust_id=cust_id
        self.cust_name= cust_name,
        self.cust_id = cust_id
        self.bal=bal
    def welcome_message(self):
        print(f'Welcome to SBI,{self.cust_name}')
    def display_details(self):
        print(f'{self.cust_id}-{self.cust_name}-{self.bal}')



