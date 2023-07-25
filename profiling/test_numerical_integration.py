import pytest

from numerical_integration import integrate_f


def test_integrate_f():
    f = lambda x: x ** 4 - 3 * x
    F = lambda x: 1 / 5 * x ** 5 - 3 / 2 * x ** 2
    n = 10_000
    a = -2
    b = 2

    F_analytical = F(b) - F(a)
    F_numerical = integrate_f(f, a, b, n)

    assert F_analytical == pytest.approx(F_numerical)
