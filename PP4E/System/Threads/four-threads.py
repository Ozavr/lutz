import _thread, threading


def action(i):
    print(i ** 32)


# подкласс, хранящий собственную информацию о состоянии
class MyThread(threading.Thread):
    def __init__(self, i):
        self.i = i
        threading.Thread.__init__(self)

    def run(self):
        print(self.i ** 32)


MyThread(2).start()

# передача простой функции
thread = threading.Thread(target=lambda: action(2))
thread.start()

# то же самое, но без lambda-функции,
# сохраняющей информацию о состоянии в образуемом ею замыкании
threading.Thread(target=action, args=(2,)).start()

# с помощью модуля thread
_thread.start_new_thread(action, (2,))


# обычный класс с атрибутами, ООП
class Power:
    def __init__(self, i):
        self.i = i

    def action(self):
        print(self.i ** 32)

obj = Power(2)
threading.Thread(target=obj.action).start()


# вложенная область видимости, для сохранения информации о состоянии
def action(i):
    def power():
        print(i ** 32)
    return power

threading.Thread(target=action(2)).start()

_thread.start_new_thread(obj.action, ())
_thread.start_new_thread(action, (2,))