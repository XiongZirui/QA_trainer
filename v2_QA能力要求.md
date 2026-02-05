## **A5（初级工程师）**

### A5（初级工程师）能力要求汇总
  - skill_level: A5
  - position: 初级工程师
  - role: 入门执行者
  - focus_areas: [概念理解, 工具认知, 规范学习]
  - key_skills: 
    - 理解功能测试基本术语和测试类型（功能测试、冒烟测试、I-Test、SIT、UAT等）
    - 理解缺陷基本定义
    - 了解Swagger文件需符合OpenAPI规范
    - 了解Postman、SQL别名规范、UI/接口自动化概念、Requests库等工具的基本定位
  - prerequisites: 无
  - related_documents: [ai辅助代码目录结构.md, Function Testing Work Process_Capgemini_V1.md, JTP_Postman.md]
  - keywords: [OpenAPI, Swagger, 功能测试, 冒烟测试, I-Test, SIT, UAT, 缺陷定义, Postman, SQL别名, UI自动化, 接口自动化, Requests]

### A5 **块 1.1：基础概念与术语认知**

**技能类别：基础工具与流程理解**

**检索关键词**: `功能测试术语`, `测试类型`, `缺陷定义`, `软件缺陷`, `冒烟测试`, `I-Test`, `回归测试`, `OpenAPI规范`

#### **特定能力详情**

- **AI辅助代码目录结构**
  - [规范认知] Swagger 文件必须符合 OpenAPI 规范

- **Function Testing Work Process**
  - [术语认知] 功能测试基本术语定义：功能测试、冒烟测试、Feature test(I-Test)、SIT、UAT、Rehearsal test、Go-live test、回归测试
  - [概念认知] 缺陷基本定义：软件缺陷是指破坏正常运行能力的问题、错误或隐藏的功能缺陷

**分块说明**: 此块集中了A5工程师必须理解的测试核心概念和行业术语，是后续所有技能的基础。

### A5 **块 1.2：工具与框架初步了解**

**检索关键词**: `Postman`, `SQL规范`, `UI自动化概念`, `接口自动化概念`, `Requests库`, `表别名`

#### **特定能力详情**

- **Postman**
  - [工具认知] Postman 可以发送几乎所有类型的 HTTP 请求，适用于不同操作系统

- **SQL**
  - [规范认知] SQL 中表的别名命名规范：最好不使用中文，不推荐 t1、t2，建议使用表名简写

- **Python**
  - [概念认知] UI 自动化测试是一种通过编写脚本或使用自动化测试工具，对用户界面进行自动化测试的方法（pythonUI自动化）
  - [概念认知] 接口自动化是提高测试效率和质量的重要手段之一（python接口自动化）
  - [工具认知] Requests 是基于 urllib 的 HTTP 库（python接口自动化）

**分块说明**: 此块介绍了测试工作中将接触到的关键工具和框架的基本定位与核心价值，帮助新员工建立技术全景图。

---
## **B1（工程师）**

### B1（工程师）能力要求汇总
  - skill_level: B1
  - position: 工程师
  - role: 独立执行者
  - focus_areas: [测试执行, 环境搭建, 基础脚本]
  - key_skills:
    - 能使用common.py中的基础函数解析Swagger文件并生成目录结构
    - 了解功能测试前置条件和启动检查内容
    - 能安装JMeter环境并创建基本测试元素（线程组、HTTP请求等）
    - 能使用Postman发送请求、设置变量
    - 了解SQL连接类型和NULL值处理
    - 能搭建Python+Selenium环境并执行基础操作
    - 了解接口测试流程，能使用requests.get()发送请求
  - prerequisites: 掌握A5全部内容
  - related_documents: [ai辅助代码目录结构.md, Function Testing Work Process_Capgemini_V1.md, JTP_jmeter.md, JTP_Postman.md, JTP_SQL基础入门文档.md, pythonUI自动化.md, python接口自动化.md]
  - keywords: [common.py, obtain_file_json.py, 前置条件, 启动检查, JMeter安装, 线程组, HTTP请求, Postman变量, SQL连接, NULL值, Selenium环境, requests.get]

### B1 **块 2.1：测试执行与基础操作**

