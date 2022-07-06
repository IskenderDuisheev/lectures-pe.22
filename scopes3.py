# global -> позволяет менять значение глобальной переменной находясь в локальной области видимости
# nonlocal -> позволяет менять значение не локальной переменной находясь в локальной области видимости

#var = 100 

#def increment ():
 #   global var 
  #  var + 1
  #  print(var)
 #   increment()
 #   increment()
  #  increment()
  #  increment()
  #  print(var)

 # def counter() :
 #   num = 0
  #  def incrementer():
  #      nonlocal num
  #      num += 1
   #     return num
  #  return incrementer 

 #c = counter ()
 #print(c()) # 1
 #print(c()) # 2
 #print(c()) # 3

# print(len(dir(__builtins__)))
# print(abs(-15)) #Стандартный вызов встроенной функции
# abs = 15 # Переопределяю встроенное имя abs в глобальной области
# del abs
# print(abs(-15))
# list = ([1,2,3] , [3,3,5], [5,6,5], [12,3,34])
# res = [sum(x) for x in list]
# print(res)

# ------------------------------------------
alice = [13, 15, 38]
john = [5, 15, 50]


[54, 20, 10]
[10, 35, 15]

alice = [54, 20, 10]
john = [10, 35, 15]

def comparescores(a, j):
    score_a = 0
    score_j = 0
    for i in range(0, len(a)):
        if a(1) > j(1):
            score_a += 1
        elif j(1) > a(1):
            score_j += 1
        else:
            pass
    return ('Alice': score_a, 'John': score_j)
    print(comparescores(alice, john))


