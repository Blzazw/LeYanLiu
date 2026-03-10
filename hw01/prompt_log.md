# Prompt Log for HW01

## Overview
本日志记录了使用 AI 编程工具（Cursor + Claude 3.5 Sonnet）完成八皇后求解器项目的主要交互过程。

## Step 1: 项目初始化
**用户 Prompt**：初始化一个标准 Python 工程，包含 src/ 和 tests/ 目录，并添加 requirements.txt 用于 pytest。
**AI 操作**：创建了目录结构和空文件。

## Step 2: 实现求解器
**用户 Prompt**：编写一个函数 `solve_n_queens(n)`，使用回溯法返回所有 N 皇后问题的解。
**AI 响应**：生成了初始代码，包含回溯框架和 `is_safe` 检查。

## Step 3: 编写单元测试
**用户 Prompt**：为 N=4 和 N=8 编写 pytest 测试，验证解的个数以及每个解的有效性。
**AI 响应**：生成了 `tests/test_solver.py`。

## Step 4: 故意引入 Bug（用户手动操作）
在 `is_safe` 函数中故意修改了对角线检查条件，将 `abs(board[r] - col) == row - r` 改为 `board[r] - col == row - r`。

## Step 5: 运行测试，发现失败
测试 N=8 时得到 157 个解（期望 92），且部分解无效。

## Step 6: AI 调试
**AI 分析**：对角线冲突检查有误，缺少 `abs` 导致只检测一个方向。建议修改为 `abs(board[r] - col) == row - r`。

## Step 7: 修复 Bug
应用修复后所有测试通过。

## Step 8: 代码优化
添加类型提示和详细文档字符串。

## 总结
- AI 工具能快速生成项目骨架和测试代码。
- 清晰的错误日志有助于 AI 精准定位 Bug。
- 微小的逻辑错误（如缺少 `abs`）会导致结果大幅偏离，AI 能根据错误模式推断出根本原因。