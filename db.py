import pymysql
import config

conn = None
cursor = None


def connection():
    conn = pymysql.connect(
        host=config.MYSQL_HOSTNAME,
        user=config.MYSQL_USERNAME,
        passwd=config.MYSQL_PASSWORD,
        port=config.MYSQL_PORT,
        db=config.MYSQL_DATABASE_NAME
    )
    cursor = conn.cursor()
    return cursor, conn


def create_all_tables():
    try:
        cursor, con = connection()
        # CREATE BUS CHECKINS TABLE
        query = "CREATE TABLE IF NOT EXISTS `bus_checkins` (\
                `id` INT NOT NULL AUTO_INCREMENT,\
                `lpn_id` VARCHAR(100) NULL,\
                `mac_addr` VARCHAR(45) NULL,\
                `rssi` DECIMAL(5,2) NULL,\
                `date_modified` datetime DEFAULT CURRENT_TIMESTAMP,\
                PRIMARY KEY (`id`));"
        cursor.execute(query)

        # CREATE BUS NAMES TABLE
        query = "CREATE TABLE IF NOT EXISTS `bus_names` (\
                `id` INT NOT NULL AUTO_INCREMENT,\
                `bus_name` VARCHAR(100) NULL,\
                `bus_type` VARCHAR(100) NULL,\
                `lpn_id` VARCHAR(100) NULL,\
                `date_modified` datetime DEFAULT CURRENT_TIMESTAMP,\
                PRIMARY KEY (`id`));"
        cursor.execute(query)
        con.commit()
    except Exception as e:
        print("There was an error creating tables")
        print(e)
