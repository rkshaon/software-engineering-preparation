class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            # Initialize the instance (e.g., establish the database connection)
            cls._instance.connection = cls._connect_to_database()
        return cls._instance

    @staticmethod
    def _connect_to_database():
        return "Database Connection Established"


# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1.connection)  # Output: Database Connection Established
print(db1 is db2)  # Output: True (both references point to the same instance)
