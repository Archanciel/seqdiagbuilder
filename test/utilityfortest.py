import os,sys,inspect
import re

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from test.datetimeutil import DateTimeUtil

class UtilityForTest:
    '''
    This class contains static utility methods used by some unit test classes. It avoids code duplication.
    '''
    @staticmethod
    def getFormattedDateTimeComponentsForArrowDateTimeObj(dateTimeObj):
        '''
        Return dateTimeObjYearStr, dateTimeObjMonthStr, dateTimeObjDayStr, dateTimeObjHourStr,
        dateTimeObjMinuteStr corresponding to the passed Arrow date object
        :param dateTimeObj: passed Arrow date object
        :return:
        '''
        dateTimeObjDayStr = dateTimeObj.format('DD')
        dateTimeObjMonthStr = dateTimeObj.format('MM')
        dateTimeObjYearStr = dateTimeObj.format('YY')
        dateTimeObjHourStr = dateTimeObj.format('HH')
        dateTimeObjMinuteStr = dateTimeObj.format('mm')

        return dateTimeObjYearStr, dateTimeObjMonthStr, dateTimeObjDayStr, dateTimeObjHourStr, dateTimeObjMinuteStr


    @staticmethod
    def removePriceFromResult(resultStr):
        '''
        Used to remove unique price from RT request results or variable date/time price request results
        :param resultStr:
        :return:
        '''
        patternNoWarning = r"(.*) ([\d\.]*)"
        patternOneWarning = r"(.*) ([\d\.]*)(\n.*)" #in raw string, \ must not be escaped (\\n not working !)
        match = re.match(patternOneWarning, resultStr)

        if (match):
            if len(match.groups()) == 3:
                # here, resultStr contains a warning like in
                # BTC/USD on CCCAGG: 30/01/18 01:51R 11248.28\nWarning - unsupported command -ebitfinex in request btc usd 0 all -ebitfinex !
                return match.group(1) + match.group(3)

        match = re.match(patternNoWarning, resultStr)

        if (match):
            if len(match.groups()) == 2:
                # the case for resultStr containing BTC/USD on CCCAGG: 30/01/18 01:49R 11243.72 for example !
                return match.group(1)

        return ()

    @staticmethod
    def removeAllPricesFromCommandValueResult(resultStr):
        '''
        Used to remove multiple prices from RT request results or variable date/time price request results
        :param resultStr:
        :return:
        '''
        patternNoWarning = r"(?:[\d\.]*) (\w*/)(?:[\d\.]*) (.*) (?:[\d\.]*)"
        patternOneWarning = r"(?:[\d\.]*) (\w*/)(?:[\d\.]*) (.*) (?:[\d\.]*(\n.*))"
        match = re.match(patternOneWarning, resultStr)

        if match != None:
            if len(match.groups()) == 3:
                return match.group(1) + match.group(2) + match.group(3)

        match = re.match(patternNoWarning, resultStr)

        if len(match.groups()) == 2:
            return match.group(1) + match.group(2)
        else:
            return ()


if __name__ == '__main__':
    now = DateTimeUtil.localNow('Europe/Zurich')
    nowMonthStr, nowDayStr, nowHourStr, nowMinuteStr = UtilityForTest.getFormattedDateTimeComponentsForArrowDateTimeObj(now)
    print("{}/{} {}:{}".format(nowDayStr, nowMonthStr, nowHourStr, nowMinuteStr))