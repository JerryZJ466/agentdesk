# AgentDesk 开发与学习主计划

版本：v2.0；审核日期：2026-10-29。计划目标不等于已完成成果。

本文件与 HTML 由 plan.source.json 生成；PDF 是同版本固定快照。进度证据记录在 [PROGRESS](../PROGRESS.md)。

## AgentDesk 开发与学习主计划

v2.0 | 2026-10-29 审核版 | 独立 AI 应用 / Agent 工程项目

> 主路线：后端与确定性基线 → 单 Agent 与早期 harness → 检索与 Web → 审批、沙箱、恢复 → 评测和交付。

构建一个虚构 SaaS 支持工单调查助手：查工单、可见文档和日志，给出带证据的诊断；需要重试导出时先提出具体操作，审批后执行并核实回执。它与 MeetLoop 的业务、仓库、数据库和部署完全独立。

| 已有准备 | 不能视为完成 |
| --- | --- |
| 公开仓库、课程与源码地图、虚构数据、12 个开发集规格、策略设计示例。 | Agent 运行时、权限执行、沙箱、自动评分器、真实模型评测和部署均未实现。 |
| 本版统一阶段、工时、验收与岗位差距；补 Web 基础、数据生命周期和 FDE 交付。 | 你的 Python / SQL 独立能力、环境和实际可用 API 仍需 A0-A2 验证。 |

主目标是 AI 应用 / Agent 工程；A7 增加 FDE 交付训练。模型服务平台为独立进阶分支，训练算法、CUDA 内核和分布式训练不在本项目主线。

唯一执行口径：plan.source.json 生成 plan.md / plan.html / 本 PDF。START_HERE 与 PROGRESS 使用同一阶段 ID；旧 v1.0 的 44 周与 400h 排期归档，不再驱动任务。

## 阶段总表与面试出口

新版显式计入 Web、数据维护与交付；主线 450-650h

| 阶段 | 本阶段 | 累计 | 完成后能做什么 |
| --- | --- | --- | --- |
| A0 环境与 Python 起点 | 10-15h | 10-15h | 读取虚构工单，独立写带范围的查询与断言。 |
| A1 后端与确定性基线 | 50-70h | 60-85h | Python / HTTP / SQL 基础、受限只读 API 和可重复基线。 |
| A2 LLM 与 Agent 循环 | 45-65h | 105-150h | 自己写一次小循环，接一种 SDK，具备早期 harness。 |
| A3 检索与数据生命周期 | 40-60h | 145-210h | 可见资料检索、引用、索引更新与删除均有验证。 |
| A4 React Web 控制台 | 60-85h | 205-295h | 掌握 DOM / CSS / React、API 联调、鉴权与事件流。 |
| A5 权限与受控写入 | 55-80h | 260-375h | 操作绑定审批、执行时复查、幂等与回执。 |
| A6 沙箱与持久化恢复 | 80-115h | 340-490h | 隔离执行、worker 重启、未知结果对账与取消传播。 |
| A7 系统评测与交付 | 110-160h | 450-650h | 冻结评测、测量优化、部署恢复、两轮试用与 FDE 演练。 |

A0-A4 累计 205-295h，是只读 AI 应用作品的首次投递检查点；A0-A5 累计 260-375h，增加受控操作。两处都必须能独立演示小闭环、解释权限与失败处理并提供真实评测证据，才考虑投递对应实习；没有通过关卡就延长。

> A0 → A1 → A2 → A3 → A4 → A5 → A6 → A7。评测、权限、日志和预算从前期就有最小版本；后续阶段加深。工时包括学习、实现、测试与正常返工，不是招聘行业统计。

## A0-A1：后端基础与确定性工作流

A0 10-15h；A1 50-70h | 前期不需要模型 API 或 GPU

