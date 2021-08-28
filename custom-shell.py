def prompt_imput():
    PROMPT = 'jan@program:~$'
    COLOR_PREFIX = '\033[42m'
    COLOR_POSTFIX = '\033[0m '
    return input(COLOR_PREFIX + PROMPT + COLOR_POSTFIX)

def handle_ls():
    print('dict1 dict2 dict3')

def handle_echo(string):
    print(string)

def handle_exit():
    print('bye')
    exit()

while(True):
    command = prompt_imput()
    
    if command == 'ls':
        handle_ls()
    elif command[:4] == 'echo':
        handle_echo(command[5:])
    elif command == 'exit':
        handle_exit()
    else:
        print('Commands available: ls, echo, exit')
