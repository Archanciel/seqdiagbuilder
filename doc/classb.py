from doc.classc import ClassC

class ClassB:
    def doB(self, p1):
        c = ClassC()
        a = 0

        c.doC1(p1)
        a += 1 # dummy instruction
        c.doC2(p1)

        print(a) # another dummy instruction