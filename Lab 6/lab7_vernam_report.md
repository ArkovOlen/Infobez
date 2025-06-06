
# Лабораторная работа №7: Элементы криптографии. Однократное гаммирование

## 1. Титульный лист


**Отчёт по лабораторной работе №7**  
по дисциплине: _Информационная безопасность_  
**Тема**: Элементы криптографии. Однократное гаммирование  

**Студент**: Олейников Артём Игоревич  
**Группа**: НБИбд-01-23
**Дата выполнения**: 16.05.2025

---

## 2. Цель работы

Освоить на практике применение режима однократного гаммирования (шифра Вернама).

---

## 3. Ход выполнения

### 3.1. Генерация ключа

**Описание**: Генерация ключа, длина которого равна длине сообщения.

**Команда**:

```bash
python vernam_lab7.py
```

**Результат**:

Ключ (в HEX):  
`5F3A47A9D1B29338EE83F516589BDDAA6DC65181A6F1885BA60DA2`

---

### 3.2. Шифрование сообщения

**Открытый текст**:  
`С Новым Годом, друзья!`

**Описание**: Выполнено побитовое XOR-смешивание ключа и текста.

**Результат (зашифрованный текст в HEX)**:  
`303F26C291D4E24B8796A6F53EDAD8C04AAB317CC4D9A2EED52B8B`

---

### 3.3. Расшифровка

**Описание**: Выполнена обратная операция XOR (дешифрование).

**Результат**:  
`С Новым Годом, друзья!` — совпадает с исходным текстом.

---

### 3.4. Восстановление ключа

**Описание**: Ключ был восстановлен по формуле:

```
K = C ⊕ P
```

**Результат**: Восстановленный ключ совпадает с изначальным.

---

## 4. Выводы

В результате лабораторной работы:

- Был реализован алгоритм шифрования на основе однократного гаммирования (XOR);
- Подтверждена корректность шифрования и расшифровки;
- Проверена возможность восстановления ключа при известном открытом тексте и шифротексте;
- Сделан вывод о криптостойкости при соблюдении условий: ключ равной длины, полная случайность и однократность использования.
