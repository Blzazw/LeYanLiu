"""
八皇后问题求解器
使用回溯算法返回所有解，每个解为每行皇后所在的列索引列表
"""

from typing import List


def solve_n_queens(n: int) -> List[List[int]]:
    """
    求解 N 皇后问题

    Args:
        n: 棋盘大小

    Returns:
        所有解的列表，每个解是一个长度为 n 的列表，表示每行皇后所在的列索引
    """
    result: List[List[int]] = []
    board = [-1] * n  # board[row] = column index

    def is_safe(row: int, col: int) -> bool:
        """检查在 (row, col) 放置皇后是否与已放置的皇后冲突"""
        for r in range(row):
            # 检查列冲突和对角线冲突
            if board[r] == col or abs(board[r] - col) == row - r:
                return False
        return True

    def backtrack(row: int) -> None:
        if row == n:
            result.append(board.copy())
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # 回溯

    backtrack(0)
    return result