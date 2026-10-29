# 每天3小时：首28天学习清单

版本v1.0；2026-10-29；Windows起步，Mac到货后补UI。与MeetLoop v3.1 / AgentDesk v2.1配套；任务尚未执行。

## 每天 3 小时：首 28 天学习清单

2026-10-29 | Windows 起步，Mac 到货后补 UI | 执行补充 v1.0

> 主线：Swift / iOS先扎实，Agent从Python与只读后端开始。课程是练习的入口；每天留下能运行、能改题、能解释的证据。

这是MeetLoop v3.1与AgentDesk v2.1的起步补充，不改变两个独立项目的业务。前28天日程以本清单为准；旧START_HERE中第一周就建好列表的安排只适用于已有独立基础且Mac可用的情况。

| 每7天循环 | 安排 | 本周合计 |
| --- | --- | --- |
| 第1、2、4、5天 | iOS各3h | 12h iOS |
| 第3天 | Agent 3h | 3h Agent |
| 第6天 | Agent 2h + 公共1h | 2h Agent + 1h公共 |
| 第7天 | iOS复盘1h + 公共2h | 1h iOS + 2h公共 |

每天180分钟是含短休息的占用时段；一周21h中有效学习通常约18-19h。既往长期估时按有效工时估算，今后用实际日志校正，不能把休息和下载等待算成学习成果。

### 每日固定节奏

常规单线日：回忆10min → 课程45min → 休息10min → 编码65min → 休息10min → 独立改题25min → 记录15min。配对章节允许课程到60min，从编码段挪15min；总量不增加。混合日按2h+1h或1h+2h拆块，短休息从各块内扣。

D1表示你真正开始的第一天，不硬绑定星期。若今天开始且不中断，D28为2026-11-25；遇学校事务就顺延。不是28天必须追完28个课程单元。

## 资料怎么用：一门主课，按问题查阅

课程目录核查：2026-10-29 | 不把“看完”当作“掌握”

### 100 Days of SwiftUI：现在的主课

先做语言单元1-15，再用16-18做WeSplit。文字或视频选一种主载体，另一种仅在卡点时补充。每10-15分钟停下运行，再关页面复写和改条件。Checkpoint与挑战要动手；Optional Reading不要求一次读完。

### Swift 官方指南：查漏，不从头背

遇到Optional、值与引用、协议、闭包时，只读对应一节，做一个10-20行小实验。保存“问题→预测→实际输出→解释”，不抄长篇知识笔记。

### Stanford CS193p：通过第一项SwiftUI独立改题后再加

官网目前公开2025版。模型与UI不清楚看Lecture 3；数据流看5/6；列表导航看10。每次20-30分钟片段替换当天课程时间，然后做自己的变式；不额外追整套CodeBreaker作业。若要系统学全课，另排作业工时。

### Apple Today：M3 的UIKit专项

在本地闭环、网络与排错基础上，跟做UIKit列表/详情，再移植MeetLoop一页。后置是为了控制负荷，并不是UIKit技术上必须先学SwiftUI。

### Agent 与公共课：目前只开必要章节

Python按列表/字典→函数→JSON/异常→pytest→SQL顺序；不通读整本。Pro Git实际操作。MIT 6.006只作以后复杂度与数据结构参考，首月不并行整套视频。RN、Kotlin、Go、Agent SDK与开源框架阅读按后续关卡解锁。

