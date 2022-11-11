from datetime import datetime
import pandas as pd

class UtilsDatetime():

    @staticmethod
    def difDTReturnDatetimeYYYYMMDDxDay(dateIni, dateEnd):
        """
        Resta dos fechas
        obtiene las fechas de cada día en un rango de fechas indicado como parámetro
        :param dateIni: formato 2021-12-30
        :param dateEnd: formato 2022-01-02
        :return: retorna las fechas por día en un array
        ['2021-12-30', '2021-12-31', '2022-01-01', '2022-01-02']
        """
        start = datetime.strptime(dateIni, "%Y-%m-%d")
        end = datetime.strptime(dateEnd, "%Y-%m-%d")
        date_generated = pd.date_range(start, end)
        # print(date_generated.strftime("%d-%m-%Y"))
        diasList = []
        for i in date_generated:
            diasList.append(i.strftime("%Y-%m-%d"))
        return diasList;

    @staticmethod
    def difDTReturnYears(dateIni, dateEnd):
        """
        Resta dos fechas
        obtiene las fechas de cada día en un rango de fechas indicado como parámetro
        :param dateIni: formato 2021-12-30
        :param dateEnd: formato 2022-01-02
        :return: retorna sólo los años en un array
        [2021, 2022]
        Notice: years no repeat

        """
        start = datetime.strptime(dateIni, "%Y-%m-%d")
        end = datetime.strptime(dateEnd, "%Y-%m-%d")
        date_generated = pd.date_range(start, end)

        anios = date_generated.year;

        # remove duplicates:
        anios = [*set(anios)]

        return anios

    @staticmethod
    def getRangeTupleDTXYearList(dateIni, dateEnd):
        """
        Obtiene rango de fechas por año.
        :param dateIni: formato 2021-12-30
        :param dateEnd: formato 2022-01-02
        :return: retorna las fechas por año en un array
        [('2021-12-30', '2021-12-31'), ('2022-01-01', '2022-01-02')]
        """
        start = datetime.strptime(dateIni, "%Y-%m-%d")
        end = datetime.strptime(dateEnd, "%Y-%m-%d")
        date_generated = pd.date_range(start, end)

        anhos = date_generated.year;

        # remove duplicates:
        anhos = [*set(anhos)]

        # almacenamos las fechas
        _dateTimeList = [];
        for anho in anhos:
            # validate datetime range
            if str(anho) in dateIni:
                _dateIni = dateIni;
                if str(anho) in dateEnd:
                    _dateEnd = dateEnd;
                else:
                    _dateEnd = str(anho) + '-12-31';
            else:
                _dateIni = str(anho) + '-01-01'
                if str(anho) in dateEnd:
                    _dateEnd = dateEnd;
                else:
                    _dateEnd = str(anho) + '-12-31';
            _dateTimeList.append((_dateIni, _dateEnd))
        return _dateTimeList;

    @staticmethod
    def getYear(dtStr:str):
        """
        Get year of date
        Obtiene el año de una fecha determinada
        :param dtStr:
        :return: retorna el año en string
        """
        dtObject = datetime.strptime(dtStr, "%Y-%m-%d")
        return str(dtObject.year);


if __name__=="__main__":

    print("Listado de fechas por día")
    diasList = UtilsDatetime.difDTReturnDatetimeYYYYMMDDxDay("2021-12-30", "2022-01-02")
    print(diasList)

    print("Listado de años")
    yearsList = UtilsDatetime.difDTReturnYears("2021-12-30", "2022-01-02")
    print(yearsList)

    print("Listado rango de fechas por año")
    rangeDTTupleXYearList = UtilsDatetime.getRangeTupleDTXYearList("2021-12-30", "2022-01-02")
    print(rangeDTTupleXYearList)

    for dateIni,dateEnd in rangeDTTupleXYearList:
        print(dateIni,dateEnd)

    year=UtilsDatetime.getYear("2017-01-01")
    print(year)
    print(type(year))


