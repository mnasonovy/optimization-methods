from typing import Callable, Tuple, List

def fibonacci_method(
        f: Callable[[float], float],
        a: float,
        b: float,
        N: int,
        verbose: bool = False
    ) -> Tuple[float, float, int, List[Tuple[float, float]], float, float, float]:

    F = [1, 1]
    while len(F) < N + 1:
        F.append(F[-1] + F[-2])

    history = [(a, b)]
    n_iter = 0

    epsilon = 1e-10
    k = 1

    x1 = a + (F[N - 2] / F[N]) * (b - a)
    x2 = a + (F[N - 1] / F[N]) * (b - a)
    f1 = f(x1)
    f2 = f(x2)
    n_iter = 2

    while n_iter + 1 < N:
        if f1 <= f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (F[N - k - 3] / F[N - k - 1]) * (b - a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (F[N - k - 2] / F[N - k - 1]) * (b - a)
            f2 = f(x2)

        n_iter += 1
        k += 1
        history.append((a, b))

    if f1 <= f2:
        b = x2
    else:
        a = x1

    # финальный шаг
    if f1 <= f2:
        b = x2
        x1 = (a + b - epsilon) / 2
        f1 = f(x1)
        n_iter += 1
    else:
        a = x1
        x2 = (a + b + epsilon) / 2
        f2 = f(x2)
        n_iter += 1

    if f1 <= f2:
        b = x2
    else:
        a = x1

    x_min = (a + b) / 2
    f_min = f(x_min)
    delta = b - a

    # эти переменные ты должен определить сам
    x_theoretical_min = None
    f_theoretical_min = None

    error_x = 0 if x_theoretical_min is None else abs(x_min - x_theoretical_min)
    error_f = 0 if f_theoretical_min is None else abs(f_min - f_theoretical_min)

    history.append((a, b))

    return x_min, f_min, n_iter, history, delta, error_x, error_f
