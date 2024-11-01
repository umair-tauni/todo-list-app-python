
class Todo:
    # empty list
    tasks_list = []
    total_todos = 0
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
            
    # create method
    def create_todo(self):
        total_tasks = int(input("Enter todo's: "))
        for i in range(1, total_tasks + 1):
            task = input(f'Enter task no {i}: ')
            self.tasks_list.append(task)
            self.total_todos+=1
        print('--------------------------------')
        # print(self.tasks_list)
        print(('Tasks Saved: ' + ', '.join(str(i) for i in self.tasks_list)))
        print('--------------------------------')

# run static method
Todo.welcome()
# create object from class
todo = Todo()
# while loop to run program continuously
while True:
    result = todo.menu()
    if result == 1:
        todo.create_todo()