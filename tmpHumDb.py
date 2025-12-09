import psycopg

class TmpHumDb:
    def __init__(self, hostStr, dbPort, dbStr, uNameStr, dbPassStr) -> None:
        self.hostStr = hostStr
        self.dbPort = dbPort
        self.dbStr = dbStr
        self.uNameStr = uNameStr
        self.dbPassStr = dbPassStr

    def insertData(self, tmp, hum, sensorId):
        conn = None
        try:
            # Connect to PostgreSQL
            conn = psycopg.connect(
                host=self.hostStr,
                port=self.dbPort,
                dbname=self.dbStr,
                user=self.uNameStr,
                password=self.dbPassStr
            )

            with conn.cursor() as cur:
                # Single-row insert with ON CONFLICT
                cur.execute(
                    """
                    INSERT INTO public.temp_hum_data (tmp, hum, sid)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (sid, data_time)
                    DO UPDATE SET hum = excluded.hum, tmp = excluded.tmp
                    """,
                    (tmp, hum, sensorId)
                )

            conn.commit()
            print("Data logged successfully!")

        except Exception as error:
            print("Error while interacting with PostgreSQL...\n", error)

        finally:
            if conn:
                conn.close()

