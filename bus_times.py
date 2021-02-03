import simplejson as json
from flask import render_template
import db

cursor = None
conn = None

def read_bus_times():
  cursor, conn = db.connection()
  bus_times = []
  query = "SELECT c.id, c.lpn_id, c.mac_addr, c.rssi, c.date_modified, n.bus_name, n.bus_type FROM bus_checkins c LEFT OUTER JOIN bus_names n ON c.lpn_id=n.lpn_id;"
  cursor = conn.cursor()
  cursor.execute(query)
  loc = cursor.fetchall()
  if cursor.rowcount > 0:
    bus_log_row_headers = [x[0] for x in cursor.description]
    for i, cur_record in enumerate(loc):
      bus_times.append(dict(zip(bus_log_row_headers, cur_record)))
  return bus_times

def delete_bus_entry(entry_id):
  try:
    cursor, conn = db.connection()
    query = "DELETE FROM bus_checkins WHERE id = {0}".format(entry_id)
    cursor.execute(query)
    row_id = cursor.lastrowid
    conn.commit()
    return {"ok": True, "last_inserted_id": row_id}
  except Exception as e:
    return {"ok": False, "error": str(e)}