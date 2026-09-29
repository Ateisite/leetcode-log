# CLAUDE.md - LeetCode 刷题项目

> 新对话启动时自动加载，帮助 Claude 快速了解上下文。

## 项目概述

- 路径：`E:\02_Learning\Programming\LeetCode\`
- GitHub：https://github.com/Ateisite/leetcode-log.git
- 语言：Python 3
- 目标：Hot 100 → 专题练习 → 365 题

## 当前进度

已完成 8 题（全部 Easy），详见 progress.md。

## 每日刷题流程

1. 从 `solutions/0000template.py` 复制，命名为 `00XX题目名.py`
2. 粘贴题目描述到文件头部注释
3. 用户自己写代码（**不要代写**，只给提示）
4. 用户去 LeetCode 提交验证
5. 通过后回填：Idea（英文）、Complexity、Submission Log、Time spent
6. 更新 progress.md
7. git add → commit → push

## Commit 格式

```
LeetCode #XXX 题目名 (Easy/Medium/Hard)

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
```

## Git 操作

```bash
cd "E:\02_Learning\Programming\LeetCode"
"E:\06_Software\Git\cmd\git.exe" add <files>
"E:\06_Software\Git\cmd\git.exe" commit -m "message"
"E:\06_Software\Git\cmd\git.exe" push
```

## 用户偏好

- **不要代写代码**：用户是初学者，需要自己思考。可以给提示、解释概念、指出错误，但代码必须用户自己写
- Idea 部分用英文
- 用户是跨专业（风景园林 → AI），Python 基础薄弱，解释概念时要从基础讲起
- 用户习惯用中文交流

## 文件结构

```
LeetCode/
├── 刷题笔记.md      ← 技巧、踩坑记录、算法模式
├── progress.md      ← 每日进度日志
├── solutions/       ← 每道题一个文件
│   ├── 0000template.py
│   ├── 0001XXX.py
│   └── ...
└── CLAUDE.md        ← 本文件
```

## 常见错误速查

| 错误 | 正确写法 |
|------|---------|
| `for i in len(s)` | `for i in range(len(s))` |
| `len(s)/i`（字符串乘法） | `len(s)//i` |
| `digits[len(digits)]` | `digits[len(digits)-1]` 或 `digits[-1]` |
| 中文冒号 `：` | 英文冒号 `:` |
| `return False` 在循环内 | 循环结束后再 `return False` |

详见 刷题笔记.md。