**技能类别：测试执行与基础自动化**

**检索关键词**: `common.py函数`, `obtain_file_json.py`, `测试前置条件`, `测试启动检查`, `JMeter安装`, `JMeter线程组`, `Postman变量`, `SQL连接类型`, `NULL值处理`

#### **特定能力详情**

- **AI辅助代码目录结构**
  - [工具使用] 能使用 common.py 中的基础函数：load_swagger_file, extract_data, replace_key_values, replace_slash_with_dot, find_value_by_key, check_and_create_directory, remove_key, extract_description_keys, get_str
  - [工具使用] 能运行 execute 层的 obtain_file_json.py 文件，通过 create_subdirectories_from_dict_keys、get_any_datas、process_dict、get_json_pointer、generate_feature 等方法解析 Swagger 文件并生成目录结构

- **Function Testing Work Process**
  - [流程认知] 了解功能测试前置条件：需求文档评审通过、开发自测用例通过率100%
  - [流程认知] 了解测试启动检查包括检查测试环境与数据是否可用

- **Apache JMeter**
  - [工具认知] 了解 JMeter 是一款纯 Java 的开发测试工具，用于服务器压力测试和功能/回归测试
  - [环境搭建] 能安装 JMeter 环境：下载 JDK、JMeter、插件管理器
  - [工具操作] 能在 JMeter 中创建测试计划、线程组（setUp Thread Group, Thread Group, tearDown Thread Group）、HTTP 请求用例、结果断言（如 JSON Assertion）、查看 View Results Tree 和聚合报告

- **Postman**
  - [工具操作] 能使用 Postman 发送 GET/POST 请求，查看响应状态码和 body，使用 History 记录
  - [工具操作] 能在 Postman 中设置变量（Global 全局变量、Environment 环境变量），使用 {{变量名}} 引用

- **SQL**
  - [知识认知] 了解 SQL 连接类型选择原则：内连接、左连接、右连接
  - [知识认知] 了解 SQL 中 NULL 值处理注意事项，例如在运算中（工资+奖金）需观察字段是否存在 NULL

**分块说明**: 此块聚焦于具体测试活动的执行和各类工具的基础操作能力，是独立承担测试任务的关键。

### B1 **块 2.2：自动化环境搭建与脚本基础**

**检索关键词**: `UI自动化步骤`, `Selenium环境搭建`, `Selenium基础操作`, `接口测试流程`, `requests.get`

#### **特定能力详情**

- **Python**
  - [流程认知] 了解 UI 自动化测试步骤：环境设置、测试脚本编写、测试数据准备、测试脚本执行、结果分析和报告生成
  - [环境搭建] 能搭建 Python+Selenium 环境：安装 Python、pycharm、Selenium、Chrome 浏览器、ChromeDriver
  - [工具操作] 能使用 Selenium 初始化浏览器对象、访问页面、设置浏览器大小、前进后退、获取页面基础属性（title, current_url, name, page_source）
  - [流程认知] 了解接口测试流程：发起请求、获取响应、解析内容、内容断言
  - [工具操作] 能使用 requests.get() 发送不带参数和带参数（params）的 GET 请求

**分块说明**: 此块是自动化测试的起点，涵盖了环境准备和编写第一个简单脚本所需的全部技能。

---
## **B2（中级工程师）**

### B2（中级工程师）能力要求汇总
  - skill_level: B2
  - position: 中级工程师
  - role: 熟练执行者
  - focus_areas: [测试执行熟练, 工具进阶, 脚本编写]
  - key_skills:
    - 能使用命令行执行JMeter脚本并生成报告
    - 能使用Newman命令行执行Postman Collection
    - 了解JMeter聚合报告指标含义
    - 能处理接口参数关联和加密接口（如MD5签名）
    - 了解YAML语法并能编写数据驱动测试用例
    - 能在Postman中编写断言、实现鉴权、使用Pre-request Script和参数化测试
    - 能将Postman Collection导出为其他语言脚本
  - prerequisites: 掌握B1全部内容
  - related_documents: [JTP_jmeter.md, JTP_Postman.md, python接口自动化.md]
  - keywords: [JMeter命令行, Newman, 聚合报告, Postman断言, Postman鉴权, Pre-request Script, 参数关联, 加密接口, MD5, YAML语法, 数据驱动]

