from ..Utils.UtilsDatetime import UtilsDatetime


class Report:
    @staticmethod
    def hello():
        year = UtilsDatetime.getYear("2022-11-11")
        return year;
