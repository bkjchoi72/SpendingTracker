from src.enumeration.spending import Spending


class SpendingCategoryOutOfRange(Exception):
    pass


class SpendingCategoryValueNotFound(Exception):
    pass


class SpendingCategory(object):
    def __init__(self):
        self.categories = [category for category in Spending]

    def categorize_row_by_description(self, description, date):
        print '\nWhich category does "{} - {}" belong to?'.format(description, date)
        print '(Default value is OTHER)'
        self._print_options()

        user_input = raw_input('Enter (ex. 1): ')

        if not user_input:
            user_input = Spending.OTHER.value

        user_input = int(user_input)
        number_of_categories = len(self.categories)
        if user_input < 1 or user_input > number_of_categories:
            raise SpendingCategoryOutOfRange

        return self._find_category_by_int_value(user_input)

    def _print_options(self):
        print ''
        for i, category in enumerate(self.categories, start=1):
            print '{}) {}'.format(i, category.name)

    def _find_category_by_int_value(self, numeric_int_value):
        for category in self.categories:
            if category.value == int(numeric_int_value):
                return category

        raise SpendingCategoryValueNotFound
