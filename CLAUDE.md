# CLAUDE.md - LeetCode 刷题项目

> 新对话启动时自动加载，帮助 Claude 快速了解上下文。

## 项目概述

- 路径：`E:\02_Learning\Programming\LeetCode\`
- GitHub：https://github.com/Ateisite/leetcode-log.git
- 语言：Python 3
- 目标：Hot 100 → 专题练习 → 365 题

## 当前进度

> **每次新对话启动时**，读取 `代码随想录题单.md` 统计 ⬜/✅ 数量，自动知道当前进度。
> 不要在这里硬编码数字，以题单文件为准。

- 题单：`E:\03_Notes\Charlie_vault\Knowledge\LeetCode\代码随想录题单.md`
- 流水账：`E:\02_Learning\Programming\LeetCode\progress.md`
- 复习表：`E:\03_Notes\Charlie_vault\Daily\每日学习日志.md`

## 面试时间线

| 时间 | 刷题目标 | 投递策略 |
|------|---------|---------|
| 现在→寒假 | 数据结构+二叉树（~80题） | 投小厂/日常实习，**练面试** |
| 2027.2-3月 | ~100题 | 春招提前批，投暑假实习 |
| 2027.5月底 | **156题全部完成** | 暑假实习笔试高峰期 |
| 2027.9月 | 二刷高频 | 秋招正式 offer |

**寒假面试目标：不是拿 offer，是知道差在哪，回来针对性补。**

## 刷题路线（代码随想录顺序）

```
阶段1：数据结构基础
  数组(5题) → 链表(7题) → 哈希表(8题) → 字符串(7题) → 双指针(10题) → 栈和队列(7题)

阶段2：核心算法 ⭐ 当前阶段
  二叉树(35题) ← 从这里开始！面试最高频
  回溯算法(15题) → 贪心(17题)

阶段3：进阶
  动态规划(34题) → 单调栈(5题) → 图论(6题)

合计 156 题
```

> 当前专题和下一题：读取 `代码随想录题单.md` 第一个 ⬜ 题自动确定

## 自动做题流程

> 用户说"我要做题"或"下一题"时，Claude 自动执行以下步骤，不需要用户手动操作。

### 第1步：自动找下一题
- 读取 `E:\03_Notes\Charlie_vault\Knowledge\LeetCode\代码随想录题单.md`
- 找到第一个 ⬜ 的题（按专题顺序）
- 告诉用户：题号 + 题目名 + 难度 + 链接

### 第2步：自动建文件
- 从 `solutions/0000template.py` 复制
- 命名：`00XX题目名.py`（XX = 当前已做题数 + 1，用 progress.md 统计）
- 填入：题目描述、约束条件、示例
- 告诉用户：文件已建好，去写代码

### 第3步：用户写代码
- **不要代写**，只给提示
- 用户卡住时给适度引导
- 用户想自己尝试时不等不给思路

### 第4步：提交后更新（用户说"更新今日笔记"或"做完了"）
- 追问易错点 → 写入 `LeetCode刷题笔记.md` 的「易错题目回顾」
- 题单改 ⬜→✅，更新进度统计
- `每日学习日志.md` 追加复习行（+1/+3/+7/+15天）
- `progress.md` 追加当日记录
- git add → commit → push 到 GitHub

### Git 操作
```bash
cd "E:\02_Learning\Programming\LeetCode"
"E:\06_Software\Git\cmd\git.exe" add <files>
"E:\06_Software\Git\cmd\git.exe" commit -m "LeetCode #XXX 题目名 (Easy/Medium/Hard)"
"E:\06_Software\Git\cmd\git.exe" push
```

## Commit 格式

```
LeetCode #XXX 题目名 (Easy/Medium/Hard)

Co-Authored-By: Claude Code <noreply@anthropic.com>
```

## Git 操作

```bash
cd "E:\02_Learning\Programming\LeetCode"
"E:\06_Software\Git\cmd\git.exe" add <files>
"E:\06_Software\Git\cmd\git.exe" commit -m "message"
"E:\06_Software\Git\cmd\git.exe" push
```

**代理**：不需要代理，直连即可

## 用户偏好

- **不要代写代码**：用户是初学者，需要自己思考。可以给提示、解释概念、指出错误，但代码必须用户自己写
- **用户想先自己尝试**：先不给思路提示，等用户问或卡住再给适度引导
- Idea 部分用英文
- 用户是跨专业（风景园林 → AI），Python 基础薄弱，解释概念时要从基础讲起
- 用户习惯用中文交流

## 文件结构

```
LeetCode/
├── progress.md      ← 每日进度日志
├── solutions/       ← 每道题一个文件
│   ├── 0000template.py
│   ├── 0001XXX.py
│   └── ...
└── CLAUDE.md        ← 本文件

笔记文件（Obsidian vault）：
E:\03_Notes\Charlie_vault\Knowledge\LeetCode\LeetCode刷题笔记.md
```

## 常见错误速查

| 错误 | 正确写法 |
|------|---------|
| `for i in len(s)` | `for i in range(len(s))` |
| `len(s)/i`（字符串乘法） | `len(s)//i` |
| `digits[len(digits)]` | `digits[len(digits)-1]` 或 `digits[-1]` |
| 中文冒号 `：` | 英文冒号 `:` |
| `return False` 在循环内 | 循环结束后再 `return False` |

详见笔记文件。
