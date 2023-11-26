fFv=1 #скорость 1 друга
sFv=2 #скорость 2 друга
dv=5 #скорость собаки
Sstart=400 #расстояние между друзьями в начале пути
#на картинке собака бежит от 2 друга
count=0
S = Sstart
print(S)
t = 0
while int(S) > 0:
    #(S=Sstart + Sdelta) пока не встретились
    if count%2 == 0:
        #Sdelta = fFv * t
        #Sstart + Sdelta = dv * t
        #fFv*t = Sstart - dv * t
        t = S / (dv - fFv) #бежала собака от 2 друга, когда 1 друг удалялся
        #S = S + t * fFv - t * sFv + S1 #расстояние между друзьями
        S=S - t * (sFv - fFv)
    elif count%2 != 0:
        #sFv*t = Sdelta(2)
        #S - Sdelta(2) = dv * t
        #расстояние, которое прошёл 2 друг в прошлый раз, когда собака бежала от 2 до 1
        t = S / (sFv + dv) #бежала собака обратно от 1 друга, когда 1 друг приближался
        S = S - t * (sFv - fFv)
    count += 1
    print(count,'',S)
