# AgentDesk

企业工单调查与受控执行助手：后端、Agent循环、检索、Web控制台、权限、沙箱、恢复、评测与交付。

## 当前状态

目前只有计划、文档和虚构fixtures；没有Agent运行时、权限引擎、沙箱或评分器。12条eval仍是SPEC_ONLY，不能当作已通过测试。 本次完成的是开工准备与计划审核，功能目标不代表已经掌握。

## 只从这份计划开始

- **[当前主计划 v2.0](docs/plans/plan.md)**：阶段顺序、工时、开发任务、验收及学到什么。
- [今天和前四周](docs/START_HERE.md)：第一项任务，无需先读完全部资料。
- [进度账本](docs/PROGRESS.md)：各关卡当前均待开始，用代码和验证证据更新。
- [岗位能力审核](docs/JOB_REQUIREMENTS_AUDIT.md)：官方样本、缺口与角色边界。
- [准备工作审核](docs/PREPARATION_AUDIT.md) · [时间与面试评估](docs/面试准备与时间评估.md) · [公共基础](docs/COMMON_FOUNDATIONS.md)
- [本机HTML版](docs/plans/plan.html) · [当前PDF快照](docs/plans/AgentDesk_开发与学习主计划_v2.0_2026-10-29.pdf)

主目标是AI应用/Agent工程，FDE增加需求和交付训练；模型服务平台另有分支。先确定性流程和教学循环，再一种主SDK，不局限于LangChain，也不堆框架。

## 时间与优先级

首轮iOS实习准备默认每周MeetLoop 13h、AgentDesk 5h、公共基础3h；M3过关后默认8h/10h/3h。主线各450-650h，以实际关卡推进；两条并行含中断余量约14-21个月，不能把18个月当录用承诺。选修分支另计。

## 独立迭代

按需增加 `apps/api`、`apps/console`、`agent`、`worker`、`evals`；只创建实际用到的部分。 本项目不依赖另一个项目的代码、文件或服务。远程仓库：[JerryZJ466/agentdesk](https://github.com/JerryZJ466/agentdesk)，public，默认分支main。

开始工作前拉取最新提交；每次完成可解释的小变化后检查diff、验证、commit和push。真实凭据、运行数据与本机历史资料保持Git忽略；依赖锁文件提交。

## 文档维护与历史

`docs/plans/plan.source.json` 是内容源；`python tools/build_plan_html.py` 同时生成Markdown与HTML。PDF为同版本固定快照，修改源后须另外更新PDF；元数据在`docs/CURRENT_PLAN.json`。**旧PDF仅供历史参考，执行顺序与工时以当前主计划为准。**

- [虚构数据说明](fixtures/准备材料说明.html)
- [开源阅读地图](docs/开源阅读地图.html)
- [旧v1.0 PDF（历史）](docs/plans/AgentDesk_Agent工程学习执行计划_v1.0_2026-10-28.pdf)
