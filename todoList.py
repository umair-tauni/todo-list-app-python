
class Todo:
    
    @staticmethod
    def welcome(self):
        print('--------------------------------')
        print('Welcome to Todo list app in Python')
        print('---------------------------------')
    
    def menu(self):
        try:
            print('1. Create todo')
            print('2. View tdod')
            print('3. Update todo')
            print('4. Delete todo')
            print('5. Exit program')
            choice = int(input('Choose: '))
            return choice
        except Exception as e:
            print(e)
        
    