from __future__ import annotations
import pytest
from string_utils import StringUtils
# Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
# Пример: `capitilize("skypro") -> "Skypro"`

@pytest.mark.positive_test_capitilize
@pytest.mark.parametrize('num, result', [('привет', 'Привет'), ('hello', 'Hello'), ('как дела', 'Как дела'),('111', '111')])
def test_capitilize_positive(num, result):
    utils = StringUtils()
    res = utils.capitalize(num)
    assert res == result

@pytest.mark.xfail
@pytest.mark.negative_test_capitilize
@pytest.mark.parametrize('line, result', [("", ""), (" ", " "), (None, None),(333, 333)])
def test_negative_capitilize(line, result):
    utils = StringUtils()
    res = utils.capitalize(line)
    assert res == result

# Принимает на вход текст и удаляет пробелы в начале, если они есть
# Пример: `trim("   skypro") -> "skypro"

@pytest.mark.positive_test_trim
def test_trim_positive():
    utils = StringUtils()
    res = utils.trim(" skypro")  
    assert res == "skypro"
    
@pytest.mark.negative_test_trim
def test_trim_negative():
    utils = StringUtils()
    res = utils.trim("skypro  ")  
    assert res == "skypro  "

# Принимает на вход текст с разделителем и возвращает список строк. \n
# Параметры: \n 
#     string` - строка для обработки \n
#     delimeter` - разделитель строк. По умолчанию запятая (",") \n
#     Пример: `to_list("1:2:3", ":") -> ["1", "2", "3"]`

@pytest.mark.positive_test_to_list
def test_to_list_positive():
    utils = StringUtils()
    res = utils.to_list("1:2:3", ":")  #разделитель строк. По умолчанию запятая (",")
    assert res == ["1", "2", "3"]
   
# Возвращает `True`, если строка содержит искомый символ и `False` - если нет \n 
# Пример 1: `contains("SkyPro", "S") -> True`
# Пример 2: `contains("SkyPro", "U") -> False`

@pytest.mark.positive_test_contains
def test_contains_positive():
    res = True
    utils = StringUtils()
    if  not utils.contains("Арфа", "ф"):
        res = False
    if utils.contains("Арфа", "к"):
        res = False
    assert res is True

# Удаляет все подстроки из переданной строки 
# Пример 1: `delete_symbol("SkyPro", "k") -> "SyPro"`
# Пример 2: `delete_symbol("SkyPro", "Pro") -> "Sky"`

@pytest.mark.positive_test_del_symbol
def test_del_symbol_positive():
    utils = StringUtils()
    res = utils.delete_symbol("AskoPRO", "PRO")
    assert res == "Asko"

@pytest.mark.negative_test_del_symbol
def test_del_symbol_negative():
    utils = StringUtils()
    res = utils.delete_symbol("AskoPRO", "pro")
    assert res == "AskoPRO"

# Возвращает `True`, если строка начинается с заданного символа и `False` - если нет \n 
# Пример 1: `starts_with("SkyPro", "S") -> True`
# Пример 2: `starts_with("SkyPro", "P") -> False`

@pytest.mark.positive_test_starts_with
def test_starts_with_positive():
    res = True
    utils = StringUtils()
    if not utils.starts_with("Москва", "М"):
        res = False
    if utils.starts_with("Volkov", "P"):
        res = False
    assert res is True

# Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет \n 
# Пример 1: `end_with("SkyPro", "o") -> True`
# Пример 2: `end_with("SkyPro", "y") -> False`

@pytest.mark.positive_test_end_with
def test_end_with_positive():
    res = True
    utils = StringUtils()
    if not utils.end_with("Москва", "а"):
        res = False
    if utils.end_with("Volkov", "P"):
        res = False
    assert res is True

# Возвращает `True`, если строка пустая и `False` - если нет \n 
# Пример 1: `is_empty("") -> True`
# Пример 2: `is_empty(" ") -> True`
# Пример 3: `is_empty("SkyPro") -> False`

@pytest.mark.positive_test_is_empty
def test_empty():
    res = True
    utils = StringUtils()
    if not utils.is_empty(""):
        res = False
    if not utils.is_empty(" "):
        res = False
    if utils.is_empty("123"):
        res = False

    assert res is True

# Преобразует список элементов в строку с указанным разделителем \n 
# Параметры: \n 
        # Пример 1: `list_to_string([1,2,3,4]) -> "1, 2, 3, 4"`

def test_list_to_string():
    utils = StringUtils()
    res = utils.list_to_string(["Sky", "Pro"], "-")  
    assert res == "Sky-Pro"