import pytest

from decorators import log


def test_log_success(capsys):
    @log()
    def add(x, y):
        return x + y

    result = add(2, 3)
    assert result == 5

    captured = capsys.readouterr()
    assert "5" in captured.out

def test_log_exception(capsys):
    @log()
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    assert "Function: divide, raised <class 'ZeroDivisionError'>. division by zero\n"

def test_log_to_file(tmp_path):
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def multiply(x, y):
        return x * y

    result = multiply(4, 5)
    assert result == 20

    with open(log_file, "r") as file:
        assert "Function: multiply, Result: 20" in file.read()