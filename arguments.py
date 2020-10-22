# *args  and  # **kwargs

# normal way

# def func_name_print(a,b,c,d,e):
#     print(a,b,c,d,e)
# func_name_print("harry","vishmay","rohan","marry","shiva")



def fargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\nand here let me introduce u")
    for key,value in kwargs.items():
        print(f"{key} is a {value}")


n1="this is normal"

har=["harry","vishmay","rohan","marry","shiva"]

kw={"harry":"worker","vishmay":"CEO","satyam":"manager"}

fargs(n1,*har,**kw)