# Python Tests with Certificate 🎓

Проект содержит 20 comprehensive Python тестов с автоматической генерацией сертификата по завершении.

## 📋 Описание

Проект включает:
- **20 Python тестов** (unit tests) для различных операций
- **Автоматическая генерация сертификатов** после успешного прохождения всех тестов
- **3 формата сертификатов**: HTML, JSON и текстовый

## 🧪 Тесты (20 штук)

### Math Operations (7 тестов)
1. Test 1: Basic addition
2. Test 2: Basic subtraction
3. Test 3: Basic multiplication
4. Test 4: Basic division
5. Test 5: Power operation
6. Test 6: Square root
7. Test 7: Modulo operation

### String Operations (5 тестов)
8. Test 8: String concatenation
9. Test 9: String length
10. Test 10: String uppercase
11. Test 11: String lowercase
12. Test 12: String replacement

### List Operations (4 теста)
13. Test 13: List creation and access
14. Test 14: List append operation
15. Test 15: List sum
16. Test 16: List sorting

### Dictionary Operations (4 теста)
17. Test 17: Dictionary creation and access
18. Test 18: Dictionary keys
19. Test 19: Dictionary values
20. Test 20: Dictionary get method

## 🚀 Установка и запуск

### 1. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 2. Запуск всех тестов
```bash
pytest
```

### 3. Запуск с подробным выводом
```bash
pytest -v
```

### 4. Запуск с покрытием кода
```bash
pytest --cov=.
```

## 🎖️ Генерация сертификатов

После успешного прохождения **всех 20 тестов** автоматически генерируются 3 файла:

- **certificate.html** - красивый HTML сертификат (откройте в браузере)
- **certificate.json** - данные сертификата в JSON формате
- **certificate.txt** - текстовый формат сертификата

## 📊 Структура проекта

```
test-sasha/
├── test_math_operations.py    # 20 тестов для различных операций
├── certificate_generator.py   # Генератор сертификатов
├── conftest.py               # Конфигурация pytest
├── pytest.ini                # Настройки pytest
├── requirements.txt          # Зависимости
├── README.md                 # Этот файл
└── certificates/             # Сгенерированные сертификаты
    ├── certificate.html
    ├── certificate.json
    └── certificate.txt
```

## 💻 Примеры использования

### Запуск конкретного теста
```bash
pytest test_math_operations.py::TestMathOperations::test_addition -v
```

### Запуск конкретного класса тестов
```bash
pytest test_math_operations.py::TestStringOperations -v
```

### Запуск с маркерами
```bash
pytest -m "not integration"
```

## 🏆 Что получится

После запуска команды `pytest` вы увидите:

```
======================== test session starts ========================
test_math_operations.py::TestMathOperations::test_addition PASSED
test_math_operations.py::TestMathOperations::test_subtraction PASSED
... (все 20 тестов) ...

======================== 20 passed in 0.05s ========================

================================================================================
🎉 ALL TESTS PASSED! Generating completion certificate...
================================================================================
✓ HTML certificate generated: certificate.html
✓ JSON certificate generated: certificate.json
✓ Text certificate generated: certificate.txt
```

## 📝 Требования

- Python 3.7+
- pytest >= 7.0
- pytest-cov >= 4.0

## 👤 Автор

Sasha Trubarova

## 📄 Лицензия

MIT License
