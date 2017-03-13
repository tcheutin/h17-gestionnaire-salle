from django.db import connection

with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM rest_framework_api_key_apikey")
        # cursor.execute("SELECT foo FROM bar WHERE baz = %s")
        row = cursor.fetchone()
        print(row)

        cursor.execute("INSERT INTO rest_framework_api_key_apikey VALUES('1f15f7a4-f5f2-4c9e-a03e-d844c4daad80', '2017-03-12T15:59:23-04:00','2017-03-12T15:59:23-04:00', 'pi', 'a677abfcc88c8126deedd719202e50922')")

