import sqlite3

from .sql_helper import sql_helper


def sql_sqlite(db_path, req, *params):
    def connect():
        return sqlite3.connect(
            db_path,
            detect_types=sqlite3.PARSE_DECLTYPES
        )

    def exception_handling(e):
        raise sqlite3.ProgrammingError(
            str(e) +
            '\nreq = “{}”\nparams = “{}”'.format(req, params))

    exception = (
        sqlite3.ProgrammingError, sqlite3.InterfaceError,
        sqlite3.IntegrityError, )
    return sql_helper(
        connect, exception, exception_handling, req, *params)
