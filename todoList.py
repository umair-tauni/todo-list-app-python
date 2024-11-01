
class Todo:
    
    # static method
    @staticmethod
    def welcome():
        print('--------------------------------')
        print('Welcome to Todo list app in Python')
        print('---------------------------------')
    
    # display method
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

# run static method
Todo.welcome()
# create object from class
todo = Todo()

    