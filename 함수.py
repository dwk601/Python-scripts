def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit_account(balance, money):
    print("입금이 완료되었습니다.. 잔액은 {0} 원입니다.".format(balance+money))
    return balance + money


def withdraw_account(balance, money):
    if balance < money:
        print("잔액이 부족합니다.")
        return balance
    else:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
        return balance - money


def close_account(balance):
    print("계좌가 닫혔습니다. 잔액은 {0} 원입니다.".format(balance))


def main():
    balance = 0
    while True:
        print("1. 계좌 생성")
        print("2. 입금")
        print("3. 출금")
        print("4. 계좌 삭제")
        print("5. 종료")
        menu = int(input("메뉴를 선택하세요: "))
        if menu == 1:
            open_account()
        elif menu == 2:
            balance = deposit_account(balance, int(input("입금할 금액을 입력하세요: ")))
        elif menu == 3:
            balance = withdraw_account(balance, int(input("출금할 금액을 입력하세요: ")))
        elif menu == 4:
            close_account(balance)
            break
        elif menu == 5:
            break
        else:
            print("잘못 입력하셨습니다.")


if __name__ == "__main__":
    main()
