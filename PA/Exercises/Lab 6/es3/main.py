from multitriggered import MultiTriggered

class MT(metaclass=MultiTriggered( \
        {'m2': [2, lambda x,y: x*y], \
         'm3': [3, lambda x,y: x+y]} )):

    def m1(self):
        print("m1 has been called!")
    def m2(self, i):
        print("m2({0}) has been called!".format(i))
    def m3(self, x ,y):
        print("m3({0}, {1}) has been called!".format(x, y))

if __name__ == "__main__":
    mt = MT()
    mt.m1()
    print("### after the 1st call to m1")
    mt.m2(5)
    print("### after the 1st call to m2")
    mt.m3('a', 3)
    print("### after the 1st call to m3")
    mt.m2(7)
    print("### after the 2nd call to m2")
    mt.m3('b', 5)
    print("### after the 2nd call to m3")
    mt.m2(3)
    print("### after the 3rd call to m2")
    mt.m3('c', 7)
    print("### after the 3rd call to m3")
    mt.m3('c', 7)
    print("### after the 3rd call to m3")