### B2 **块 3.1：持续集成与命令行工具**

**技能类别：持续集成与复杂场景测试**

**检索关键词**: `JMeter命令行`, `Newman`, `nodejs`, `cnpm`, `聚合报告指标`

#### **特定能力详情**

- **Apache JMeter, Postman (命令行执行与集成)**
  - [工具操作] 能使用命令行执行 JMeter 脚本并生成测试报告：`jmeter -n -t ./xxx/name.jmx -l ./xxx/name.jtl -e -o ./xxx/name/reports`
  - [工具操作] 能使用 Newman 命令行执行 Postman Collection：`newman run v2ex.postman_collection.json -d test.json -r html,cli,json,junit`
  - [工具认知] 了解 Newman 是命令行的 postman 接口集运行器，安装需依赖 nodejs 和 cnpm

- **Apache JMeter (性能测试进阶)**
  - [知识认知] 了解 JMeter 聚合报告中的各项数据：Label, Samples, Average, Median, 90%Line, Min, Max, Error%, Throughput, KB/Sec

**分块说明**: 此块将测试执行从GUI界面推进到命令行和持续集成环境，是实现自动化流水线和CI/CD的关键步骤。

### B2 **块 3.2：复杂接口测试与数据驱动**

**检索关键词**: `接口参数关联`, `token传递`, `加密接口`, `MD5签名`, `YAML数据结构`, `YAML语法`, `数据驱动测试`

#### **特定能力详情**

- **Python接口自动化 (复杂接口测试)**
  - [场景处理] 能处理接口参数关联请求，例如登录后获取 token 并在后续请求头中使用
  - [场景处理] 能处理加密接口请求，例如使用 hashlib 进行 MD5 签名
  - [知识认知] 了解 YAML 是一种数据标记语言，支持对象、数组、纯量三种数据结构
  - [知识认知] 了解 YAML 基本语法：大小写敏感、使用缩进表示层级、缩进不允许使用 Tab、# 表示注释
  - [工具操作] 能编写 YAML 格式的测试用例数据，用于数据驱动测试

**分块说明**: 此块专注于解决实际测试中的复杂场景，如状态保持、安全验证，并引入YAML实现测试数据与代码的分离。

### B2 **块 3.3：高级工具特性应用**

**检索关键词**: `Postman Tests断言`, `Postman Cookies`, `Postman鉴权`, `Pre-request Script`, `Collection参数化`, `脚本导出`

#### **特定能力详情**

- **Postman 进阶**
  - [工具操作] 能在 Postman 的 Tests 中编写断言脚本，检查响应 body、headers、状态码、响应时间等
  - [工具操作] 能在 Postman 中获取 cookies 并在下一个 API 中应用
  - [工具操作] 能在 Postman 中实现鉴权：Basic Auth、在 headers 中添加 token、将 token 添加到环境变量
  - [工具操作] 能使用 Postman 的 Pre-request Script 在请求发送前执行代码，例如生成随机数、处理身份证号判断性别
  - [工具操作] 能运行 Postman Collection，进行参数化（数据驱动）测试
  - [工具操作] 能将 Postman Collection 导出为其他脚本语言（如 Python）并运行

**分块说明**: 此块深度挖掘Postman等工具的高级功能，实现更强大、灵活和可维护的接口测试。

---
## **C1（高级工程师）**

### C1（高级工程师）能力要求汇总
  - skill_level: C1
  - position: 高级工程师
  - role: 框架使用者
  - focus_areas: [pytest框架, 接口自动化框架, UI自动化进阶, 测试用例设计]
  - key_skills:
    - 全面掌握pytest框架：安装、配置、执行方式、插件、前后置、参数化、断言等
    - 能搭建基于Python+requests+pytest+yaml+allure的接口自动化框架
    - 能使用requests.post()发送POST请求并获取响应内容
    - 能使用Selenium进行元素定位、鼠标键盘操作，了解等待机制
    - 能编写完整测试用例，了解测试用例设计原则和4-eyes-principle
  - prerequisites: 掌握B2全部内容
  - related_documents: [pytest框架.md, python接口自动化.md, pythonUI自动化.md, Function Testing Work Process_Capgemini_V1.md]
  - keywords: [pytest, pytest插件, pytest.ini, @pytest.mark, fixture, 参数化, assert, requests.post, YAML, find_element, ActionChains, Keys, 测试用例设计原则]

