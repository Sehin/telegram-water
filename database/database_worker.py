from datetime import datetime, timedelta

import psycopg2


class DatabaseWorker:
    def __init__(self, host, port, database, user, password):
        self._conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        self._cur = self._conn.cursor()
        self._create_base_table()

    def _create_base_table(self):
        """Create base table if not exists"""
        self._cur.execute('CREATE TABLE IF NOT EXISTS water '
                          '(id SERIAL PRIMARY KEY, tlguser VARCHAR(64),time TIMESTAMP,count INTEGER)')
        self._conn.commit()

    def get_today_water(self, user):
        current_time = datetime.now()
        today = datetime(year=current_time.year, month=current_time.month, day=current_time.day)
        today_string = today.strftime('%Y-%m-%d %H:%M:%S')
        tommorow = (today+timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
        self._cur.execute(
            f"SELECT sum(count) "
            f"from water "
            f"WHERE time>='{today}' and "
            f"time<'{tommorow}' and "
            f"tlguser='{user.id}'"
        )
        result = self._cur.fetchone()
        if result:
            return result[0]
        else:
            return 0

    def add_water(self, user, water_count):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self._cur.execute(
            f"INSERT INTO public.water "
            f"(tlguser, time, count) "
            f"VALUES "
            f"('{user.id}', '{current_time}', {water_count});"
        )
        self._conn.commit()