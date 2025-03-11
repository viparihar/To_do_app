def get_todos(file):
    with open(file, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos, file):
    with open(file, 'w') as file:
        file.writelines(todos)
print(__name__)
# __name__ is used to control what we show in the import functions
if __name__ == "__main__":
    print("Hello")
