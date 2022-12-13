class IllegalArgumentError(ValueError):
    pass


class CsvConverterError(RuntimeError):
    pass


class WrongFileStructureError(CsvConverterError):
    pass


class WrongCsvStructureError(CsvConverterError):
    pass


class TaskManagerError(RuntimeError):
    pass


class WrongSubtaskError(TaskManagerError):
    pass


class WrongTaskStatusError(TaskManagerError):
    pass
