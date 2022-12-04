import sqlite3
import hashlib

def addNewUser(newUsername, newPassword):
    con = sqlite3.connect("userdata.db")
    cur = con.cursor()

    newPassword = hashlib.sha256(newPassword.encode()).hexdigest()

    cur.execute("CREATE TABLE IF NOT EXISTS userdata(id INTEGER PRIMARY KEY, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL)")
    try:
        cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (newUsername, newPassword))
        con.commit()
    except sqlite3.IntegrityError:
        return False
    finally:
        con.close()

def validate(username, password):
    con = sqlite3.connect("userdata.db")
    cur = con.cursor()

    password = hashlib.sha256(password.encode()).hexdigest()
    cur.execute("SELECT COUNT(1) FROM userdata WHERE username = ? AND password = ?", (username, password))
    x = cur.fetchone()
    # print(x[0])
    if x[0] == 1:
        return True
    else:
        return False
    

def main():
    result = addNewUser("soljt","password")
    if not result:
        print("That username is already in the db!")
    print(validate("soljt", "password"))

if __name__=="__main__":
    main()