### C1 **块 4.1：Pytest 框架深度应用**

**技能类别：自动化框架与中级测试能力**

**检索关键词**: `pytest框架`, `pytest插件`, `pytest执行方式`, `pytest.ini`, `用例执行顺序`, `跳过用例`, `前后置fixture`, `参数化`, `断言assert`

#### **特定能力详情**

- **Python (pytest 框架应用)**
  - [框架认知] 了解 pytest 是基于 Python 的单元测试框架，比 unittest 更灵活
  - [框架认知] 了解 pytest 可以与 selenium, requests, appium 实现 web, 接口, app 自动化
  - [框架认知] 了解 pytest 强大的插件：pytest-html, pytest-xdist, pytest-ordering, pytest-rerunfailures, pytest-base-url, allure-pytest
  - [环境搭建] 能通过 requirements.txt 文件安装 pytest 及其插件
  - [规则认知] 了解 pytest 默认测试用例发现规则：模块名以 test_ 开头或 _test 结尾；测试类以 Test 开头且不能有 __init__ 方法；测试方法以 test 开头
  - [工具操作] 能使用主函数模式（pytest.main()）和命令行模式执行 pytest 测试用例
  - [知识认知] 了解 pytest 命令行参数：-s, -v, -vs, -n, --rerun, -x, --maxfail, -k
  - [配置操作] 能配置 pytest.ini 文件改变 pytest 默认行为
  - [工具操作] 能使用 @pytest.mark.run(order=1) 改变测试用例执行顺序
  - [工具操作] 能使用 @pytest.mark.skip 和 @pytest.mark.skipif 跳过测试用例
  - [工具操作] 能使用 setup/teardown, setup_class/teardown_class 实现用例前后置
  - [工具操作] 能使用 @pytest.fixture() 装饰器实现用例前后置，了解其参数：scope, params, autouse, ids, name
  - [工具操作] 能使用 @pytest.mark.parametrize 实现参数化
  - [工具操作] 能使用 assert 进行断言

**分块说明**: 此块是Python自动化测试的核心，全面掌握pytest框架的使用是搭建可靠自动化测试套件的基础。

### C1 **块 4.2：接口自动化框架搭建**

**检索关键词**: `接口自动化框架结构`, `requests.post`, `响应内容获取`, `common层`, `data层`, `YAML`

#### **特定能力详情**

- **Python (接口自动化框架搭建)**
  - [环境搭建] 能通过 requirements.txt 安装接口自动化所需插件：pytest, requests, pytest-html, pytest-xdist, pytest-ordering, pytest-rerunfailures, pytest-base-url, allure-pytest
  - [框架认知] 了解基于 Python+requests+pytest+yaml+allure 的接口自动化框架结构：common层, data层, logs层, reports层, temps层, testcase层, pytest.ini, requirements.txt, run.py
  - [工具操作] 能使用 requests.post() 发送 data 表单数据和 json 数据的 POST 请求
  - [工具操作] 能获取响应内容：status_code, url, encoding, headers, cookies, text, content, json()

**分块说明**: 此块从使用单个请求库升级到理解和搭建完整的接口自动化测试框架，是工程化测试的开始。

### C1 **块 4.3：UI自动化进阶与测试用例设计**

**检索关键词**: `Selenium元素定位`, `ActionChains鼠标操作`, `Keys键盘操作`, `等待机制`, `测试用例设计原则`, `4-eyes-principle`

#### **特定能力详情**

