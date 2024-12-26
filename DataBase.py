import mysql.connector
from mysql.connector import Error
#sua thu vien
# Kết nối đến MySQL
def create_connection():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root", 
            password="123456",
            database="event_database",
            port=3306

        )
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def EventDetails():
    conn = create_connection()
    if not conn:
        return [], [], [], [], [], []
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS event_details (
            event_name VARCHAR(255), 
            event_id VARCHAR(255) PRIMARY KEY, 
            event_date DATE, 
            event_time TIME, 
            event_duration VARCHAR(255)
        )
    """)

    cursor.execute('SELECT * FROM event_details')
    event_details = cursor.fetchall()
    conn.close()
    
    if not event_details:
        return [], [], [], [], [], []
    
    event_names, event_ids, event_dates, event_times, event_durations = zip(*event_details)
    
    return list(event_names), list(event_ids), list(event_dates), list(event_times), list(event_durations), event_details

def TicketDetails():
    conn = create_connection()
    if not conn:
        return [], [], [], [], [], [], [], []
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ticket_details (
            customer_name VARCHAR(255), 
            ticket_id VARCHAR(255) PRIMARY KEY, 
            event_name VARCHAR(255), 
            event_id VARCHAR(255), 
            event_date DATE, 
            event_time TIME, 
            duration VARCHAR(255)
        )
    """)

    cursor.execute('SELECT * FROM ticket_details')
    ticket_details = cursor.fetchall()
    conn.close()
    
    if not ticket_details:
        return [], [], [], [], [], [], [], []
    
    customer_names, ticket_ids, event_names, event_ids, event_dates, event_times, event_durations = zip(*ticket_details)
    
    return list(customer_names), list(ticket_ids), list(event_names), list(event_ids), list(event_dates), list(event_times), list(event_durations), ticket_details

def BookTicket(customer_name, ticket_id, event_name):
    try:
        event_names, event_ids, event_dates, event_times, event_durations, _ = EventDetails()
        
        if event_name not in event_names:
            return "Event not found"

        event_index = event_names.index(event_name)
        event_id = event_ids[event_index]
        event_date = event_dates[event_index]
        event_time = event_times[event_index]
        event_duration = event_durations[event_index]
        
        conn = create_connection()
        if not conn:
            return "Connection failed"
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ticket_details (
                customer_name, ticket_id, event_name, event_id, event_date, event_time, duration
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (customer_name, ticket_id, event_name, event_id, event_date, event_time, event_duration))
        conn.commit()
        conn.close()
        return 'Success'
    except Error as e:
        return str(e)

def CreateNewEvent(event_name, event_id, event_date, event_time, event_duration):
    try:
        conn = create_connection()
        if not conn:
            return "Connection failed"
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO event_details (
                event_name, event_id, event_date, event_time, event_duration
            ) VALUES (%s, %s, %s, %s, %s)
        """, (event_name, event_id, event_date, event_time, event_duration))
        conn.commit()
        conn.close()
        return 'Success'
    except Error as e:
        return str(e)

def DeleteTicket(ticket_id):
    try:
        conn = create_connection()
        if not conn:
            return "Connection failed"
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ticket_details WHERE ticket_id = %s", (ticket_id,))
        conn.commit()
        conn.close()
        return 'Success'
    except Error as e:
        return str(e)
