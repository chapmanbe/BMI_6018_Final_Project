"""import sqlite3 to use with the sqlite database"""
import sqlite3

class Database:
    """database object that stores the user's balance for the date"""

    def __init__(self):
        self.connection = sqlite3.connect("calorie.db")
        self.cursor = self.connection.cursor()

    def updatedb(self, bal):
        """insetrs data into the table"""
        self.cursor.execute("INSERT INTO calorie (balance) VALUES (?)", (bal,))
        self.connection.commit()
        return

    def get_info(self):
        """gets the information from the database"""
        self.cursor.execute("SELECT * FROM calorie;")
        return self.cursor.fetchall()

    def close_db(self):
        """closes the database"""
        self.connection.close()
        return
