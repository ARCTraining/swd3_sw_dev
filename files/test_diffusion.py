import math

import pytest

from diffusion import heat, step


def linspace(start, stop, num):
    return [start + x * (stop - start) / (num - 1) for x in range(num)]


@pytest.mark.parametrize("L,tmax", [(1, 0.5), (2, 0.5), (1, 1)])
def test_heat(L, tmax):
    nt = 10
    nx = 20
    alpha = 0.01

    xs = linspace(0, L, nx)

    numerical_solution = heat(
        [0] + [math.sin(math.pi * x / L) for x in xs][1:-1] + [0],
        nt,
        nx,
        alpha,
        L,
        tmax,
    )

    analytical_solution = (
        [0]
        + [
            math.sin(math.pi * x / L) * math.exp(-tmax * alpha * (math.pi / L) ** 2)
            for x in xs[1:-1]
        ]
        + [0]
    )

    assert numerical_solution == pytest.approx(analytical_solution, abs=1e-2)


def test_step():
    assert step([0, 1, 1, 0], 0.04, 0.02, 0.01) == [0, 0.875, 0.875, 0]


def test_step_instability():
    with pytest.raises(Exception):
        step([0, 1, 1, 0], 0.04, 0.02, 0.1)
