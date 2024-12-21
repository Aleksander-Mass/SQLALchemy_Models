from sqlalchemy.schema import CreateTable
from app.backend.db import Base, engine
from app.models import User, Task

# Распечатываем SQL запросы для создания таблиц
def print_sql_for_tables():
    for table in Base.metadata.tables.values():
        print(CreateTable(table).compile(engine))
        print()

if __name__ == "__main__":
    print_sql_for_tables()

###  ПРИМЕЧАНИЕ:
# Для получения результатов согласно задания, необходимо запустать команду:
# python init_db.py
# в терминале