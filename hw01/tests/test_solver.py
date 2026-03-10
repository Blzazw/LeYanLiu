import pytest
from src.solver import solve_n_queens


def is_valid_solution(board: list[int]) -> bool:
    """验证一个解是否合法（任意两个皇后不冲突）"""
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                return False
    return True


def test_n4():
    solutions = solve_n_queens(4)
    assert len(solutions) == 2  # 4 皇后有 2 个解
    for sol in solutions:
        assert is_valid_solution(sol)


def test_n8():
    solutions = solve_n_queens(8)
    assert len(solutions) == 92  # 8 皇后有 92 个解
    for sol in solutions:
        assert is_valid_solution(sol)


def test_n1():
    solutions = solve_n_queens(1)
    assert len(solutions) == 1
    assert is_valid_solution(solutions[0])