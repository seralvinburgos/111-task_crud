from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        result_dict = {
            "id": result[0],
            "title": result[1],
            "subtitle": result[2],
            "body": result[3],
            "active": result[4]
        }
        out.append(result_dict)
    return out


def scan():
    conn = get_db()
    cursor = conn.execute(
            "SELECT * FROM task WHERE active=1",
            ()
    )
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results) 


def select_by_id(pk):
    conn = get_db()
    cursor = conn.execute(
            "SELECT * FROM task WHERE id=?",
            (pk,)
    )
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def insert(raw_data):
    task_data = (
        raw_data.get("title"),
        raw_data.get("subtitle"),
        raw_data.get("body")
    )
    statement = """
        INSERT INTO task (
            title,
            subtitle,
            body
        ) VALUES (
            ?, ?, ?
        )
    """
    conn = get_db()
    conn.execute(statement, task_data)
    conn.commit()
    conn.close()


def update(pk, raw_data):
    task_data = (
        raw_data.get("title"),
        raw_data.get("subtitle"),
        raw_data.get("body"),
        pk
    )
    statement = """
        UPDATE task 
        SET title = ?,
            subtitle = ?,
            body = ?
        WHERE id = ?
    """
    conn = get_db()
    conn.execute(statement, task_data)
    conn.commit()
    conn.close()


def delete(pk):
    conn = get_db()
    conn.execute(
            "DELETE FROM task WHERE id =?", 
            (pk, )
    )
    conn.commit()
    conn.close()