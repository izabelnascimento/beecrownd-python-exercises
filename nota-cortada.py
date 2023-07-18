b = int(input())
t = int(input())

h = 70
felix = (t+b)/2 * h
marzia = (320-t-b)/2 * h

if (felix == marzia):
    print(0)
elif (felix > marzia):
    print(1)
elif (marzia > felix):
    print(2)
