class ExpenseTracker:

    database = {}

    def _get_user_expense(self):
        while True:
            try:
                amount: float = float(input('Amount: '))
                category: str = input('Category: ')
                break
            except ValueError as e:
                print(f'Invalid Input: {e}')
        return amount, category


    def insert_expense(self, expenses) -> None:
        amount, category = self._get_user_expense()
        expenses.append({'amount': amount, 'category': category})
        

    def display_all_current_expenses(self, expenses) -> None:
        for expense in expenses:
            print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')


    def add_all_current_expenses(self, expenses) -> float:
        print(sum(map(lambda expense: expense['amount'], expenses)))


    def _get_user_category_choice(self) -> str:
        user_category: str = input('Which Category: ')
        return user_category

    
    def _filter_expenses_by_category(self, expenses, category):
        return filter(lambda expense: expense['category'] == category, expenses)


    def display_expenses_by_category(self, expenses):
        category = self._get_user_category_choice()
        filtered_expenses_by_category = self._filter_expenses_by_category(expenses, category)
        self.display_all_current_expenses(filtered_expenses_by_category)


    def save_user_data_to_database(self, username: str, expenses) -> None:
        if username in ExpenseTracker.database:
            ExpenseTracker.database[f'{username}'].extend([{'amount': expense['amount'], 'category': expense['category']} for expense in expenses])
        else:
            user_data = {username: [{'amount': expense['amount'], 'category': expense['category']} for expense in expenses]}
            ExpenseTracker.database.update(user_data) 
        expenses.clear()


    def display_all_data_from_database(self) -> None:
        
        for username, expenses in ExpenseTracker.database.items():
            expense_counter = 1
            print(f'Username: {username}')
            for expense in expenses:
                print(f'{expense_counter}. Amount: {expense["amount"]} Category: {expense["category"]}')
                expense_counter = 1



MENU: dict = {
    1: 'Insert an Expense',
    2: 'Display all current expenses',
    3: 'Display current total expenses',
    4: 'Display current expenses by category',
    5: 'Save current user data to database',
    6: 'Display all data from Database',
    7: 'Enter new user',
    8: 'Exit'
}

def get_username() -> str:
    username: str = input("Enter your username: ")
    return username 


def get_user_input(username: str) -> int:
    for index, description in MENU.items():
        print(f'{index}. {description}')
    while True:
        try:
            user_choice: int = int(input('=> '))
            if user_choice < 1 or user_choice > len(MENU):
                print('Choice out of range!')
                continue
            return user_choice
        except ValueError:
            print('Invalid Input!')




def main() -> None:
    while True:
        expenses = []
        print("EXPENSE TRACKER\n")
        username: str = get_username()
        
        expenseTracker: ExpenseTracker = ExpenseTracker()

        print(f'\nWelcome {username}! Choose from the options below.\n')
        while True:
            user_choice: int = get_user_input(username)
            match user_choice:
                case 1: expenseTracker.insert_expense(expenses)
                case 2: expenseTracker.display_all_current_expenses(expenses)
                case 3: expenseTracker.add_all_current_expenses(expenses)
                case 4: expenseTracker.display_expenses_by_category(expenses)
                case 5: expenseTracker.save_user_data_to_database(username, expenses)
                case 6: expenseTracker.display_all_data_from_database()
                case 7: break
                case 8: return
                case _: continue
        continue


if __name__ == '__main__':
    main()

    
    