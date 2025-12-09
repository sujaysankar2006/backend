import asyncio
import hashlib
import sqlite3
connection=sqlite3.connect('history.db')
establish=connection.cursor()
establish.execute('''CREATE TABLE IF NOT EXISTS DATA (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  input_text TEXT,
                  hashvalue TEXT )''')
async def store_to_db():
    await asyncio.sleep(2)
    for inputs in range(5):
        input_data=input(f"enter data {inputs+1}: ")
        hash_obj=hashlib.sha256(input_data.encode()).hexdigest()
        establish.execute('INSERT INTO DATA (input_text,hashvalue) VALUES (?,?)', (input_data, hash_obj))
        connection.commit()
    return f"data was stored successfully"
async def main():
    result=await store_to_db()
    print(result)
asyncio.run(main())        