from service_worker.init_django_orm import init_django_orm  # noqa: F401

import os
import psycopg2
from django.db import transaction

from db.models import Location, Institution, Student, StudentResults

if __name__ == "__main__":
    host = "db"
    user = "postgres"
    db_name_old = "ZNO2020"
    password = "6667"

    old_db_conn = psycopg2.connect(dbname=db_name_old, user=user, password=password, host=host)
    old_db_cursor = old_db_conn.cursor()

    old_db_cursor.execute("SELECT * FROM zno_results;")
    data_info = old_db_cursor.fetchall()

    with transaction.atomic():
        for row in data_info:
            location, loc_created = Location.objects.get_or_create(region_name=row[3], area_name=row[4], territory_name=row[5], territory_type=row[7])
            institution, inst_created = Institution.objects.get_or_create(name=row[8], type=row[9])
            student, stu_created = Student.objects.get_or_create(birth_year=row[1], sex=row[2], type=row[6], location=location, institution=institution)
            result, res_created = StudentResults.objects.get_or_create(student=student, status=row[10], ukrball100=row[11], ukrball12=row[12])

    print("DB2 is Done")

    old_db_cursor.close()
    old_db_conn.close()
