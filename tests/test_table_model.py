import pytest

from ..src.ui.table_model import *
from ..src.models.biblio_models import Usuario

def test_table_model():
    users = Usuario.select().dicts()
    tm = TableModel(users)
    assert tm.data(tm.index(0,0)) == 1
