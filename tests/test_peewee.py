import pytest

from ..src.models.biblio_models import *

def test_database_name():
    assert database.database == "biblioteca.db"

def test_get_first_user():
    assert Usuario.get().nome == 'ANA'

def test_select_users():
    assert [row.nome for row in Usuario.select().where(Usuario.id <= 2)] == ['ANA', 'FELIPE']