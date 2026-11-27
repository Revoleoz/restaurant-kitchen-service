# Restaurant Kitchen Service

Навчальний Django-застосунок для керування кухнею ресторану. У ньому можна
додавати й редагувати страви, типи страв і кухарів, шукати записи та
призначати відповідальних за приготування. Кухар також може призначити
себе на сторінці страви або зняти своє призначення.

## Локальний запуск

Потрібен Python 3.12 або новіший. Команди нижче призначені для Git Bash
на Windows. Виконуй їх у корені проєкту, поруч із `manage.py`.

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Відкрий <http://127.0.0.1:8000/kitchen/> та увійди під створеним
обліковим записом.

## Демодані

За бажанням після міграцій завантаж фікстуру з 12 стравами,
5 кухарями та 3 типами страв.

```bash
python manage.py loaddata kitchen_demo.json
```

Для входу використовуй обліковий запис, створений через `createsuperuser`.

## Тести

```bash
python manage.py test
```
