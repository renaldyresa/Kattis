while True :
     w,l = map(int,input().split())
     if w==0 and l==0 :
         break
     ak = int(input())
     x1 , y1 ,x,y= 0,0,0,0
     for i in range(ak):
         gerak , byk = map(str,input().split())
         byk = int(byk)
         if gerak == "u" :
             y1 += byk
             if y+byk<l :
                 y += byk
             else :
                 y = l-1
         elif gerak == "d" :
             y1 -= byk
             if y-byk>=0 :
                 y -= byk
             else :
                 y = 0
         elif gerak == "r" :
             x1 += byk
             if x+byk<w :
                 x += byk
             else :
                 x = w-1
         elif gerak == "l" :
             x1 -= byk
             if x - byk >= 0 :
                 x -= byk
             else :
                 x = 0
     print("Robot thinks",x1,y1)
     print("Actually at",x,y)
     print()
