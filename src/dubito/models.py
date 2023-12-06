from pony import orm

db = orm.Database()

class SubitoInsertion:

    id = orm.PrimaryKey(int)
    title = orm.Required(str)
    url = orm.Required(str)
    