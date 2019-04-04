
def sql_helper(connect, exception, exception_handling, req, *params):
    """
        used to implement the connection to differente database

        if params is a list or map, it's an executemany
        if the request is an insert, it return the key id

        connection must have .execute, .executemany,
            .lastrowid and .fetchall
    """
    many = False
    if len(params) == 1:
        if isinstance(params[0], (list, map)):
            many = True
            params = params[0]

    is_insert = req.split()[0].lower() == 'insert'

    with connect() as con:
        try:
            if many:
                return con.executemany(req, params).fetchall()
            else:
                c = con.execute(req, params)
        except exception as e:
            exception_handling(e)

        if is_insert:
            return c.lastrowid
        return c.fetchall()
