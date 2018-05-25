import time
while True:
    lr = open('l.txt', 'r')
    for x in lr:
        old = int(x)
    l = open('l.txt', 'w')
    new = old + 1204555456542252545562342
    l.write(str(new))
    l.close()
    lr.close()
    time.sleep(.01)