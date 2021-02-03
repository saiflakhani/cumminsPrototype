import simplejson as json
from flask import render_template
import db

cursor = None
conn = None

def add_bus_name(lpn_id, bus_name, bus_type):
    try:
        cursor, conn = db.connection()
        query = "INSERT INTO bus_names(lpn_id, bus_name, bus_type) VALUES ('{0}', '{1}', '{2}');".format(lpn_id, bus_name, bus_type)
        cursor.execute(query)
        row_id = cursor.lastrowid
        conn.commit()
        return {"ok": True, "last_inserted_id": row_id}
    except Exception as e:
        return {"ok": False, "error": str(e)}