- **Python (UI 自动化进阶)**
  - [工具操作] 能使用 Selenium 的 find_element 方法通过不同属性定位元素：CLASS, XPATH, LINK_TEXT, PARTIAL_LINK_TEXT, TAG, CSS, ID
  - [工具操作] 能使用 ActionChains 模拟鼠标操作：右击(context_click)、双击(double_click)、拖拽(drag_and_drop)、悬停(move_to_element)
  - [工具操作] 能使用 Keys 类模拟键盘操作：删除键、空格键、制表键、回退键、回车、全选、复制、剪切、粘贴、F1 等
  - [知识认知] 了解 Selenium 三种等待方式：强制等待（time.sleep）、隐式等待（implicitly_wait）、显式等待

- **Function Testing Work Process (测试用例设计)**
  - [工作产出] 能编写测试用例，包含测试功能点、测试条件、测试步骤、输入值、预期结果、优先级、严重程度等要素
  - [原则认知] 了解测试用例设计原则：用例摘要简短独特；每个用例涉及一个或多个需求；定义必要先决条件；包含预期结果；测试步骤清晰易懂（5+/-2步，不超过10步）；明确测试目标；进行优先级排序；回归用例标记“回归相关”；基于 4-eyes-principle 保证质量

**分块说明**: 此块结合了UI自动化的高级交互技巧和测试设计的核心方法论，是保证测试有效性和自动化脚本健壮性的关键。

---
## **C2（资深工程师）**

### C2（资深工程师）能力要求汇总
  - skill_level: C2
  - position: 资深工程师
  - role: 策略制定者
  - focus_areas: [框架优化, 测试策略, 测试管理, SQL进阶, 流程管理, 缺陷管理, 测试报告, 自动化价值分析, 质量保障体系, 上线后支持, 高级测试技术, AI辅助测试]
  - key_skills:
    - 了解AI辅助框架原理并能操作
    - 能制定测试计划、测试策略和风险评估
    - 能组织测试用例评审和执行全流程测试活动（冒烟、I-Test、SIT、UAT等）
    - 了解SQL进阶知识（主键、GROUP BY等）
    - 能制定并优化功能测试流程，管理缺陷全生命周期
    - 能发送Test Report并组织复盘总结
    - 理解UI/接口自动化价值与局限性
    - 能制定测试中止/出口准则，组织上线后支持（Hypercare）
    - 了解Allure报告、Selenium分布式特性等高级测试技术
  - prerequisites: 掌握C1全部内容
  - related_documents: [ai辅助代码目录结构.md, ai辅助操作手册.md, Function Testing Work Process_Capgemini_V1.md, JTP_SQL基础入门文档.md, pytest框架.md, pythonUI自动化.md, python接口自动化.md]
  - keywords: [$ref嵌套, AI辅助框架, 测试计划, 测试策略, 风险评估, 用例评审, 冒烟测试执行, I-Test, SIT, UAT, 主键, GROUP BY, 功能测试流程优化, 缺陷严重程度, 缺陷优先级, 缺陷状态, 引入阶段, 解决时效, 缺陷流转, Test Report, 复盘总结, UI自动化优缺点, 接口自动化价值, 测试中止准则, 测试出口准则, 需求覆盖率, 缺陷修复率, Hypercare, RootCause分析, Allure报告, Selenium特点, AI辅助框架结构]

### C2 **块 5.1：框架扩展与测试策略制定**

**技能类别：框架优化与测试策略设计**

**检索关键词**: `$ref嵌套解析`, `AI辅助框架步骤`, `测试计划制定`, `测试策略`, `风险评估`, `冒烟测试失败`, `提测延误`, `缺陷阻塞`

#### **特定能力详情**

- **AI辅助代码目录结构, AI辅助操作手册 (框架扩展与维护)**
  - [原理认知] 了解 obtain_file_json.py 中的 process_dict 方法支持解析 "$ref" 最多三层嵌套，后续可能优化
  - [工具认知] 了解 extract_filename.py 和 output_promt.py 在新版中未使用
  - [工具认知] 了解 run.py 用于执行对应方法
  - [流程认知] 了解 AI 辅助代码框架的操作步骤：准备 OpenAPI 规范文件、设置文件路径、运行 run.py、通过 AI 识别 prompt 生成 karate 测试用例、手工填写参数执行用例

