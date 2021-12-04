def swap(func):
   def обертка(*args, **kwargs):
       arr = args[::-1]
       возврат func(*arr, **kwargs)
   возвратная обертка

def div(x, y, show=False):
    res = x / y
    если показать:
        печать(res)
    возврат res

print(div(2,4, show = False))

div = swap(div)

print(div(2,4, show = False))