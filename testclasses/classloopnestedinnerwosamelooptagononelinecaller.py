from testclasses.classloopnestedinnertwosamelooptagononeline import ClassLoopNestedInnerTwoSameLoopTagOnOneLine

class ClassLoopNestedInnerTwoSameLoopTagOnOneLineCaller:
    '''
    ClassLoopNestedCaller is the entry point of our sequence diagram.
    '''

    def call(self, p1):
        '''
        call() is the entry method of our sequence diagram.
        '''
        b = ClassLoopNestedInnerTwoSameLoopTagOnOneLine()
        b.doB(p1)
