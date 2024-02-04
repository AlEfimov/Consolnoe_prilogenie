from main import check_password
from main import apply_transaction
from main import add_balance
from main import take_money
from main import add_transaction
from main import check_balance


def test_check_balance(monkeypatch):
    with open("user_data.txt") as fin:
        password = fin.readline()
        password = fin.readline()
        password = fin.readline()
    inputs = iter([password])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert check_balance(1000, password) == None


def test_apply_transaction():
    assert apply_transaction(0, 1000, ["100", "qaz", "1000", "qwe", "900", "zxc", "200", "qwe"]) == (
        1000, [1000, "qwe", 200, "qwe"])


def test_add_balance(monkeypatch):
    inputs = iter(['1000'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert add_balance(1000) == 2000


def test_take_money_then_ok(monkeypatch):
    with open("user_data.txt") as fin:
        password = fin.readline()
        password = fin.readline()
        password = fin.readline()
    inputs = iter([password, '1000'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert take_money(1000, password) == 0


def test_take_money_then_no_ok(monkeypatch):
    with open("user_data.txt") as fin:
        password = fin.readline()
        password = fin.readline()
        password = fin.readline()
    inputs = iter([password, '1100'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert take_money(1000, password) == 1000


def test_check_password_then_true(monkeypatch):
    inputs = iter(['123'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert check_password('123') == True


def test_check_password_then_folse(monkeypatch):
    inputs = iter(['234'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert check_password('123') == False


def test_add_transaction(monkeypatch):
    inputs = iter(['1000', 'qwe'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert add_transaction(['1000', 'asd', '2000', 'zxc']) == ['1000', 'asd', '2000', 'zxc', '1000', 'qwe']
