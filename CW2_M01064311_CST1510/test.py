from app_data.db import conn 
from app_data.cyber_incidents import get_all_cyber_incidents

data = get_all_cyber_incidents(conn)

print (data('severtiy'))
'''
Index(['indes', 'incident_id', 'timestamp', 'severity', category', 'status', 'decsription'], dtype='object')'''
