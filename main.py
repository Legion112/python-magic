# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class CallMixin:
    def __getattr__(self, name):
        methods = list(filter(lambda functionName: not functionName.startswith('__'), dir(self)))

        raise AttributeError(f'Maybe you mean one of those: {methods}')
    pass

class A(CallMixin):
    def existedFunction(self):
        print('This is the exist function')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = A()
    a.aNotExistingFunction()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
