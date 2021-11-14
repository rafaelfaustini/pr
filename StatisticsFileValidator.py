
import datetime
from pandas_schema import Column, Schema
from pandas_schema.validation import CustomElementValidation

class StatisticsFileValidator:

    number_validation = [CustomElementValidation(lambda d: StatisticsFileValidator.check_number(d), 'is not a number')]
    date_validation = [CustomElementValidation(lambda d: StatisticsFileValidator.check_date(d), 'is not a date')]

    schema = Schema([
            Column('date', date_validation),
            Column('inflation', number_validation),
            Column('interest', number_validation),
            Column('growth', number_validation),
            Column('unemployment', number_validation),
            Column('poverty', number_validation),
            ])

    @staticmethod
    def check_number(dec):
        try:
            if type(dec) == int or float:
                return True
            return False
        except Exception:
            return False

    @staticmethod
    def check_date(dec):
        try:
            datetime.datetime.strptime(dec, "%Y-%m-%d %H:%M:%S")
        except Exception:
            return False
        return True

    @staticmethod
    def validate(data):
        errors = StatisticsFileValidator.schema.validate(data)
        for error in errors:
            print(error)
            return False
        return True