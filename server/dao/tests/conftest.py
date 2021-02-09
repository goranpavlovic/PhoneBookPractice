import pytest
from server.dao.entry_dao import EntryDao


@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    EntryDao.truncate()