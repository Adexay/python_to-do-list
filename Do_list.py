tasks=[]
def add():
  task=input('Enter a task: ')
  tasks.append(task)
  print('Task has been added successfully!')
  save()
def view():
  if tasks:
    print('\nYour Task: ')
    for i,task in enumerate(tasks,start=1):
      print(f'{i}.{task}')
  else:
    print('No tasks available.')
    save()
def mark():
  number=int(input('Enter task number: '))
  if 1<=number<=len(tasks):
    if not tasks[number-1].startswith('✔'):
      tasks[number-1]='✔'+tasks[number-1]
      print('Task marked as complete')
    else:
      print('Task already completed!')
  else:
    print('Invalid Task number.')
    save()
def delete():
  number=int(input('Enter the task number you want to delete'))
  if 1<=number<=len(tasks):
    tasks.pop(number-1)
    print('Task deleted successfully!')
  else:
    print('Invalid Task number')
    save()
def save():
  with open('tasks.txt','w') as file:
    for task in tasks:
      file.write(task+'\n')
  print('Tasks saved successfully!')
def main():
  while True:
    print('=== TO-DO LIST ===')
    print('1. Add Task')
    print('2. View Tasks')
    print('3. Mark Task as completed')
    print('4. Delete Task')
    print('5. Save Tasks')
    print('6. Exit')
    choice=(input('Choose an option: '))
    if choice=='1':
      add()
    elif choice=='2':
      view()
    elif choice=='3':
      mark()
    elif choice=='4':
      delete()
    elif choice=='5':
      save()
    elif choice=='6':
      save()
      print('Goodbye!')
      break
if __name__=='__main__':
  main()
