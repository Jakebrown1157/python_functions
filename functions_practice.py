
def function0():
    print('hello from inside a function')

function0()

storage = []

def function(a,b,c):
    storage.append(a)
    storage.append(b)
    storage.append(c)
    print(storage)

function(1,2,3)

my_list = ['eggs','bacon','toast']

def eat_lunch(my_list):
  if len(my_list) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_list)):
      if i == 0:
        print(f"First I eat {my_list[0]}")
      elif i == 1:
        print(f"Next I eat {my_list[1]}")
      else: 
        print(f"Then I eat {my_list[i]}")
eat_lunch(my_list)