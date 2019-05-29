from testclasses.classloopnestedinnertwocallstwoloopstarttagsonsameline import ClassLoopNestedInnerTwoCallsTwoLoopStartTagsOnSameLine

class ClassLoopNestedInnerTwoTwoCallsTwoLoopStartTagsOnSameLineCaller:
    '''
    ClassLoopNestedInnerTwoTwoCallsTwoLoopStartTagsOnSameLineCaller is the entry point of our sequence diagram.
    '''

    def call(self, p1):
        '''
        call() is the entry method of our sequence diagram.
        '''
        b = ClassLoopNestedInnerTwoCallsTwoLoopStartTagsOnSameLine()
        b.doB(p1)
