# -----------------------------------------
# Script by Andriy.K.
#
#
# Version       Date       Info
# 1.0           2023       Initial Version
#
# -----------------------------------------

import os
from models.database import DATABASE_NAME, Session, Metadata
import creat_db as db_creator



if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
    #
    # db = Metadata
    # table_names = db.tables.keys()
    #
    # # Виведення імен всіх таблиць
    # print(list(table_names))