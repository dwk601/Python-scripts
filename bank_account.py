# write code in english
# make a bank account class containing the following attributes:
# creating an account, depositing, withdrawing, closing an account, and commission fee.
# The commission fee is 0.1% of the amount deposited.
# Run it as main function.

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.commission = 0.1

    def open_account(self):
        print("새로운 계좌가 생성되었습니다.")

    def deposit_account(self, money):
        self.balance += money
        print("입금이 완료되었습니다.. 잔액은 {0} 원입니다.".format(self.balance))
        return self.balance

    def withdraw_account(self, money):
        if self.balance < money:
            print("잔액이 부족합니다.")
            return self.balance
        else:
            self.balance -= money
            self.balance -= self.commission * money
            print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(self.balance))
            return self.balance

    def close_account(self):
        print("계좌가 닫혔습니다. 잔액은 {0} 원입니다.".format(self.balance))

    def main(self):
        while True:
            print("1. 계좌 생성")
            print("2. 입금")
            print("3. 출금")
            print("4. 계좌 삭제")
            print("5. 종료")
            menu = int(input("메뉴를 선택하세요: "))

            if menu == 1:
                self.open_account()
            elif menu == 2:
                self.balance = self.deposit_account(
                    int(input("입금할 금액을 입력하세요: ")))
            elif menu == 3:
                self.balance = self.withdraw_account(
                    int(input("출금할 금액을 입력하세요: ")))
            elif menu == 4:
                self.close_account()
                break
            elif menu == 5:
                break

            else:
                print("잘못 입력하셨습니다.")


if __name__ == "__main__":
    account = BankAccount()
    account.main()
    print("종료합니다.")
    print("잔액은 {0} 원입니다.".format(account.balance))  # 잔액은 0 원입니다.