资料：[100 Days of SwiftUI 总目录](https://www.hackingwithswift.com/100/swiftui) · [Swift 官方语言指南](https://docs.swift.org/latest/documentation/the-swift-programming-language/) · [Stanford CS193p 2025](https://cs193p.stanford.edu/) · [Apple Today UIKit](https://developer.apple.com/tutorials/app-dev-training/getting-started-with-today) · [Python 第3章：入门](https://docs.python.org/3/tutorial/introduction.html) · [Pro Git：记录每次更新](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)

## 今天在 Windows 上怎么开始

只做D1；今天不配置iOS模拟器，也不购买API或GPU

| 时间 | 要完成的动作 |
| --- | --- |
| 00:00-00:20 | 打开SwiftFiddle，运行print；用15分钟尝试表达活动数据。创建本地练习文件；Git不会可等D6补。 |
| 00:20-00:55 | 读或看100 Days单元1，练let、var、String、Int与简单运算。 |
| 00:55-01:05 | 休息。 |
| 01:05-02:05 | 自己写活动标题、容量、人数、剩余名额；分别运行10/3、10/10、1/0，预测输出再核对。 |
| 02:05-02:15 | 休息。 |
| 02:15-02:45 | 关闭课程复写，换输入；故意把let重新赋值，看编译错误并修复。 |
| 02:45-03:00 | 另存day01.swift；记录今天理解的3点、1个错误和明天任务。 |

SwiftFiddle是第三方在线Swift运行器，适合这些虚构的小练习；Ctrl+Enter运行。源码另存本地，网页Ctrl+S是分享操作，不当作本地保存。无需点击Share，也不放入实习公司的代码。

如服务不可用，先读单元1、在本地写出并预测结果；运行验收标待做。Windows长期使用可依官方教程安装Swift工具链，其Visual Studio依赖可能较大，配置卡住30分钟就换备用任务。

纯Swift能在Windows运行；iOS/SwiftUI应用需要Mac与Xcode。Mac到后用下一个iOS时段确认正式工具链、拉取自己的仓库、创建并运行最小工程，记录版本。UI课可顺延，已经完成的语言课不用重刷。

资料：[100 Days 单元 1](https://www.hackingwithswift.com/100/swiftui/1) · [SwiftFiddle 在线运行器](https://swiftfiddle.com/) · [Swift Windows 官方安装](https://www.swift.org/install/windows/) · [Swift 官方起步与平台要求](https://www.swift.org/getting-started/)

## 第 1 周每日清单 · 上

180分钟/天；卡住时替换后续任务，不叠加作业。所有复选框初始均未完成。

### D01 Windows 开始：变量与活动信息

iOS3h | 资料：100 Days 单元 1、SwiftFiddle 在线运行器

- [ ] 学：先用15分钟尝试写活动标题、容量和已报名人数；不会就留空。看单元1必修部分，视频和文字选一种。
- [ ] 做：SwiftFiddle运行一个print；自己写标题、capacity、registered和剩余名额，输入10/3、10/10、1/0三组数据。代码另存本地.swift文件。
- [ ] 验收：关闭教程重写变量和减法，解释let与var；记录一个编译错误及修复。今天不要求struct、筛选函数或SwiftUI。

### D02 布尔与输出：把活动说清楚

iOS3h | 资料：100 Days 单元 2

- [ ] 学：单元2：布尔、字符串插值；完成Checkpoint 1。能独立做对的内容只查漏。
- [ ] 做：输出“活动名称、容量、已报名、剩余名额”；练习布尔值表达是否公开。不要提前写复杂报名流程。
- [ ] 验收：换标题和数字仍能运行；不靠复制能解释Int、String、Bool各放什么。

### D03 Python 环境与工单字典

Agent3h | 资料：Python 第3章：入门、Python 第5章：数据结构、Python 第12章：虚拟环境

- [ ] 学：只读第3章字符串/列表，第5章字典，第12章venv的入门段落，总阅读控制在35分钟。
- [ ] 做：确认Python，创建项目隔离环境；写两个虚构工单字典，打印ticket_id与subject；保存执行命令。
- [ ] 验收：合上资料从空文件重写一个字典与取值；解释列表和字典区别。环境卡住就顺延功能。

### D04 集合与类型：选择合适的数据结构

iOS3h | 资料：100 Days 单元 3、100 Days 单元 4

- [ ] 学：单元3加单元4的类型标注；先读必修、边敲边做，Optional Reading留作查询。配对单元太多就拆成两个iOS时段。
- [ ] 做：数组放三个活动标题；字典以ID查标题；Set去掉重复ID；枚举表示活动类别。此时不要求提前写Activity结构体。
- [ ] 验收：给四个小例子换数据；解释为什么不能依赖Set固定顺序，为什么字典键要唯一。

资料：[100 Days 单元 1](https://www.hackingwithswift.com/100/swiftui/1) · [SwiftFiddle 在线运行器](https://swiftfiddle.com/) · [100 Days 单元 2](https://www.hackingwithswift.com/100/swiftui/2) · [Python 第3章：入门](https://docs.python.org/3/tutorial/introduction.html) · [Python 第5章：数据结构](https://docs.python.org/3/tutorial/datastructures.html) · [Python 第12章：虚拟环境](https://docs.python.org/3/tutorial/venv.html) · [100 Days 单元 3](https://www.hackingwithswift.com/100/swiftui/3) · [100 Days 单元 4](https://www.hackingwithswift.com/100/swiftui/4)

## 第 1 周每日清单 · 下

180分钟/天；卡住时替换后续任务，不叠加作业。所有复选框初始均未完成。

### D05 条件分支：活动满员怎么办

iOS3h | 资料：100 Days 单元 5

- [ ] 学：单元5的if与switch；三元表达式能读懂即可，不强求把每个分支压成一行。
- [ ] 做：对剩余名额>0、=0、<0打印“可报名、满员、数据异常”；用switch按类别输出标签。
- [ ] 验收：用正常、满员、异常三组输入验证；说明为什么显示负名额时不能继续当作正常报名。

### D06 Python 函数 + Git 入门

Agent2h + 公共1h | 资料：Python 第4章：控制流与函数、Pro Git：记录每次更新

- [ ] 学：Agent 120分钟：读if、for与Defining Functions约25分钟。公共60分钟：Pro Git的status、diff、add、commit。
- [ ] 做：Agent：内存数组实现find_ticket(id)，没找到返回None。公共：检查自己改动，只提交当天练习，不提交.venv。各时段含短休息。
- [ ] 验收：Agent正常/未知ID/空数组三个断言；公共解释工作区与暂存区。今天还不加JSON、权限或HTTP。

### D07 第一周回顾 + 数组与去重

iOS1h + 公共2h | 资料：100 Days of SwiftUI 总目录、Pro Git：记录每次更新

- [ ] 学：iOS 60分钟只补D1-D5遗漏。公共120分钟：数组和Set概念、手工去重例子90分钟，口述30分钟。
- [ ] 做：iOS关闭课程复写一组活动信息和满员分支。公共用纸或Swift描述按顺序去重，给空输入和重复输入；尚不会循环可先画步骤。
- [ ] 验收：录2分钟说明变量、集合和条件。列出未通过任务，下周先补；不能因为到了周末就勾完。

资料：[100 Days 单元 5](https://www.hackingwithswift.com/100/swiftui/5) · [Python 第4章：控制流与函数](https://docs.python.org/3/tutorial/controlflow.html) · [Pro Git：记录每次更新](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository) · [100 Days of SwiftUI 总目录](https://www.hackingwithswift.com/100/swiftui)

## 第 2 周每日清单 · 上

180分钟/天；卡住时替换后续任务，不叠加作业。所有复选框初始均未完成。

### D08 循环与筛选

iOS3h | 资料：100 Days 单元 6

- [ ] 学：单元6；完成Checkpoint 3或同等难度独立题。
- [ ] 做：遍历一组剩余名额，输出可报名项目；测试空数组、全满、都可报名。
- [ ] 验收：先预测输出再运行，解释循环执行次数；把“>0”改为“>=2”并说明结果。

### D09 函数：把规则从打印里拿出来

iOS3h | 资料：100 Days 单元 7、100 Days 单元 8

- [ ] 学：单元7、8核心：参数、返回值、默认值、throw。先用普通返回值；错误处理难就留下一iOS时段。
- [ ] 做：写remainingSeats与canRegister函数，调用方负责打印；给无效容量的处理写清规则。
- [ ] 验收：正常、满员、负容量至少3个assert；解释return与print区别。不会的单元继续补，不强行结束。

### D10 读取真实夹具与租户隔离

Agent3h | 资料：Python 第7章：文件与JSON、Python 第8章：异常

- [ ] 学：Python第7章7.2/7.2.2与第8章基础异常；读agent/fixtures说明。
- [ ] 做：读取tickets.json顶层tickets数组；从actors.example.json的actors中选可信测试身份，写get_ticket(actor,id)并检查tenant_id。
- [ ] 验收：u-n-viewer能读T-1001、不能读T-2001；未知ID有明确结果。actor来自测试程序，不取自工单正文或用户自报字段。

### D11 闭包：理解filter而不是背写法

iOS3h | 资料：100 Days 单元 9

- [ ] 学：单元9：闭包与函数参数；先写完整形式，再看尾随闭包简写。
- [ ] 做：用filter重写D8循环筛选，比较两种结果；按剩余名额排序只作有余力加分项。
- [ ] 验收：对空数组和边界值两种实现一致；解释闭包接收什么、返回什么，能展开简写。

资料：[100 Days 单元 6](https://www.hackingwithswift.com/100/swiftui/6) · [100 Days 单元 7](https://www.hackingwithswift.com/100/swiftui/7) · [100 Days 单元 8](https://www.hackingwithswift.com/100/swiftui/8) · [Python 第7章：文件与JSON](https://docs.python.org/3/tutorial/inputoutput.html) · [Python 第8章：异常](https://docs.python.org/3/tutorial/errors.html) · [100 Days 单元 9](https://www.hackingwithswift.com/100/swiftui/9)

## 第 2 周每日清单 · 下

180分钟/天；卡住时替换后续任务，不叠加作业。所有复选框初始均未完成。

### D12 Activity 结构体与封装

iOS3h | 资料：100 Days 单元 10、100 Days 单元 11

- [ ] 学：单元10加11：struct、计算属性、访问控制。static做小例子即可；不在此时学架构框架。
- [ ] 做：建立Activity(id,title,capacity,registered)，用计算属性表达剩余名额；把早期零散变量换成三个模型。
- [ ] 验收：改变一个活动不误改另一个；解释哪些属性是存储的、哪些可推导。未学完就拆课顺延。

### D13 pytest 与一次真实失败 + HTTP

Agent2h + 公共1h | 资料：pytest Get Started、MDN HTTP 消息

- [ ] 学：Agent120分钟：pytest首个测试和异常断言。公共60分钟：HTTP请求/响应、方法与状态码，不并行整套网络课程。
- [ ] 做：Agent把D10规则变成测试，故意删除租户检查观察失败后修复。公共用浏览器Network查看一个公开网页请求。
- [ ] 验收：保存测试命令和失败原因；解释浏览器请求与Python函数调用不是同一件事，None也不是HTTP状态码。

### D14 第二周回顾 + 线性查找

iOS1h + 公共2h | 资料：100 Days of SwiftUI 总目录

- [ ] 学：iOS60分钟复习函数和Activity。公共120分钟：90分钟线性查找与集合去重，30分钟表达。
- [ ] 做：手工走一遍ID查找；用已会的Swift循环或Python实现，固定一种面试练习语言，验证头/尾/不存在。
- [ ] 验收：解释查找随n增长的次数；不用背复杂公式。口述本周跨租户测试为什么应该失败。

资料：[100 Days 单元 10](https://www.hackingwithswift.com/100/swiftui/10) · [100 Days 单元 11](https://www.hackingwithswift.com/100/swiftui/11) · [pytest Get Started](https://docs.pytest.org/en/stable/getting-started.html) · [MDN HTTP 消息](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Messages) · [100 Days of SwiftUI 总目录](https://www.hackingwithswift.com/100/swiftui)

## 第 3 周每日清单 · 上

180分钟/天；卡住时替换后续任务，不叠加作业。所有复选框初始均未完成。

### D15 值类型与引用类型

iOS3h | 资料：100 Days 单元 12

- [ ] 学：单元12类与继承；重点是复制struct与共享class实例的区别。
- [ ] 做：用两个变量分别持有struct副本或同一个class实例，修改一个字段，先预测再运行。
- [ ] 验收：保留两个最小实验，能说明为何不应为了“面向对象”把全部模型都改成class。

### D16 协议与扩展：只做小实验

iOS3h | 资料：100 Days 单元 13、Swift 官方语言指南

- [ ] 学：单元13；查协议与扩展对应官方条目。今天不建立网络Repository或多层抽象。
- [ ] 做：给Activity添加一个只读描述能力，写一个小协议与实现；用extension补一个格式化方法。
- [ ] 验收：保留协议要求，删除遵循类型中对应实现，观察不符合协议的编译错误再补回；解释协议承诺的能力与存储数据的区别。

### D17 Agent A0 独立验收

Agent3h | 资料：Python 第8章：异常

- [ ] 学：只回看已学材料；阅读最多20分钟。其余用于独立实现、排错和记录。
- [ ] 做：关闭AI重写get_ticket；追加u-s-viewer、一个新north工单、空列表，保持可信actor来源。
- [ ] 验收：能读写Python、解释JSON/异常并独立通过正常/未知/跨租户变式才过A0；未过则D20/D24继续补。

### D18 Optional 与找不到活动

iOS3h | 资料：100 Days 单元 14

- [ ] 学：单元14：if let、guard let、nil合并；不要用强制解包绕过不确定结果。
- [ ] 做：查询Activity返回可选值，显示“未找到”或标题；比较nil与一个空字符串。
- [ ] 验收：不存在的ID不崩溃；关闭资料讲清Optional包的是什么。

资料：[100 Days 单元 12](https://www.hackingwithswift.com/100/swiftui/12) · [100 Days 单元 13](https://www.hackingwithswift.com/100/swiftui/13) · [Swift 官方语言指南](https://docs.swift.org/latest/documentation/the-swift-programming-language/) · [Python 第8章：异常](https://docs.python.org/3/tutorial/errors.html) · [100 Days 单元 14](https://www.hackingwithswift.com/100/swiftui/14)

## 第 3 周每日清单 · 下

180分钟/天；卡住时替换后续任务，不叠加作业。所有复选框初始均未完成。

### D19 Swift 总复习与独立关卡

iOS3h | 资料：100 Days 单元 15

- [ ] 学：用单元15查漏；先尝试独立题，再看具体不懂的章节，不抄综合答案。
- [ ] 做：45分钟从空文件写Activity、按ID查询、只筛可报名活动；余时定位错误，写边界assert并记录。
- [ ] 验收：语言子关卡：模型/查询/筛选与边界能独立解释。Mac尚未就绪时，只记录语言通过，M0的Xcode构建项仍待验收。

### D20 模块与需求说明 + Git 分支

Agent2h + 公共1h | 资料：Python 第6章：模块、Pro Git：分支的新建与合并

- [ ] 学：Agent120分钟：读import、作为脚本运行。公共60分钟：在自己的练习分支查看差异。
- [ ] 做：Agent分开数据读取、查询逻辑和测试；写半页谁能读什么、成功/错误、当前非目标。公共做一次小分支提交并查看diff。
- [ ] 验收：import模块不意外打印或执行查询；别提前搭复杂架构。不做强制推送或覆盖已有改动。

### D21 第三周回顾 + 栈的最小练习

iOS1h + 公共2h | 资料：100 Days of SwiftUI 总目录

- [ ] 学：iOS60分钟复做最弱语言题。公共120分钟：90分钟数组模拟栈，30分钟讲解故障。
- [ ] 做：用push/pop或append/removeLast的等价操作演示后进先出；尝试括号匹配。不会就只完成栈实验。
- [ ] 验收：空栈处理明确；录2分钟讲一个真实编译/测试错误。若两周同一知识仍卡住，下周减少新课。

资料：[100 Days 单元 15](https://www.hackingwithswift.com/100/swiftui/15) · [Python 第6章：模块](https://docs.python.org/3/tutorial/modules.html) · [Pro Git：分支的新建与合并](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) · [100 Days of SwiftUI 总目录](https://www.hackingwithswift.com/100/swiftui)

## 第 4 周每日清单 · 上

180分钟/天；卡住时替换后续任务，不叠加作业。所有复选框初始均未完成。

### D22 SwiftUI 起步：WeSplit 的组件

iOS3h | 资料：100 Days 单元 16、Swift 官方起步与平台要求

- [ ] 学：Mac就绪：单元16，App、Form、NavigationStack、@State和绑定；单次看10-15分钟就停下复现。
- [ ] 做：Mac就绪：创建课程练习工程，试一个TextField与状态变化；只复制必要工程设置，控件亲手写。
- [ ] 验收：能在模拟器运行，并解释输入如何改变值；若Mac刚到，环境验证可占用整段，不补夜赶课。

Windows替代：仍是Windows：暂缓单元16的UI实施；用Swift模型实现本地报名规则，覆盖正常、满员、重复报名。语言代码可运行不等于iOS工程验收。

### D23 组合 WeSplit，而不是只看视频

iOS3h | 资料：100 Days 单元 17

- [ ] 学：Mac就绪：单元17；先理解输入、派生计算和显示三个部分，再逐段跟做。
- [ ] 做：Mac就绪：完成最小WeSplit，手工改变金额、人数、小费；记录一个键盘或输入问题。
- [ ] 验收：关闭教程重写计算逻辑并给3组预期结果；应用完整跑通才记完成。

Windows替代：仍是Windows：实现报名与取消的纯Swift状态变化；每个操作之后检查容量和唯一性，保留“我的报名”需要的数据，不写无法运行的SwiftUI。

### D24 SQLite 只读查询起步

Agent3h | 资料：Python sqlite3 Tutorial

- [ ] 学：A0已过才读sqlite3 Tutorial的建表、插入、SELECT和占位符，约35分钟。
- [ ] 做：用:memory:数据库建立最小tickets表，导入三条虚构工单；查询条件同时含tenant_id与ticket_id。
- [ ] 验收：解释表/行/列/WHERE；用参数绑定而非拼字符串；north查询不返回south。A0未过则继续D17。

### D25 WeSplit 独立修改与复习

iOS3h | 资料：100 Days 单元 18

- [ ] 学：Mac就绪：单元18复习与挑战；先做课程的一项独立修改，完成后再选下一项。
- [ ] 做：Mac就绪：改变一个计算或展示要求，用自己的测试输入验证；不一边看答案一边修改。
- [ ] 验收：能说明@State为何放这里、派生值为何无需重复保存。没通过继续本课，不急着加MeetLoop UI。

Windows替代：仍是Windows：从空文件重写查询/筛选/报名的一项；故意制造重复ID或满员边界，定位并修复，保存回归断言。

资料：[100 Days 单元 16](https://www.hackingwithswift.com/100/swiftui/16) · [Swift 官方起步与平台要求](https://www.swift.org/getting-started/) · [100 Days 单元 17](https://www.hackingwithswift.com/100/swiftui/17) · [Python sqlite3 Tutorial](https://docs.python.org/3/library/sqlite3.html#tutorial) · [100 Days 单元 18](https://www.hackingwithswift.com/100/swiftui/18)

## 第 4 周每日清单 · 下

180分钟/天；卡住时替换后续任务，不叠加作业。所有复选框初始均未完成。

### D26 把知识迁移到 MeetLoop

iOS3h | 资料：Apple SwiftUI List、100 Days 单元 16

- [ ] 学：Mac且WeSplit关卡通过：查Apple List的最小例子，回看单元16中的ForEach和导航容器。
- [ ] 做：创建MeetLoop最小SwiftUI工程，用已有Activity显示三条列表；先显示标题与剩余名额，详情页作为加分项。
- [ ] 验收：换成空数组、改一个标题都能解释结果；今天不接网络、登录、RN或Go。

Windows替代：仍是Windows：将纯Swift规则整理成可运行示例与5个边界断言；画列表/详情两个草图并标注数据来源。Mac到后从D22开始补UI，不跳过。

### D27 SQL 回归 + 系统基础复述

Agent2h + 公共1h | 资料：Python sqlite3 Tutorial、MDN HTTP 消息

- [ ] 学：Agent120分钟复习参数绑定；公共60分钟复习HTTP与本地函数/数据库的区别。
- [ ] 做：Agent把只读SQL接到查询函数，重跑正常/未知/跨租户测试，加包含引号的非法ID。公共画未来浏览器→API→数据库链路。
- [ ] 验收：非法ID被当数据处理；记录当前只读、无真实认证、无LLM。新增单元测试不代表原12条eval规格已经通过。

### D28 首月验收与下月重排

iOS1h + 公共2h | 资料：100 Days of SwiftUI 总目录

- [ ] 学：iOS60分钟核对语言、环境和UI各自的证据。公共120分钟：90分钟重做最弱编码题，30分钟复盘。
- [ ] 做：列实际学习小时、能独立做的三件事、两个卡点；Mac未到就把UI全部标待做。依据证据安排下一周。
- [ ] 验收：不以看课天数判断完成。52h iOS、20h Agent、12h公共是时段上限；不承诺M0+M1或A0+A1全部做完。

资料：[Apple SwiftUI List](https://developer.apple.com/documentation/swiftui/list) · [100 Days 单元 16](https://www.hackingwithswift.com/100/swiftui/16) · [Python sqlite3 Tutorial](https://docs.python.org/3/library/sqlite3.html#tutorial) · [MDN HTTP 消息](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Messages) · [100 Days of SwiftUI 总目录](https://www.hackingwithswift.com/100/swiftui)

## 卡住、提前完成与下一阶段

按证据调整；首次日程用于测量真实速度

### 卡住如何处理

- 单一问题尝试15-20分钟：缩成最小例子，记录预期、实际与错误，再向AI要一条提示或排错路径。
- 同一课未过关：下一iOS/Agent时段替换为补做，后面的该主线任务整体顺延；不靠周末额外加时补齐。
- 同一基础连续两周卡住：减少功能、拆小练习，并修订长期工时估计。M0的10-15h等只是初估，不能为了符合数字跳关。
- 如果已掌握：先独立做当天变式，解释错误与边界，全部通过后把课程时间用于下一个同主线任务；不凭“看着熟悉”快进。

### 第28天的合理成果

Swift语言的可运行练习与独立变式；Mac可用且进度顺利时，WeSplit独立改题及MeetLoop静态列表雏形。Agent约20h时段只争取A0通过与A1只读SQL起步，不能宣称完整Agent后端或12条eval通过。

### 之后按这个顺序继续

iOS：未完成的单元16-18 → 单元19独立小挑战 → 20-22按钮/弹窗/状态 → MeetLoop列表、详情、报名、取消与我的报名。遇到状态难点才引入Stanford片段；M1通过后进M2网络与排错，再到M3 UIKit。RN在M4/M5。

Agent：A0不足先补 → A1完成只读数据、HTTP、SQL与测试 → A2再接LLM与小harness → 后续检索、控制台、审批、沙箱、恢复与评测。教程数量不是目标。

资料：[100 Days 单元 19](https://www.hackingwithswift.com/100/swiftui/19) · [100 Days 单元 20](https://www.hackingwithswift.com/100/swiftui/20) · [100 Days 单元 21](https://www.hackingwithswift.com/100/swiftui/21) · [100 Days 单元 22](https://www.hackingwithswift.com/100/swiftui/22) · [Stanford CS193p 2025](https://cs193p.stanford.edu/)

## 每天收尾：只记能证明的进步

练习自己写；本清单没有提前实现应用或代做课程作业

### 最小学习日志

日期 / D编号：
占用分钟 / 有效分钟：
课程章节（只写今天真正看的）：
自己完成的改动：
运行命令或设备 + 预期/实际：
一个错误、定位与修复：
关掉AI后的变式是否通过：
代码路径或commit：
下次先补什么：

### 怎么使用AI

可以这样问：“我在做D09。预期是……，实际是……，我试过……。先指出一个可能的原因或给一个反例，不给完整实现。” 得到提示后自己改，再请AI检查边界。代码能跑但你说不清，仍记待复习。

### 文件怎么放

MeetLoop练习可逐步放在exercises/swift/dayNN.swift，课程App可用exercises/WeSplit；真正项目再放apps/ios。Agent练习在自己的仓库exercises/python，测试放tests。只在真正写代码时创建目录，不预建空壳；两仓库不互相依赖。

两个仓库各带一份相同日程，方便迁移到Mac，但只记一份自己的学习日志，不能把两份清单的时间相加。勾选状态保存在Markdown或个人笔记，HTML/PDF供阅读和打印。

> 今天完成标准很小：你能独立写出并运行活动信息，改三组输入，解释let/var与一个错误。达到这里就可以收工，不需要今天开始“做完整项目”。
