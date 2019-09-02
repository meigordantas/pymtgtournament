class Test():

    def __init__(self):
        self.name = 'Igor'

class Arr():
    
    def __init__(self, test):
        self.pessoa = test



v1 = Test()

print(v1)

v2 = Arr(v1)
print(v2.pessoa)
v2.pessoa.name = 'nani'

print(v1.name)