- **Function Testing Work Process (测试策略制定)**
  - [工作产出] 能制定测试计划，确定测试策略（I-Test, UAT 等；功能、性能、安全、自动化等类型）、预估测试工作量、输出测试时间线
  - [风险管理] 能预估测试风险并提出应对措施：
    - 冒烟测试未通过：开发自测用例通过率100%，开发进行结卡演示并达成三方一致（DEV&BA&QA）
    - 开发提测延误：开发严格控制进度，如有风险立即通知，测试管理人员评估风险，必要时申请修改测试计划
    - 严重或高级别缺陷阻塞测试：开发优先解决，测试管理人员调整用例执行策略，将问题升级到项目组

**分块说明**: 此块从技术实现延伸到流程与策略，要求工程师不仅能使用框架，还能理解其原理、局限性，并能规划和管理整个测试活动。

### C2 **块 5.2：全流程测试执行与管理**

**检索关键词**: `测试用例评审`, `冒烟测试执行`, `I-Test执行`, `SIT执行`, `UAT执行`, `Rehearsal test`, `Go-live test`, `回归测试场景`

#### **特定能力详情**

- **Function Testing Work Process_Capgemini (测试执行与管理)**
  - [流程管理] 能组织测试用例评审，开发人员和产品经理需参与，明确测试范围及冒烟测试用例范围
  - [测试执行] 能执行冒烟测试：快速验证提测版本的基本功能、主要场景和主要流程
  - [测试执行] 能执行 Feature test(I-Test)：在测试环境对新增或修改功能进行功能测试，侧重 feature team 内部交互
  - [测试执行] 能执行 SIT：验证与其他系统的三方交互功能
  - [测试执行] 能执行 UAT：由关键用户(KU)执行，测试人员或 KU 准备用例并共同评审（开发&测试&BA&KU），需确认问题是缺陷还是需求变更
  - [测试执行] 能执行 Rehearsal test：系统上线前由测试人员对待上线功能进行验证
  - [测试执行] 能执行 Go-live test：系统上线后由测试人员或 KU 对上线功能进行验证
  - [测试执行] 能执行回归测试：应用于四个场景：验证缺陷修复效果、检查新功能对旧功能的影响、关键节点验证系统稳定性、上线前主功能流程回归确认

**分块说明**: 此块定义了软件开发生命周期中不同阶段测试活动的具体职责和执行要点，是资深工程师必须熟练掌握的完整测试流程。

### C2 **块 5.3：SQL 进阶与数据库知识**

**检索关键词**: `主键必要性`, `数据唯一性`, `索引`, `GROUP BY规范`, `分组字段`, `聚合函数`

#### **特定能力详情**

- **SQL 进阶**
  - [原理认知] 了解主键设置的必要性：保证数据唯一性、快速查找和索引、保证数据完整性、数据库优化
  - [原理认知] 了解 GROUP BY 使用规范：选择正确的分组字段、考虑数据准确性和完整性、注意聚合函数的使用、理解 GROUP BY 的含义

**分块说明**: 此块深化了数据库相关的测试支持技能，理解数据层的基本原理有助于设计更有效的数据验证用例。

### C2 **块 5.4：测试流程管理与缺陷全生命周期**

**技能类别：测试管理与流程改进**

**检索关键词**: `功能测试流程优化`, `缺陷严重程度定义`, `缺陷优先级定义`, `缺陷状态流转`, `缺陷引入阶段`, `缺陷解决时效`, `Hotfix流程`

#### **特定能力详情**

- **Function Testing Work Process (测试流程管理)**
  - [流程优化] 能制定并优化功能测试流程，实现组织内统一，提升整体测试效率
  - [缺陷管理] 能管理缺陷全流程：缺陷严重程度（Critical, High, Medium, Low）、优先级（Critical, High, Medium, Low）、缺陷状态（New, In progress, In test, Resolved, Closed）、引入阶段（I-Test, UAT, Release, Prod）、解决时效（Critical/High:24h, Medium:48h, Low:72h）、缺陷流转流程（常规迭代和 Hotfix）

**分块说明**: 此块是测试管理的核心，涵盖了从流程设计到缺陷闭环的完整管理体系，是专家级工程师驱动质量改进的基础。

### C2 **块 5.5：测试总结、报告与自动化深入理解**

