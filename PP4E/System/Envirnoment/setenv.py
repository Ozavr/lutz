import os


print('setenvv...', end=' ')
print(os.environ['USER'])

os.environ['USER'] = 'Brian'
os.system('python3 echoenv.py')

os.environ['USER'] = 'Arthur'
os.system('python3 echoenv.py')

os.environ['USER'] = input('?')
print(os.popen('python3 echoenv.py').read())

