# AgentDesk

企业工单排查与受控执行助手，用于深入学习 Agent 运行循环、工具、上下文、权限、沙箱、持久化恢复、评测与上线交付。

## 当前状态

目前包含计划、文档和虚构准备数据；尚未实现 Agent 运行时、权限引擎、沙箱或评分器。`fixtures` 中的策略与评测样例是规格，不会自动提供安全保护。

## 从这里开始

- [完整执行计划](docs/plans/plan.html)
- [学习时间与面试验收](docs/面试准备与时间评估.md)
- [前四周任务](docs/START_HERE.md)
- [开源阅读地图](docs/开源阅读地图.html)
- [准备材料说明](fixtures/准备材料说明.html)
- [完整计划 PDF](docs/plans/AgentDesk_Agent工程学习执行计划_v1.0_2026-10-28.pdf)

当前时间估算以“学习时间与面试验收”为准；PDF 保留完整阶段与课程细则。

## 产品范围

用户提交工单 → 查询当前租户可见的文档和日志 → 给出证据与建议 → 展示待审批操作 → 授权后执行 → 查询回执并记录审计。

先做确定性工作流和小型教学循环，再用一种 SDK 承接主项目。默认参考 OpenAI Agents SDK；借鉴其他项目的机制，不把多个框架叠加为前置依赖。

后续使用 Python / FastAPI、PostgreSQL 与简单的 TypeScript / React 控制台。模型服务平台作为独立进阶阶段。

## 目录

```text
docs/                 计划、阅读地图与验收标准
fixtures/             虚构工单、文档、日志、策略示例与 12 个评测规格
tools/                独立文档生成工具
_local/               本机校验记录，Git 已忽略
```

实现时按需增加 `apps/api`、`apps/console`、`agent`、`worker`、`evals` 和测试目录。现在不创建空壳运行时。

## 第一项练习

用 Python 读取 `fixtures/tickets.json`，实现按可信测试身份查询工单：`u-n-viewer` 可以读取 `T-1001`，不能读取 `T-2001`。给正常、缺失与无权路径写断言。此练习不需要模型 API。

## 文档更新

`docs/plans/plan.source.json` 是本仓库独立的计划源文件。运行 `python tools/build_plan_html.py` 更新 HTML。PDF 是固定快照，不会随 HTML 自动更新。

## 仓库与迭代

远程仓库：[GitHub 上的 agentdesk](https://github.com/JerryZJ466/agentdesk)。默认分支为 `main`，当前设为私有。此项目不依赖 MeetLoop 的代码、文件或服务。

每次完成一个可解释、可验证的小任务后提交：

```bash
git status
git add <本次修改的文件>
git commit -m "描述本次完成的变化"
git push
```

跨设备开始工作前先拉取最新提交；较大的实验使用独立分支。历史资料、凭据与运行数据按 `.gitignore` 保持在本地。计划、虚构样例和应用源码随仓库迭代。
