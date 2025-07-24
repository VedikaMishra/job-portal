import sqlite3

conn = sqlite3.connect("job_portol.db")
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE IF NOT EXISTS companies (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    industry TEXT,
    location TEXT
);

CREATE TABLE IF NOT EXISTS jobs (
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    job_role TEXT,
    company_id INTEGER,
    location TEXT,
    salary INTEGER,
    experience_required INTEGER,
    posted_date TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);
""")

# Optional sample data
cursor.execute("INSERT INTO companies (name, industry, location) VALUES ('Infosys', 'IT Services', 'Pune')")

cursor.execute("""INSERT INTO jobs (title, job_role, company_id, location, salary, experience_required, posted_date) 
                  VALUES ('Python Developer', 'Python Developer', 1, 'Pune', 600000, 1, '2025-07-01')""")

conn.commit()
conn.close()
print("✅ Tables created in job_portol.db")
import sqlite3

conn = sqlite3.connect("job_portol.db")
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE IF NOT EXISTS companies (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    industry TEXT,
    location TEXT
);

CREATE TABLE IF NOT EXISTS jobs (
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    job_role TEXT,
    company_id INTEGER,
    location TEXT,
    salary INTEGER,
    experience_required INTEGER,
    posted_date TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);
""")

# Optional sample data
cursor.execute("INSERT INTO companies (name, industry, location) VALUES ('Infosys', 'IT Services', 'Pune')")

cursor.execute("""INSERT INTO jobs (title, job_role, company_id, location, salary, experience_required, posted_date) 
                  VALUES ('Python Developer', 'Python Developer', 1, 'Pune', 600000, 1, '2025-07-01')""")

conn.commit()
conn.close()
print("✅ Tables created in job_portol.db")