| 顺序 | 实现任务 | 完成后应能 |
| --- | --- | --- |
| Python 起点 | 虚拟环境、模块、类型、列表 / 字典、异常；读取 tickets.json；pytest。 | 独立改查询规则，区分没有数据、权限拒绝与程序故障。 |
| 数据与权限 | 从可信测试身份查询；租户和资源 ACL 校验；SQLite 学 SQL，迁移到 PostgreSQL 前掌握事务 / 约束。 | u-n-viewer 能读 T-1001，不能读 T-2001；伪造参数不能改身份。 |
| API 与连接器 | FastAPI / Pydantic、HTTP 状态与 schema、超时、有限重试、连接池与取消。 | 一个受限只读 API 能被测试和 curl 调用；不把所有错误返回 200。 |
| 确定性基线 | 固定步骤查工单 → 日志 → 规则手册 → 结构化结论；记录 run_id 与耗时。 | 说明为什么此流程不需要 Agent；之后所有模型改进都与它比较。 |

学习阶段用明确的测试身份注入；它不是登录方案。A4 接用户入口前完成真正的服务端会话 / 身份校验；不能信任前端 header 中自报的 tenant_id 或角色。

### A1 关卡

60 分钟独立增加一个只读查询接口、SQL 条件和无权测试；解释同步 / 异步边界与事务；从干净环境复现基线。基础卡住时补练，不按“第 5 周必须用模型”跳级。

