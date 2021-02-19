from datetime import datetime
import pymysql

def get_user_name_from_db(user_id):
    # Establishing a connection to DB
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='jC9okm9Ppe', passwd='LBIGnhlfpI', db='jC9okm9Ppe')
    # Getting a cursor from Database
    cursor = conn.cursor()
    cursor.execute("select user_name from jC9okm9Ppe.users where user_id = %s ;", user_id)
    row = cursor.fetchone()
    user_name = row[0]
    print("the name as listed in the DB is: ", user_name)
    cursor.close()
    conn.close()


def add_user_name_to_db(user_id, user_name):
    is_success = True
    try:
        now = datetime.now()
        # Establishing a connection to DB
        conn = pymysql.connect(host='remotemysql.com', port=3306, user='jC9okm9Ppe', passwd='LBIGnhlfpI',db='jC9okm9Ppe')
        conn.autocommit(True)
    # Getting a cursor from Database
        cursor = conn.cursor()
        sql = "INSERT into jC9okm9Ppe.users (user_id, user_name, creation_date) VALUES (%s, '%s', '%s')" % (user_id, user_name, now)
        cursor.execute(sql)
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error adding user to DB")
        is_success = False
    finally:
        return is_success


def update_user_name_in_db(user_id, user_name):
    is_success = True
    try:

        # Establishing a connection to DB
        conn = pymysql.connect(host='remotemysql.com', port=3306, user='jC9okm9Ppe', passwd='LBIGnhlfpI', db='jC9okm9Ppe')
        conn.autocommit(True)
        # Getting a cursor from Database
        cursor = conn.cursor()
        sql = "Update jC9okm9Ppe.users set user_name = '%s' where user_id = %s;" % (user_name, user_id)
        # sql = "%d" % (user_id)
        # print(user_id, user_name)
        cursor.execute(sql)
        is_success = cursor.rowcount > 0
        # print(cursor.rowcount)
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error updating user in DB")
        is_success = False
    finally:
        return is_success


def delete_user_name_from_db(user_id):
    # is_success = True
    try:
        # Establishing a connection to DB
        conn = pymysql.connect(host='remotemysql.com', port=3306, user='jC9okm9Ppe', passwd='LBIGnhlfpI', db='jC9okm9Ppe')
        conn.autocommit(True)
        # Getting a cursor from Database
        cursor = conn.cursor()
        sql = "DELETE from jC9okm9Ppe.users where user_id = %s;" % user_id
        #print(sql)
        cursor.execute(sql)
        is_success = cursor.rowcount > 0
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error deleting user from DB")
        is_success = False
    finally:
        return is_success


def get_all_user_id_from_db():
    # Establishing a connection to DB
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='jC9okm9Ppe', passwd='LBIGnhlfpI', db='jC9okm9Ppe')
    # Getting a cursor from Database
    cursor = conn.cursor()
    cursor.execute("select user_id from jC9okm9Ppe.users")
    row = cursor.fetchall()
    print("these are all the existing id's in the DB: ", row)
    cursor.close()
    conn.close()
