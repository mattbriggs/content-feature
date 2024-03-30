import sqlite3
import logging

# Database schema setup
CREATE_TABLES_SQL = """
CREATE TABLE IF NOT EXISTS markdown_files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path TEXT NOT NULL UNIQUE,
    summary TEXT
);

CREATE TABLE IF NOT EXISTS entities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_name TEXT NOT NULL,
    file_id INTEGER NOT NULL,
    FOREIGN KEY (file_id) REFERENCES markdown_files (id)
);
"""

def create_connection(db_file):
    """Create a database connection to a SQLite database specified by db_file"""
    try:
        conn = sqlite3.connect(db_file)
        logging.info(f"Connected to database {db_file}")
        return conn
    except sqlite3.Error as e:
        logging.error(f"Error connecting to database: {e}")
    return None

def create_tables(conn):
    """Create tables in the database based on the schema defined"""
    try:
        c = conn.cursor()
        c.executescript(CREATE_TABLES_SQL)
        conn.commit()
        logging.info("Tables created successfully")
    except sqlite3.Error as e:
        logging.error(f"Error creating tables: {e}")

def insert_markdown_file(conn, file_path, summary):
    """Insert a markdown file and its summary into the database"""
    sql = ''' INSERT INTO markdown_files(file_path, summary)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (file_path, summary))
    return cur.lastrowid

def insert_entity(conn, entity_name, file_id):
    """Insert an entity related to a markdown file into the database"""
    sql = ''' INSERT INTO entities(entity_name, file_id)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (entity_name, file_id))
    return cur.lastrowid

def setup_database(db_file):
    """Set up the database: create connection, create tables."""
    conn = create_connection(db_file)
    if conn is not None:
        create_tables(conn)
    else:
        logging.error("Error! cannot create the database connection.")
    return conn

def save_data_to_database(db_file, markdown_files_data):
    """Save processed data to database."""
    conn = setup_database(db_file)
    if conn is not None:
        try:
            for file_path, data in markdown_files_data.items():
                file_id = insert_markdown_file(conn, file_path, data['summary'])
                for entity in data['entities']:
                    insert_entity(conn, entity, file_id)
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error saving data to database: {e}")
        finally:
            conn.close()
