import sys
import pytest


@pytest.mark.parametrize(
    "ip_add,ip_type",
    [
        ("10.1.1.1", "unicast"),
        ("28.1.1.1", "unicast"),
        ("230.1.1.1", "multicast"),
        ("255.255.255.255", "local broadcast"),
        ("0.0.0.0", "unassigned"),
        ("250.1.1.1", "unused"),
    ],
)
def test_task_correct_ip(capsys, monkeypatch, ip_add, ip_type):
    """
    Перевірка роботи завдання при вводе multicast адреса
    """
    monkeypatch.setattr("builtins.input", lambda x=None: ip_add)
    if sys.modules.get("task_6_6a"):
        del sys.modules["task_6_6a"]
    import task_6_6a

    out, err = capsys.readouterr()
    correct_stdout = ip_type
    assert out, (
        "Нічого не виведено стандартний потік виведення. Потрібно не лише "
        "отримати потрібний результат, але й вивести його на стандартний потік "
        "виведення за допомогою print"
    )
    assert (
        correct_stdout == out.strip()
    ), "На стандартний потік виведення виводиться неправильний вивід"


@pytest.mark.parametrize(
    "ip_add,ip_type",
    [
        ("10.1.1", "wrong ip address"),
        ("10.a.2.a", "wrong ip address"),
        ("10.1.1.1.1", "wrong ip address"),
        ("10.1.1.1.a", "wrong ip address"),
        ("10.1.1.", "wrong ip address"),
        ("300.1.1.1", "wrong ip address"),
        ("30,1.1.1.1", "wrong ip address"),
    ],
)
def test_task_wrong_ip(capsys, monkeypatch, ip_add, ip_type):
    """
    Перевірка роботи завдання при вводе multicast адреса
    """
    monkeypatch.setattr("builtins.input", lambda x=None: ip_add)
    if sys.modules.get("task_6_6a"):
        del sys.modules["task_6_6a"]
    import task_6_6a

    out, err = capsys.readouterr()
    correct_stdout = ip_type
    assert out, (
        "Нічого не виведено стандартний потік виведення. Потрібно не лише "
        "отримати потрібний результат, але й вивести його на стандартний потік "
        "виведення за допомогою print"
    )
    assert (
        correct_stdout == out.strip().lower()
    ), "На стандартний потік виведення виводиться неправильний вивід"
