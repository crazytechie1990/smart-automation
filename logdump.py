#!/usr/bin/python3
import argparse
import psycopg2 as pg

parser = argparse.ArgumentParser(description=
                                 """
Reads log table. By default displays the last 1 hour log for all categories with all severities.
""")
parser.add_argument('-s', '--start_time', required=False, help="provide time in format of "
                                                               "'yyyy/mm/dd hh:mm:ss' with single quotes")
parser.add_argument('-e', '--end_time', required=False, help="provide time in format of"
                                                             " 'yyyy/mm/dd hh:mm:ss' with single quotes")
parser.add_argument('-st', '--severity', required=True, help="Severity level are INFO,WARNING,FATAL,ERROR")
parser.add_argument('-c', '--category', required=True,
                    help="""
                    Valid categories are QManager,Init,QManager,SYSTEM, tzmclnt'
                    ,'QueryServer,QueryProduct,QueryMedia,QueryConfig,QueryImages',
                    CreateConfig,CreateMedia,ExportImages,ImportImages,HouseKeeping
                    """)
args = parser.parse_args()
sql_insert_query = """ SELECT job_id,insert_time,category,message from log
                       where category=%s and severity=%s and insert_time between %s AND %s;
                       """
insert_tuple_1 = (args.category, args.severity, args.start_time, args.end_time)


def db_connect():
    # connect to the TZM Database
    try:
        conn = pg.connect(
            host="localhost",
            database="tranzman",
            user="postgres",
            password="")
        # create a cursor
        cur = conn.cursor()
        cur.execute(sql_insert_query, insert_tuple_1)
        rows = cur.fetchall()
        print("=" * 135)
        print('{:<10s}{:>20s}{:>29s}{:^50s}'.format("JobID", "Time", "Category", "Message"))
        print("=" * 135)
        for row in rows:
            print("-" * 135)
            print('{:<10s}{:>30s}{:^30s}{:^50s}'.format(str(row[0]), str(row[1]), str(row[2]), str(row[3])))
        cur.close()
        conn.close()
    except (Exception, pg.DatabaseError) as error:
        print(error)


def main():
    db_connect()


if __name__ == '__main__':
    main()
