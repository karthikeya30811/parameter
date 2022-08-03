name = int((input("enter the choice")))
if (name == 1):
    print("find perimeter and area of rectangle")
    n = int(input("enter the values"))
    n1 = int(input("enter the value"))
    k =  n*n1
    print("area of rectanlge",k)
    k1 = (2*(n+n1))
    print("perimeter of rectanlge",k1)
elif (name == 2):


   print("find the perimeter and area of Circle")
   r = float(input("enter the radius"))
   PI = 3.14
   M = (PI*r*r)
   print("area of the circle",M)
   A = (2*PI*r)
   print("Perimeter of the circle",A)
elif (name == 3):



    print("Find the perimeter of triangle and area")
    a = float(input("enter the value 1"))
    b = float(input("enter the value 2"))
    c = float(input("enter the value 3"))
    s = (a+b+c)
    print("perimerter of triangle",s)
    area =  (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print("area of triangle ",area)