**检索关键词**: `Test Report`, `复盘总结`, `UI自动化优点`, `UI自动化挑战`, `接口自动化分类`, `接口自动化性价比`

#### **特定能力详情**

- **Function Testing Work Process (测试总结与报告)**
  - [工作产出] 能在测试过程中每天发送 Test Report，同步测试进度、质量和风险预警
  - [流程活动] 能在迭代结束或项目上线后组织复盘总结，内容包括沟通与协作、各类流程、需求&开发&测试质量等

- **Python (UI/接口自动化深入)**
  - [价值认知] 了解 UI 自动化测试的优点：提高测试效率、覆盖率、一致性、软件质量
  - [局限认知] 了解 UI 自动化测试的限制和挑战：需要维护成本、可靠性和稳定性依赖环境、难以处理动态内容、无法完全替代人工测试、初始投入较大
  - [概念认知] 了解接口自动化两大类：为模拟测试数据而开展、在功能测试之前提前发现错误而开展
  - [价值认知] 了解为什么要做接口自动化：相对于 UI 自动化，接口变更频率低，自动化性价比高

**分块说明**: 此块融合了沟通报告软技能和对自动化测试战略价值的深度思考，帮助专家级工程师权衡利弊，做出正确的技术决策。

### C2 **块 5.6：质量保障体系与上线支持**

**技能类别：全流程质量保障与技术创新**

**检索关键词**: `测试中止准则`, `测试出口准则`, `需求覆盖率100%`, `缺陷修复率`, `Critical/High缺陷遗留`, `Hypercare`, `hotfix`, `RootCause分析`

#### **特定能力详情**

- **Function Testing Work Process (质量保障体系构建)**
  - [标准制定] 能制定测试中止准则：冒烟测试未通过（通过率未达到100%）、需求不明确或未达成一致
  - [标准制定] 能制定测试出口准则：
    - 测试用例对需求的覆盖率达到100%
    - 测试用例执行率达到100%
    - 测试用例通过率>=95%
    - 所有发现的缺陷均被记录并跟踪
    - 缺陷修复率>=95%
    - 没有遗留 Critical 和 High 级别的缺陷
    - 遗留的 Medium & Low 缺陷<=5%
  - [工作产出] 能明确测试输出物：《Test plan》、《Test case》、《Test case review record》、《Functional test report》

- **Function Testing Work Process (上线后支持与质量改进)**
  - [流程管理] 能组织上线后支持（Hypercare）：验证生产缺陷、由开发修复、测试通过后进入 hotfix 上线流程
  - [质量改进] 能在 Hypercare 阶段收集、整理、分类问题（非错、操作不当、数据问题、缺陷等）并进行 RootCause 分析，提出应对策略以改善测试过程、提升测试质量

**分块说明**: 此块定义了质量保障的终极标准和持续改进机制，是首席工程师构建和守护组织质量文化的关键。

### C2 **块 5.7：高级测试技术与AI辅助测试**

**检索关键词**: `Allure报告`, `Jenkins集成`, `Selenium特点`, `分布式测试`, `AI辅助框架`, `execut层`, `swagger层`

#### **特定能力详情**

- **Python, Pytest (测试技术深入)**
  - [工具认知] 了解 Allure 是一个轻量级、灵活的、支持多语言的测试报告工具，能提供详尽的测试报告、测试步骤、Log 等信息，可以集成到 Jenkins
  - [环境搭建] 能安装 Allure：下载并配置环境变量（pytest）
  - [框架认知] 了解 Selenium 是最广泛使用的开源 Web UI 自动化测试套件之一，支持多语言、多平台、多浏览器
  - [框架认知] 了解 Selenium 特点：免费开源、支持多平台、多浏览器、多语言、支持分布式执行测试用例

- **AI辅助操作手册 (AI 辅助测试)**
  - [框架认知] 了解 AI 辅助代码生成框架的整体结构：execut层、swagger层、common.py、run.py
  - [目标认知] 了解该框架用于提取编写接口用例信息的框架进行 API 测试

**分块说明**: 此块关注测试技术的前沿发展和与AI等新技术的结合，体现了首席工程师在技术选型、架构规划和创新引领方面的职责。