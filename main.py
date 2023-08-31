todos = []
while True:
    user_action = input("enter add show,edit,complete or exit:")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                print(f"{index + 1}-{item}")
        case 'edit':
            number = int(input("Number of todo to edit:"))
            number = number - 1
            todos[number] = input("Enter new todo:")
        case 'complete':
            num = int(input("Enter number of todo 2 complete:"))
            todos.pop(num-1)

        case 'exit':
            break
print("Bye!")

