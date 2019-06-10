from testclasses.classlooptagonmethodnotinrecordflow import ClassLoopTagOnMethodNotInRecordFlow

class ClassLoopTagOnMethodNotInRecordFlowCaller:
    '''
    ClassLoopTagOnMethodNotInRecordFlowCaller is the entry point of our
    sequence diagram.
    '''

    def callLoopStartAndLoopEndOnNotRecordedMethodCall(self, p1):
        '''
        Entry method of our sequence diagram.
        '''
        b = ClassLoopTagOnMethodNotInRecordFlow()
        b.doLoopStartAndLoopEndOnNotRecordedMethodCall(p1)

    def callLoopStartEndOnNotRecordedMethodCall(self, p1):
        '''
        Entry method of our sequence diagram.
        '''
        b = ClassLoopTagOnMethodNotInRecordFlow()
        b.doLoopStartEndOnNotRecordedMethodCall(p1)

    def callLoopStartOnRecordedMethodCallAndLoopEndOnNotRecordedMethodCall(self, p1):
        '''
        Entry method of our sequence diagram.
        '''
        b = ClassLoopTagOnMethodNotInRecordFlow()
        b.doLoopStartOnRecordedMethodCallAndLoopEndOnNotRecordedMethodCall(p1)

    def callLoopStartOnNotRecordedMethodCallAndLoopEndOnRecordedMethodCall(self, p1):
        '''
        Entry method of our sequence diagram.
        '''
        b = ClassLoopTagOnMethodNotInRecordFlow()
        b.doLoopStartOnNotRecordedMethodCallAndLoopEndOnRecordedMethodCall(p1)