资料：[Python 官方教程](https://docs.python.org/3/tutorial/) · [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/) · [pytest 入门](https://docs.pytest.org/en/stable/getting-started.html) · [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html)

## A2：LLM 基础与自己的小循环

45-65h | 先 scripted Mock，再真实模型，再迁移一种 SDK

| 内容 | 实验与产出 |
| --- | --- |
| LLM 基础 | token / 上下文、随机输出、结构化输出、工具调用；对同一任务改变提示或上下文，解释输出变化。工具调用是模型建议，实际执行由宿主决定。 |
| 教学循环 | 组装上下文 → 请求模型 → 解析动作 → 参数校验 / 授权 → 工具执行 → 记录结果 → 下一轮或终止。先只读，不做自动写入。 |
| 最早的 harness | 最大轮数、run / tool 超时、取消、输出字节上限、预算、重复无效调用检测；run_events 带序号并写入 SQLite，供追踪和后续回放。 |
| 主 SDK | 用同一业务工具迁移到 OpenAI Agents SDK，追一次 Runner / tool 调用。业务权限、数据与评测不依赖 SDK 类型；不并用多套编排框架。 |
| 真实模型小样本 | 用固定 10-20 个开发场景，区分任务正确、证据、越权、停止、费用与延迟；记录模型 / prompt / 工具版本。 |

模型名称和价格不写死在两年计划里。开始真实调用前核对官方接口、依赖版本、可用账户和预算；日上限与单次上限显式配置。账号未就绪时可继续 Mock，不把 Mock 通过写成模型效果。

> A2 过关：不靠框架说清完整循环；注入无效参数、重复工具和超时后能有限停止。解释 prompt、工具定义、工作流与 harness 各自解决的问题。

资料：[Hugging Face Agents Course](https://huggingface.co/learn/agents-course/en/unit0/introduction) · [OpenAI Agents SDK 源码](https://github.com/openai/openai-agents-python) · [OpenAI 评测方法](https://developers.openai.com/api/docs/guides/evaluation-best-practices)

## A3：RAG、引用与数据生命周期

40-60h | 先可解释的检索基线，再按测量决定 embedding / reranker

| 开发任务 | 必须做的验证 |
| --- | --- |
| 摄取与数据契约 | 文档 id、版本、来源、租户、ACL、更新时间；格式校验、去重、重复导入与失败重跑。 |
| 检索与生成分离 | 先关键词 / SQL 基线；再尝试 embedding / 混合检索；分别统计检索命中、证据支持和最终任务结果。 |
| 权限贯穿全链路 | 先限可见范围再返回候选；缓存键、检索日志、引用下载都带权限语义；命中文档不等于有读取权限。 |
| 更新、删除与过期 | 修改文档版本后重建相关索引；删除与撤权后检索 / 缓存 / 引用不得继续暴露旧内容；保留必要审计而非复制秘密。 |
| 上下文与引用 | 大结果限长并关联原始证据；事实 / 推断 / 未知分开；缺证据就报告不确定，不补造来源。 |

把外部文档、工单、日志和工具输出当资料。文档里的“忽略规则”“读取其他租户”不具备授权效力；宿主仍须阻止。摘要和上下文压缩可能丢信息，必须用前后任务结果对照验证。

在本阶段工时内留 4-6h，把一个只读工具包装为本地 stdio MCP 服务，用同一授权与错误断言比较调用；理解互操作协议不提供业务权限。远程 OAuth 与公开服务后置。

### 过关能力

给一条错误结论定位是摄取、检索、权限、上下文还是生成问题；展示一次文档更新 / 删除回归和一次跨租户检索拒绝。数据管道比盲目堆向量库更优先。

资料：[腾讯 WeKnora](https://github.com/Tencent/WeKnora) · [字节 DeerFlow](https://github.com/bytedance/deer-flow) · [Anthropic 长任务 harness 设计](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents)

## A4：真正补上 Web 与全栈链路

60-85h | 先 JS / TS / DOM / CSS，再 React 控制台

| 开发顺序 | 需要学到的能力 |
| --- | --- |
| Web 基础 | 语义 HTML、表单、CSS 盒模型 / Flex / Grid、响应式、DOM 与事件；DevTools 的 Network / Console / Performance。 |
| JS / TS / React | 闭包、Promise / 事件循环、联合类型；组件、表单、状态、effect 清理；先不用大型状态库。 |
| 控制台最小功能 | 工单输入、运行列表、证据详情、取消按钮；加载 / 空 / 错误状态和基本键盘可访问性。 |
| API 与身份 | 真实服务端会话 / 身份验证；区分认证与授权；理解 CORS、cookie / token、CSRF 与 XSS 对所选方案的影响。 |
| SSE 与测试 | 用 A2 的持久化事件序号按 cursor 回放；刷新 / 断线不重复执行业务；组件测试与一次端到端流程。业务恢复在 A6 加深。 |

如果已通过 MeetLoop M4，可用独立小测减少重复语言学习；DOM、CSS、浏览器与 Web 安全仍需实做。知识共享，代码和部署不共享；节省的时间用于故障与测试，不在两项目重复记账。

A4 首次做受控单实例部署与一轮试用：依赖锁定、离线测试 CI、配置外置、HTTPS 接入、健康检查和基础日志脱敏。A7 加深恢复与交付，不把首次部署全部拖到末期。

### 过关能力

手画浏览器 → HTTP → FastAPI → SQL → SSE 的链路；独立加一个表单字段并更新全链路校验；修复一次断线、过期会话或重复订阅问题。只做一个漂亮聊天窗口不能过关。

资料：[MDN Web 核心课程](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core) · [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) · [React Learn](https://react.dev/learn) · [Full Stack Open（选学）](https://fullstackopen.com/en/)

## A5：工具权限与人工审批

55-80h | 先受控模拟业务写入，不接真实客户系统

| 边界 | 实现和验收 |
| --- | --- |
| 身份与资源范围 | 身份来自可信登录上下文；所有工具与资源操作执行租户 / ACL / 角色检查；默认拒绝，不把鉴权放进 prompt。 |
| 操作绑定 | 审批记录绑定 actor、tenant、run、tool_call、工具名、规范化参数哈希、资源 / 策略版本、过期时间和批准人。 |
| 执行时复查 | 审批后改参数、撤权、资源状态变化或超时都需重查；审批不能赋予角色原本没有的权限。 |
| 幂等与回执 | 写工具使用 operation_id / 幂等键；业务执行与结果查询分开；重复投递必须关联同一业务操作。 |
| 前端与审计 | 显示具体动作、参数、影响与批准 / 拒绝；记录关联 ID、决策原因和最终事实，敏感字段脱敏。 |

首先实现 draft_reply 与 retry_export 的模拟链路；draft 不自动发送。A5 先迁移到 PostgreSQL，验证迁移与事务，再保存操作记录和未知结果；不长期维护两套数据库。A6 加 worker 重启 / 租约加固。区分“请求发出”“已确认执行”和“结果未知”。

> 关卡：篡改审批参数、重复点击、等待时撤权、工具响应丢失；行为与业务数据均符合断言。policy.example.json 只是规格，只有对应代码和测试实现后才算生效。

资料：[Agents SDK 人工审批与继续运行](https://openai.github.io/openai-agents-python/human_in_the_loop/) · [MCP 安全实践](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) · [AgentScope](https://github.com/agentscope-ai/agentscope)

## A6-1：沙箱和执行边界

A6 共 80-115h，含下一页恢复；此页先控制范围

### 分两步做，不直接开放任意代码

- 先用白名单 CSV 分析器执行固定逻辑；校验文件类型、路径、大小和输出上限。禁止通过路径遍历或符号链接逃出工作区。
- 需要运行模型生成代码时，先完成隔离执行器：每 run 独立工作区、非 root、只读输入、CPU / 内存 / 进程数 / 时间限制、默认拒绝出口网络。
- 不挂宿主主目录、Docker socket、云凭据或模型密钥；执行面仅得到任务所需数据；产物访问也检查租户和资源授权。
- 验证超时终止、取消、文件隔离、网络拒绝与清理；监控孤儿进程 / 容器，下一 run 不能继承上次文件。

Docker 是学习基线，不是对任意敌对代码的完整安全证明。OpenSandbox 可作为后续执行器替换实验；先理解控制面与执行面，再比较实现。跨 Mac / Windows / Linux 的容器限制需在实际环境验证。

### 过关能力

解释宿主权限、容器限制、文件隔离和网络策略分别在哪里生效；安全测试读取的是专门构造的诱饵数据，不使用个人秘密。E09 / E10 对应文件分析与超时回收。

资料：[Docker Engine 安全边界](https://docs.docker.com/engine/security/) · [OpenSandbox 当前仓库](https://github.com/opensandbox-group/OpenSandbox) · [OpenSandbox 文档](https://open-sandbox.ai/)

## A6-2：持久化、恢复与不确定结果

从单进程 / 单 worker 起步；分布式框架不是先修课

| 要实现 | 失败实验 / 证据 |
| --- | --- |
| Run 状态机 | created / running / waiting_approval / succeeded / failed / cancelled；需要排队时再加 queued；明确允许转移与版本检查。 |
| 事件和检查点 | 持久化运行目标、已完成步骤、审批、工具调用和回执；聊天文本不充当执行账本；恢复前重查身份和策略。 |
| 未知结果与对账 | 远端成功而响应丢失时进入待核实；查询 operation_id 再决定后续。用模拟外部系统作为可验证事实来源。 |
| 并发与取消 | 单 worker 跑通后再加 lease / fencing / version；旧 worker 不能覆盖新结果；取消与外部已执行事实分开。 |
| 重启与重复投递 | 在执行前、远端成功后本地记账前、恢复后分别中断；重复投递 / 审批重放不产生重复副作用。 |

不能凭框架 checkpoint 宣称 exactly-once。对于不支持幂等或查询回执的外部系统，必须描述局限、人工核实或补偿策略；不能靠重复调用赌结果。

> 关卡：E05 / E06 / E11 / E12 的规格成为真实测试；展示 worker 重启与最终数据库状态一致。自己的状态机足够时，不追加工作流平台。

资料：[Microsoft Agent Framework](https://github.com/microsoft/agent-framework) · [Google ADK Python](https://github.com/google/adk-python) · [Anthropic 长任务 harness 设计](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents)

## A7-1：评测与优化的方法

A7 共 110-160h，含下一页交付；评测从 A1 起持续积累

| 层次 | 何时 / 如何验证 |
| --- | --- |
| 确定性测试 | A1 起验证业务规则、SQL、权限、参数与预算；Mock 注入 429、超时、坏 JSON、重复投递。通过不等于模型有效。 |
| 开发集 | A2 起使用现有 12 个规格及新增任务；每次重置业务状态，记录输入 / 预期 / 工具轨迹 / 实际副作用。 |
| 留出评测 | A7 前冻结不同任务家族与表达的留出集，版本记录；公开后不能再声称秘密，调参用过的样本归入开发集。 |
| 指标 | 任务达成、引用支持、约束违规、恢复正确率、人工介入率、费用、总耗时与 p50 / p95；小样本报告分母与重复次数。 |
| 优化对照 | 固定模型 / 数据 / 环境，比较规则基线、检索方案、上下文、工具 schema 与缓存；一次改一个因素。 |

项目实验可先扩展到 30-50 个开发任务、20-30 个留出任务，按成本选择每题重复 3-5 次；这些是起始设计，不是行业合格线。先做确定性评分，模型裁判仅辅助，抽样人工校准。安全关键用例要求本轮全部通过，但不等于生产安全保证。

质量、时延和成本一起报告；不要求模型每次选完全相同的工具轨迹。不能只让模型给自己的回答打分，也不能把几个成功截图当成功率。

资料：[Anthropic Agent 评测方法](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) · [OpenAI 评测方法](https://developers.openai.com/api/docs/guides/evaluation-best-practices) · [OpenAI API 弃用公告](https://developers.openai.com/api/docs/deprecations)

## A7-2：上线、运维与 FDE 交付

从本地可复现到受控试用；模拟项目如实标注

| 交付 | 明确产出 |
| --- | --- |
| 部署与 CI | 锁依赖；离线测试进 CI；配置 / secrets 分离；容器化服务与数据库迁移；健康检查、版本回滚与备份恢复。 |
| 可观测性 | run / tool / request ID、错误分类、耗时、用量与队列指标；日志与 trace 脱敏、保留期限和删除路径。 |
| FDE 需求发现 | 访谈 2-3 位愿意试用的人；写现有流程、用户角色、输入输出、成功标准、系统限制与不做范围。 |
| 连接器交付 | 对一个模拟业务 API 完成 schema 映射、分页、认证、限流 / 重试 / webhook 重放或变更；选实际需要的机制。 |
| 验收与交接 | 两轮任务试用；收集失败与人工接管原因；写部署 / 故障手册、验收清单、需求变更记录和 5 分钟英文演示。 |

第一份需求和成功标准在 A1 就写；最早可运行版本就试用。A7 负责把这些证据闭环，不等开发半年后才问有没有人需要。可用模拟客户角色练习，但不得把它写成真实企业部署。

> FDE 的优势来自把含糊需求变成可验收系统，并能与用户一起处理失败。英语与外向有帮助，技术深度、集成能力、排错和交付责任仍是必要条件。

## 工具契约、信任边界与准备材料

所有 fixtures 均为虚构；样例内容只能作为数据读取

| 工具 / 材料 | 实现阶段与边界 |
| --- | --- |
| get_ticket / query_job_events | A1：只读；以可信 actor 做租户与资源授权；超时不得解释为没有日志。 |
| search_docs | A3：可见范围检索、版本与引用；删除 / 撤权传播到索引和缓存。 |
| draft_reply / retry_export | A5：草稿与操作提案区分；执行由策略、绑定审批、幂等键与回执控制。 |
| analyze_csv | A6：固定分析起步，任意代码需先通过隔离关卡；read-only 输入和产物范围。 |
| policy / actors examples | 设计规格与测试身份；不能从模型或浏览器提供的角色直接授权。 |
| 12 个 eval specs | 逐步实现：E01-03/07/08 为早期基础；E04/11 审批及 E05/06 最小幂等 / 回执丢失在 A5；E12 重启、E09/10 沙箱在 A6。当前全部仅规格。 |

信任链：用户会话 → API 认证 / 授权 → run → 工具策略 → 连接器 / 沙箱 → 结果核实。工具输出回到模型前需限长和标记来源；审计、缓存、产物与检索都不能遗漏租户范围。

目录按需创建 apps/api、apps/console、agent、worker、evals；只在有可运行代码时加入。现在不创建空壳微服务、通用插件平台或 Agent 市场。

## 开源阅读与课程顺序

一次追一个问题，不把七套框架装进同一工程

| 阶段 | 资料 / 参考 | 读完交付什么 |
| --- | --- | --- |
| A0-A1 | Python / FastAPI / pytest / PostgreSQL。 | 可测试 API 与确定性基线。 |
| A2 | HF Agents 基础 + OpenAI Agents SDK。 | 教学循环与 SDK 对照；记录调用路径、commit、测试和改动实验。 |
| A3 | WeKnora + DeerFlow + harness 文章。 | 检索 ACL / 更新验证；大输出落盘与上下文压缩实验。 |
| A4 | MDN + React / TS；Full Stack Open 选 Web 部分。 | 控制台全链路；不为了课程追加 Node、MongoDB、GraphQL 三套服务。 |
| A5-A6 | AgentScope / ADK / Microsoft Agent Framework；MCP 安全；Docker / OpenSandbox。 | 分别学习审批、事件、恢复和隔离机制，只选与当关有关的一个。 |
| A7 | Agent 评测方法与自己的失败记录。 | 可复现实验、部署与需求验收。 |

DeerFlow 使用 LangGraph / LangChain，可学其机制，无需把依赖一起移入主线。框架源码只沿一条调用链阅读；目标是能替换一层、解释边界，而不是读完整个仓库。

资料：[Python 官方教程](https://docs.python.org/3/tutorial/) · [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/) · [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/en/unit0/introduction) · [OpenAI Agents SDK 源码](https://github.com/openai/openai-agents-python) · [腾讯 WeKnora](https://github.com/Tencent/WeKnora) · [字节 DeerFlow](https://github.com/bytedance/deer-flow) · [AgentScope](https://github.com/agentscope-ai/agentscope) · [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)

## 岗位覆盖与模型服务分支

应用工程、FDE、服务平台是相关但不同的岗位目标

| 方向 | 本项目能支撑 | 额外门槛 / 分支 |
| --- | --- | --- |
| AI 应用 / Agent | A1-A7：后端、工具、检索、权限、评测与交付。 | 编码 / DSA / SQL / 网络；真实 JD 的语言与年资；不能只演示框架。 |
| FDE | A7：需求澄清、客户系统集成、演示、验收与交接。 | 部分有 new-grad / intern，部分要求多年经验或差旅；英语外向不代替工程能力。 |
| 模型服务平台 | 主线仅有调用侧基础，不足以宣称完成平台方向。 | 另 100-160h：Linux、并发、排队 / 背压、配额、路由、取消、容量与故障测量。 |
| 推理内核 / 训练 Infra | 不在主线。 | C++ / CUDA、GPU 架构、分布式通信和性能分析等；不要混同于 API 平台。 |

服务分支先用 Mock 测 429、超时、有界队列与公平性，再在兼容 Linux / GPU 环境运行 vLLM，测 TTFT、token 间延迟、吞吐、KV / 显存和队列。Mac 不等于 CUDA 环境。现有 ServeLab 若已通过相同验收，引用自己的证据、补缺口即可，不重写第二个网关。

Web / 全栈若成为主求职方向，A4 / A7 后另留约 80-140h 浏览器、布局、测试与性能专项。不要把这个分支与平台分支同时加入主线。详细官方 JD 与证据限制见 JOB_REQUIREMENTS_AUDIT.md。

资料：[vLLM 服务指标](https://docs.vllm.ai/en/latest/usage/metrics/)

## 双线时间安排与求职节奏

总预算每周 21 小时起；课程、调试、测试、文档和面试都算在内

| 时期 / 条件 | MeetLoop | AgentDesk | 公共基础 |
| --- | --- | --- | --- |
| 现在至首轮 iOS 面试准备 | 13h | 5h | 3h |
| M3 过关后的默认安排 | 8h | 10h | 3h |
| 实习 / 考试导致时间减少 | 按真实余量保留一个主项 | 维持小步或暂停新功能 | 保留每周复盘 |

从 2026 年 11 月到 2027 年 2 月底约 17 周：约 221h 给 MeetLoop、85h 给 AgentDesk、51h 给公共基础。对应目标是 M3 的中低区间和 A1 完成；不是四个月内做完双项目。若起点不足或春节暂停，按关卡顺延。

两条主线各为 450-650h，合计 900-1300h；每周项目时间 18h，粗算约 50-73 个有效周。按 M3 过关即从 13/5 切到 8/10、完成一项后暂不重分配工时估算，约 52-75 周；再加 10%-20% 中断余量，约 14-21 个日历月。18 个月可争取中档完成，高档或大幅中断会更久。

### 投递不等全部完工

- 2026 年 12 月整理实习复盘与简历，开始关注官方岗位；M2 后可试投并记录面试缺口，M3 作为首轮目标。
- 春季 2027 上海优先、4-5 天 / 周、连续至少 3 个月；毕业时间、在读身份和具体到岗日期逐项核对，不因作品完成就默认有资格。
- 美国岗位按届别及在读要求提前查看；具体实习或工作资格以学校与雇主确认为准。本次不推断个人资格。

> 月度只调整工时与下一关。不要因岗位热词每周更换技术栈；岗位复核在 M3、A5 和正式投递前进行。

## 两个项目之外必须持续训练

公共 3h / 周单独记账；同一知识不在两个项目重复计时

| 能力 | 训练安排 | 能证明什么 |
| --- | --- | --- |
| 编码与数据结构 | 每周 90 分钟：数组 / 字符串 / 哈希、栈队列、二分、树与图、堆；再按 JD 补基础 DP。 | 能说复杂度、列边界、独立写代码；隔周重做并换条件。 |
| 网络 / OS / SQL | 每周 60 分钟轮换一个主题：HTTP / TLS / DNS、进程线程与并发、事务索引与查询计划。 | 能跟踪客户端到数据库的一次请求；用实验解释取消、锁或超时。 |
| 表达与复盘 | 每周 30 分钟：3 分钟演示、一次故障讲解或英文方案说明。 | 讲清问题、选择、证据与限制；区分自己完成与 AI 辅助。 |

Git 分支、差异审查、冲突与回滚；终端、Linux 进程 / 端口 / 日志；单元与集成测试、CI、依赖锁定和密钥管理，随着实际项目用到时练。不要把“会框架”当成已经会 SDE 基础。

### 每四周一次独立复测

- 先不开 AI，用 45-90 分钟完成一个新规则或工具；允许查官方文档。随后可以让 AI 审查差异。
- 拿一个未提前看答案的故障，写出复现步骤、假设、修复与回归。未通过就缩小任务补练，不能只重新播放课程。
- 普通业务与数据结构面试仍要练；数学不强不妨碍这条应用工程路线，但不能跳过复杂度、基础概率和测量思维。

资料：[Pro Git](https://git-scm.com/book/en/v2) · [MIT 6.006 算法课程](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) · [MIT Missing Semester](https://missing.csail.mit.edu/) · [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html)

## 从今天开始与最终验收

以 A0 为起点；没有实际运行就不打勾

- 第一周 5h：环境 / 基线 1h，Python 练习 1.5h，工单查询 1.5h，断言与独立改题 1h。零基础需要更多时间就继续 A0。
- 前四周共约 20h：目标是 A0 过关并开始 A1，只读查询与测试优先；不承诺此时已完成 API、SQL 和 Agent 循环。
- 每阶段更新 PROGRESS：复现命令、独立需求变更、失败实验、验证结果、暂未理解之处；AI 可以帮助，关键边界由自己解释和验证。

### 最终应具备的五种能力

独立编码一个受限工具；解释模型、工具、状态与业务的边界；定位检索 / 权限 / 恢复故障；用数据比较质量、费用与延迟；把用户需求变成可运行、可验收、可交接的系统。

当前已准备文档与虚构输入，尚无真实运行结果。未来主线完成可支撑部分应用工程 / FDE 岗位的项目面试，但不是覆盖所有大厂岗位或替代真实团队经历。

> SDK / 模型阶段开始时复核官方版本与接口。2026-10-29 核对的 OpenAI 公告将旧 Evals 平台与 Agent Builder 标为退役路径；本计划将评测数据、runner 和断言保存在自己的仓库，不绑定这些旧平台。

资料：[OpenAI API 弃用公告](https://developers.openai.com/api/docs/deprecations)
