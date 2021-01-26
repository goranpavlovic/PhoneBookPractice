from server.dao.entry_dao import EntryDao


def test_create_entry():
    entry_dao = EntryDao()
    items = entry_dao.list()
    assert len(items) == 1

    entry_dao.create("mika", "mikic")

    items = entry_dao.list()
    assert len(items) == 2



def test_update_entry():
    pass

