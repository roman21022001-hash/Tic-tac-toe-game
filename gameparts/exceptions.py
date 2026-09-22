class FieldIndexError(IndexError):

    def __str__(self):
        return 'A value outside the boundaries of the playing field has been entered'


class CellOccupiedError(Exception):

    def __str__(self):
        return 'Попытка изменить занятую ячейку'
