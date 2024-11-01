
class Todo:
    # empty list
    todo_list = []
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
            print('2. View todo')
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
            if task in self.todo_list:
                print(f'Todo with this {task} name alredy exist')
            else:
                self.todo_list.append(task)
                self.total_todos+=1
        print('--------------------------------')
        # print(self.todo_list)
        print(('Tasks Saved: ' + ', '.join(str(i) for i in self.todo_list)))
        print('--------------------------------')

    # view method
    def view_todo(self):
        print('-----------------------------------')
        print('Total tasks:', self.total_todos)
        print("Todo's:", self.todo_list)
        print('-----------------------------------')
    
    # update method
    def update_todo(self):
        task = input('Enter task you want to update: ')
        if task not in self.todo_list:
            print('------------------')
            print('Task not exist..')
            print('-------------------')
        else:
            updated_task = input('Enter Updated Task: ')
            ind = self.todo_list.index(task)
            self.todo_list[ind] = updated_task
            print('--------------------------')
            print('Task Updated Successfully..', self.todo_list)
            print('---------------------------')
    
    # delete method
    def delete_todo(self):
        task = input('Enter task you want to delete: ')
        if task not in self.todo_list:
            print('------------------')
            print('Task not exist..')
            print('-------------------')
        else:
            ind = self.todo_list.index(task)
            del self.todo_list[ind]
            print('--------------------------')
            print('Task Deleted Successfully..', self.todo_list)
            print('---------------------------')
    
    

# run static method
Todo.welcome()
# create object from class
todo = Todo()
# while loop to run program continuously
while True:
    result = todo.menu()
    if result == 1:
        todo.create_todo()
    elif result == 2:
        todo.view_todo()
    elif result == 3:
        todo.update_todo()
    elif result == 4:
        todo.delete_todo()