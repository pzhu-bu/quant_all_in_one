---
title: "量化研究与量化交易：Python + C++ 落地学习路线"
subtitle: "从理论回顾到基础复现、经典论文复现、框架落地与毕业项目"
date: "2026-06-20"
tags: [quant-research, quant-trading, python, cpp, coquette]
theme: "blush-pink coquette"
---

<style>
:root {
  --blush-0: #fff7fa;
  --blush-1: #fff0f5;
  --blush-2: #f9d7e3;
  --blush-3: #efb5c8;
  --rose: #d86f95;
  --rose-deep: #9f4264;
  --ink: #4b3941;
  --muted: #7c6570;
  --line: rgba(216, 111, 149, .28);
}
body {
  background:
    radial-gradient(circle at 16px 16px, rgba(239,181,200,.18) 1.5px, transparent 1.7px),
    linear-gradient(180deg, var(--blush-0), #ffffff 36%, var(--blush-1));
  background-size: 28px 28px, auto;
  color: var(--ink);
  font-family: "Noto Serif SC", "Source Han Serif SC", "Songti SC", Georgia, serif;
  line-height: 1.78;
  letter-spacing: .01em;
}
.markdown-body, body > * {
  max-width: 1080px;
  margin-left: auto;
  margin-right: auto;
}
.hero {
  margin: 2.2rem auto 2rem;
  padding: 2.4rem 2.6rem;
  border: 1px solid var(--line);
  border-radius: 28px;
  background: linear-gradient(135deg, rgba(255,255,255,.94), rgba(255,240,245,.92));
  box-shadow: 0 18px 50px rgba(159,66,100,.12);
  position: relative;
  overflow: hidden;
}
.hero:before {
  content: "୨୧";
  position: absolute;
  right: 2rem;
  top: 1.2rem;
  color: rgba(216,111,149,.26);
  font-size: 5rem;
  line-height: 1;
}
.hero-kicker {
  color: var(--rose-deep);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .18em;
  font-size: .78rem;
}
.hero h1 {
  margin: .4rem 0 .6rem;
  color: var(--rose-deep);
  font-size: 2.15rem;
  line-height: 1.25;
  border: 0;
}
.hero p { color: var(--muted); margin: .25rem 0; }
.meta-card {
  margin: 1rem 0 0;
  padding: .9rem 1rem;
  border-radius: 18px;
  background: rgba(255,255,255,.68);
  border: 1px dashed var(--blush-3);
}
.ribbon-note {
  padding: .95rem 1.1rem;
  border-left: 5px solid var(--rose);
  background: rgba(255,240,245,.7);
  border-radius: 14px;
  color: var(--muted);
}
h1, h2, h3 {
  color: var(--rose-deep);
  font-family: "Noto Serif SC", "Source Han Serif SC", "Songti SC", Georgia, serif;
}
h1 {
  margin-top: 2.4rem;
  padding-bottom: .45rem;
  border-bottom: 1px solid var(--line);
}
h2 {
  margin-top: 1.8rem;
  padding-left: .6rem;
  border-left: 5px solid var(--blush-3);
}
h3 { margin-top: 1.4rem; }
.lace-break {
  text-align: center;
  color: var(--rose);
  opacity: .72;
  margin: 2.1rem auto 1.2rem;
  letter-spacing: .12em;
}
blockquote {
  margin: 1.1rem 0;
  padding: 1rem 1.15rem;
  border-left: 5px solid var(--blush-3);
  background: rgba(255,247,250,.82);
  border-radius: 14px;
  color: var(--muted);
}
code {
  background: #ffe8f0;
  color: #7d3150;
  padding: .12em .32em;
  border-radius: .42em;
}
pre {
  padding: 1.1rem 1.2rem;
  overflow: auto;
  border-radius: 18px;
  border: 1px solid var(--line);
  background: linear-gradient(180deg, #fffafd, #fff4f8);
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.7);
}
pre code { background: transparent; padding: 0; color: inherit; }
table {
  display: block;
  width: 100%;
  overflow-x: auto;
  margin: 1rem 0 1.3rem;
  border-collapse: collapse;
  border: 1px solid var(--line);
  border-radius: 18px;
  background: rgba(255,255,255,.86);
  box-shadow: 0 10px 30px rgba(159,66,100,.07);
}
th {
  background: linear-gradient(180deg, #ffe9f1, #f8ccd9);
  color: var(--rose-deep);
  font-weight: 700;
}
th, td {
  padding: .72rem .86rem;
  border: 1px solid rgba(216,111,149,.18);
  vertical-align: top;
}
tr:nth-child(even) td { background: rgba(255,247,250,.72); }
ul li::marker, ol li::marker { color: var(--rose); }
a { color: var(--rose-deep); text-decoration-color: var(--blush-3); }
hr { border: 0; border-top: 1px dashed var(--blush-3); margin: 2rem 0; }
</style>

<div class="hero">
  <div class="hero-kicker">Blush Quant Roadmap · Python × C++</div>
  <h1>量化研究与量化交易 · Python + C++ 落地学习路线</h1>
  <p><strong>从理论回顾到基础复现、经典论文复现、框架落地与毕业项目</strong></p>
  <div class="meta-card">版本：2026-06-20<br>定位：偏工程落地，不是纯理论教材<br>使用方式：按模块复现、按阶段交付、按报告验收</div>
</div>

<div class="ribbon-note">🎀 <strong>阅读定位</strong>：这是一份偏工程落地的学习路线，强调框架选型、复现路径、交付物与验收标准。淡粉色 coquette 视觉元素用于提升长文档的阅读愉悦感，不改变专业内容的严肃性。</div>

> **免责声明**：本文档仅用于学习与研究，不构成投资建议、交易建议或任何收益承诺。

# 目录

- 1. 学习目标与总体方法

- 2. 最小理论回顾：只保留落地必需的概念

- 3. Python/C++ 工程栈与代码仓库结构

- 4. 模块化落地路线：因子、预测、回测、优化、风险、衍生品、固收、信用、加密

- 5. 36 周执行计划与每阶段交付物

- 6. 经典论文复现清单

- 7. 书、论文、官方文档与数据资源

- 8. 质量控制清单与毕业项目

<div class="lace-break">⋆ ˚｡⋆୨୧˚ ⋆｡˚ ⋆</div>

# 🎀 1. 学习目标与总体方法

目标不是“读懂所有理论”，而是形成一个能持续扩展的量化研究与交易工程体系：数据可追溯，研究可复现，模型可验证，组合可约束，风险可监控，执行可回放，核心性能瓶颈可下沉到 C++。

推荐主线：Python 用于探索、研究、建模和报告；C++ 用于定价、撮合、优化、实时风控、订单状态机和低延迟行情处理。两者通过 pybind11 或服务接口连接。

| 层级 | 你要获得的能力 | 典型产物 | 验收方式 |
| --- | --- | --- | --- |
| 理论回顾 | 知道公式和假设服务于什么工程问题 | 一页公式/概念卡片 | 能说出输入、输出、假设、失败场景 |
| 基础复现 | 把书中或文档中的算法跑通并测试 | notebook + unit tests | 与已知结果/库结果对照 |
| 论文复现 | 复现实证表格/图或模型核心结论 | paper reproduction report | 能解释与原文不一致的原因 |
| 框架落地 | 在真实框架中组织数据、模型、回测、风险和报告 | 可运行 repo | make reproduce 一键执行 |
| 工程化 | 把性能和交易关键路径下沉到 C++ | C++ lib + Python binding | benchmark + correctness tests |

## ୨୧ 1.1 总体研究闭环

```text
数据接入 -> 数据清洗/点时化 -> 特征/因子 -> 标签/预测 -> 信号
     -> 组合优化 -> 风险检查 -> 回测/模拟交易 -> 执行/订单 -> 复盘/归因
     -> 参数/模型/数据版本记录 -> 下一轮研究
```

每个模块都要产出三类结果：1）理论卡片；2）Python 复现；3）C++ 或性能关键路径实现。若某个方向暂时不做 C++，也要给出将来下沉到 C++ 的接口边界。

<div class="lace-break">⋆ ˚｡⋆୨୧˚ ⋆｡˚ ⋆</div>

# 🎀 2. 最小理论回顾：只保留落地必需的概念

下面不是完整理论教材，而是落地时最容易卡住的基础概念清单。每个概念都必须绑定一个可运行的实现任务。

| 理论块 | 必须理解的最小内容 | 对应实现任务 | 常见误区 |
| --- | --- | --- | --- |
| 概率统计 | 期望、方差、协方差、相关、分布尾部、置信区间、bootstrap | 收益率统计、IC 显著性、VaR/ES | 把正态假设当事实；忽略样本相关 |
| 时间序列 | 自相关、平稳性、ARIMA/GARCH、滚动估计、regime shift | 指数/crypto 波动率预测和 VaR | 随机 K-fold 泄漏未来 |
| 横截面资产定价 | CAPM、Fama-French、因子暴露、alpha/beta、t-stat | FF3/FF5 回归、因子分组 | 把相关性当可交易因果 |
| 优化 | 凸优化、QP、约束、KKT、正则化、估计误差 | 组合优化、最优执行 | 只最大化历史 Sharpe |
| 机器学习 | 标签、特征、验证、正则、校准、特征重要性 | triple-barrier、Qlib baseline | 只看 accuracy，不看交易收益 |
| 随机过程 | GBM、Ito、风险中性测度、蒙特卡洛 | BSM、Heston、LSM | 忽略 market convention 和校准 |
| 固收 | 贴现、期限结构、曲线、DV01、day count | curve bootstrap、swap pricing | 把收益率口径混用 |
| 信用 | 违约概率、回收率、hazard rate、信用利差 | Merton DD、CDS curve | 混淆实际 PD 与风险中性 PD |
| 市场微观结构 | 订单簿、spread、冲击成本、队列、maker/taker | TWAP/VWAP/做市回测 | 用 bar 回测推断限价单成交 |

<div class="lace-break">⋆ ˚｡⋆୨୧˚ ⋆｡˚ ⋆</div>

# 🎀 3. Python/C++ 工程栈与代码仓库结构

先搭一个“研究—复现—报告—C++ 核心”的统一仓库。所有模块都在同一个工程规范下迭代，而不是散落 notebook。

| 门类 | Python 侧 | C++ 侧 | 落地建议 |
| --- | --- | --- | --- |
| 数据工程 | pandas, Polars, PyArrow, DuckDB, parquet, yfinance/数据商 SDK | Arrow C++, DuckDB C++, HDF5, mmap, flatbuffers | 统一 symbol master、交易日历、点时数据、复权、缺失值和版本化 |
| 因子研究 | Alphalens, Qlib, statsmodels, scipy, sklearn | Eigen, Arrow, pybind11 | 横截面 rank/neutralize/winsorize 适合 C++ 加速 |
| 预测模型 | scikit-learn, LightGBM/XGBoost, PyTorch, Qlib, Optuna | ONNX Runtime C++, LightGBM C API, 自写线性/树模型 | Python 训练，C++ 在线推理；保持 feature parity |
| 回测 | vectorbt, Backtesting.py, Backtrader, Zipline/Qlib, RQAlpha/vn.py | 自写事件引擎、订单簿模拟、broker simulator | 先向量化，再事件驱动；结果可追踪 |
| 组合优化 | CVXPY, PyPortfolioOpt, Riskfolio-Lib, skfolio, OSQP | Eigen, OSQP C/C++, qpOASES/IPOPT(可选) | 矩阵构造在 Python，求解内核可 C++ |
| 风险模型 | arch, statsmodels, Riskfolio, scipy, empyrical/pyfolio | Eigen/BLAS, C++ risk service | 日报 + 盘中 pre-trade risk 两套节奏 |
| 衍生品/固收/信用 | QuantLib-Python, scipy, pandas | QuantLib C++, Eigen | QuantLib 是主线，自己实现小模型用于理解和测试 |
| 执行/连接 | ccxt, ib_insync, vn.py, Hummingbot, FastAPI | QuickFIX, websocketpp/Boost.Beast, spdlog/fmt | 生产交易链路必须状态机化、可回放、可审计 |
| 加密货币 | CCXT, Freqtrade, Hummingbot, pandas/Polars | C++ L2 order book builder, REST/WebSocket client | 考虑 7x24、资金费率、maker/taker、交易所风险 |
| 工程质量 | pytest, ruff, mypy, pre-commit, MLflow/DVC, Prefect/Airflow | GoogleTest, Google Benchmark, sanitizers, CMake, CI | 研究代码和生产内核都要测试、基准、版本化 |

## ୨୧ 3.1 推荐仓库结构

```text
quant-lab/
  README.md
  pyproject.toml
  environment.yml
  CMakeLists.txt
  configs/
    data.yaml
    backtest.yaml
    risk_limits.yaml
  data/                       # 不提交大数据；只提交 schema 和样例
    raw/
    interim/
    processed/
    features/
  notebooks/
    01_data_quality.ipynb
    02_factor_alphalens.ipynb
    03_ml_triple_barrier.ipynb
    04_portfolio_optimization.ipynb
    05_derivatives_quantlib.ipynb
  src/quantlab/
    data/ calendars.py corporate_actions.py point_in_time.py
    features/ factors.py labels.py neutralize.py
    models/ train.py inference.py validation.py
    backtest/ vectorized.py event_driven.py performance.py
    portfolio/ optimizer.py constraints.py costs.py
    risk/ factor_model.py var_es.py limits.py stress.py
    derivatives/ bsm.py quantlib_adapter.py
    crypto/ ccxt_client.py orderbook.py funding.py
    reports/ tear_sheet.py
  cpp/
    include/quantlab/
      factor_engine.hpp optimizer.hpp event_engine.hpp risk_engine.hpp bsm.hpp
    src/
      factor_engine.cpp optimizer.cpp event_engine.cpp risk_engine.cpp bsm.cpp
    bindings/
      pybind_module.cpp
    tests/
      test_factor_engine.cpp test_optimizer.cpp test_bsm.cpp
    benchmarks/
      bench_factor_engine.cpp bench_event_engine.cpp
  tests/
    test_data_no_leakage.py
    test_backtest_accounting.py
    test_portfolio_constraints.py
  reports/
    factor_reports/
    strategy_reports/
    risk_reports/
```

## ୨୧ 3.2 环境搭建任务

1.  Linux/WSL2 或 Docker：统一 Python、编译器、CMake、QuantLib、TA-Lib、DuckDB、Arrow。

2.  Python：mamba/uv 管理环境；pytest、ruff、mypy、pre-commit 作为默认质量门。

3.  C++：C++20、CMake、vcpkg/conan（二选一）、GoogleTest、Google Benchmark、sanitizers。

4.  数据：用 Parquet 分区存储；所有数据表必须有 schema、timezone、currency、calendar、point-in-time 字段说明。

5.  报告：每个 notebook 最终导出 HTML/PDF/markdown 摘要；核心图表和表格保存到 reports/。

<div class="lace-break">⋆ ˚｡⋆୨୧˚ ⋆｡˚ ⋆</div>

# 🎀 4. 模块化落地路线

每个模块都按同一模板推进：最小理论回顾 -> Python 复现 -> C++/性能关键路径 -> 经典论文复现 -> 验收标准。

## ୨୧ 4.1 因子投资：从横截面数据到可交易组合

目标：建立可复现的 factor research loop：定义因子、清洗样本、行业/市值中性化、分组检验、IC/RankIC、换手、容量、交易成本、组合构建。

| 环节 | 内容 |
| --- | --- |
| 最小理论 | • 横截面收益预测：r_{i,t+1}=a+b f_{i,t}+epsilon；重点不是推导，而是避免样本泄漏和行业暴露混淆。<br>• 评价指标：IC/RankIC、ICIR、分组收益、因子暴露、换手、收益归因、capacity。<br>• 因子组合：z-score、winsorize、neutralization、orthogonalization、Bayesian/ML blending。 |
| Python 落地 | • pandas/Polars 计算横截面因子；Alphalens 做 tear sheet；Qlib 管理数据、模型和回测；statsmodels 做 FF 回归。<br>• 先复现价值、动量、低波、质量、规模，再做多因子合成；每个因子必须产出 notebook + CSV + 报告。 |
| C++ 落地 | • 用 Arrow/Parquet 读取 panel 数据，Eigen 做矩阵运算，写 rolling window 和 cross-sectional rank 的 C++ 核心。<br>• 用 pybind11 暴露 factor_engine.rank_zscore_neutralize() 到 Python，比较 pandas/Polars/Numba/C++ 速度。 |
| 复现项目 | • 复现 Fama-French 三因子回归：用 Ken French 数据验证因子收益和 portfolio alpha。<br>• 复现 Jegadeesh-Titman 动量：J=12,K=1/3/6/12，跳过最近一个月，加入交易成本。<br>• 构建 A 股或美股多因子选股：每月调仓，行业中性，最大个股权重限制。 |
| 验收标准 | • 因子报告含 IC 序列、分组收益、回撤、换手、行业/市值暴露。<br>• 能解释为什么样本、调仓日、财报披露滞后和退市股票处理会影响结果。<br>• 同一因子 Python 与 C++ 输出误差在 1e-10 到 1e-8 量级。 |
| 资源/论文 | R3, R4, R18；论文：Fama-French、Carhart、Jegadeesh-Titman、López de Prado HRP/AFML。 |

## ୨୧ 4.2 预测模型：金融 ML 的可验证 pipeline

目标：把“预测涨跌”改造成可交易问题：标签、特征、样本权重、时间序列交叉验证、概率校准、模型解释和策略评价。

| 环节 | 内容 |
| --- | --- |
| 最小理论 | • 金融数据低信噪比、非平稳、样本相关；普通 K-fold 会泄漏未来。<br>• 标签：fixed-horizon、triple-barrier、meta-labeling；输出最好是概率/期望收益/风险调整信号。<br>• 模型：线性/树模型是基线，深度学习和强化学习需要更严格的 out-of-sample 和交易成本检验。 |
| Python 落地 | • scikit-learn、LightGBM/XGBoost、PyTorch、Qlib、Optuna；mlfinlab 可作参考，但优先自己复现核心算法。<br>• 实现 PurgedGroupTimeSeriesSplit、embargo、sample uniqueness、deflated Sharpe、feature importance。 |
| C++ 落地 | • C++ 负责高吞吐特征计算和在线推理；模型可通过 ONNX Runtime C++、LightGBM C API 或自写线性/树模型推理。<br>• 用 Google Benchmark 衡量特征延迟；用 pybind11 保持 Python research API。 |
| 复现项目 | • AFML triple-barrier + meta-labeling：以动量/突破为 primary model，二级模型决定是否交易。<br>• Qlib Alpha158/Alpha360 baseline：替换 LightGBM、MLP、Transformer，统一回测和风险报告。<br>• 事件驱动预测：财报/新闻/宏观日历的 event study，避免 announcement time 泄漏。 |
| 验收标准 | • train/valid/test 按时间滚动；所有 scaler/neutralizer 只在训练集 fit。<br>• 报告 precision-recall、calibration、turnover、capacity，而不仅是 accuracy。<br>• 模型上线前必须过 shadow trading 或 paper trading。 |
| 资源/论文 | R3, R10, R11, R12；论文：AFML、Qlib、FinRL、CVXPY/OSQP 用于下游组合。 |

## ୨୧ 4.3 回测：从向量化验证到事件驱动撮合

目标：建立两类回测器：研究速度优先的向量化回测，以及执行真实性优先的事件驱动回测；二者结果必须能互相解释。

| 环节 | 内容 |
| --- | --- |
| 最小理论 | • 回测不是收益曲线生成器，而是交易规则、数据时点、撮合规则、成本模型、约束系统。<br>• 关键误差源：look-ahead、survivorship bias、corporate action、delisting return、bid-ask bounce、partial fill、latency。<br>• 评价：CAGR、vol、Sharpe/Sortino、max drawdown、Calmar、turnover、exposure、capacity、tail risk。 |
| Python 落地 | • vectorbt 适合大规模参数扫描；Backtesting.py/Backtrader/RQAlpha/Zipline-reloaded 适合策略原型；Qlib 适合 ML 研究闭环。<br>• 建立统一 performance module：returns、positions、orders、transactions、risk exposures。 |
| C++ 落地 | • 实现 event queue、order book、broker simulator、position/accounting、commission/slippage；用 C++ 做可控、可测、可基准的核心。<br>• 用 Python 负责配置、数据准备、报告；C++ 负责撮合循环和风险检查。 |
| 复现项目 | • 均线交叉/突破策略：先 vectorbt，再事件驱动重写，比较差异。<br>• 横截面月度调仓：实现开盘/收盘成交、延迟成交、涨跌停/停牌处理。<br>• 订单簿回测：用 L2 数据模拟限价单排队、撤单、部分成交。 |
| 验收标准 | • 同一策略在极简成本假设下，向量化与事件驱动结果方向一致。<br>• 每笔交易可追踪从 signal 到 order 到 fill 到 position 到 PnL。<br>• 随机种子、数据快照、参数配置可完全复现。 |
| 资源/论文 | R2, R3, R20, R21, R22；论文：Almgren-Chriss、Avellaneda-Stoikov、Zhang et al. |

## ୨୧ 4.4 组合优化：把 alpha 变成约束下的仓位

目标：掌握从 alpha/risk 到 portfolio 的映射：均值方差、风险平价、Black-Litterman、CVaR、交易成本、换手、行业/风格/个股约束。

| 环节 | 内容 |
| --- | --- |
| 最小理论 | • 优化目标常见形式：max mu'w - lambda w'Sigma w - cost(w-w0)，subject to budget、bounds、exposure、turnover。<br>• 估计误差比求解算法更重要：收益预测极不稳定，协方差也需要 shrinkage、factor structure 或 robust 方法。<br>• 实盘组合构建通常是 alpha、risk、cost、constraints 的折中，不是单一 Sharpe 最大化。 |
| Python 落地 | • CVXPY 负责一般约束；PyPortfolioOpt 快速原型；Riskfolio-Lib/skfolio 研究多风险度量和 HRP；OSQP 用于二次规划。<br>• 建立 optimizer API：inputs=alpha,cov,exposure,cost,current_position；outputs=target_weight, trade_list, diagnostics。 |
| C++ 落地 | • Eigen 存储稀疏/稠密矩阵；OSQP C/C++ 接口做实时/批量优化；对约束、边界、热启动做单元测试。<br>• 把 Python 构建的矩阵序列化为 Arrow/npz，C++ 求解后回写 weight。 |
| 复现项目 | • MVO 稳定性实验：sample covariance vs Ledoit-Wolf vs factor covariance。<br>• Black-Litterman：把主观 views 或模型 alpha 映射为期望收益。<br>• 含交易成本和换手约束的月度多因子组合优化。 |
| 验收标准 | • 每次优化输出 KKT/solver status、约束违背、边际风险贡献、换手贡献。<br>• 能解释为何最大 Sharpe 组合常常极端；知道如何加 L2/L1/box/exposure 限制。<br>• 滚动外样本胜过或至少可解释地不弱于 1/N/市值权重基线。 |
| 资源/论文 | R5, R6, R7, R8, R13；论文：Markowitz、Ledoit-Wolf、DeMiguel、Black-Litterman、HRP。 |

## ୨୧ 4.5 风险模型：从收益波动到可解释风险预算

目标：构建日频组合风险、因子风险、尾部风险、压力测试和模型风险监控；让策略在回测和实盘中都有同一套风险语言。

| 环节 | 内容 |
| --- | --- |
| 最小理论 | • 风险不是单一波动率：包括市场/风格/行业/特质、流动性、集中度、杠杆、尾部、模型、操作风险。<br>• VaR/ES/GARCH/EVT/蒙特卡洛提供不同视角；需要 backtesting exceptions 和 stress scenarios。<br>• 因子风险模型：r = X f + u，组合风险 = w' X Cov(f) X' w + w' D w。 |
| Python 落地 | • statsmodels、arch、riskfolio、numpy/scipy；pandas/Polars 做暴露矩阵和归因表。<br>• 建立 daily_risk_report：exposure、factor contribution、specific risk、VaR/ES、stress、drawdown、leverage。 |
| C++ 落地 | • 高维风险矩阵分解、增量协方差、实时 exposure 检查；Eigen/BLAS 做核心。<br>• C++ risk engine 提供 check_order(order, portfolio_state, limits) 接口。 |
| 复现项目 | • Barra-like 风格/行业风险模型：市值、价值、动量、波动、流动性、行业哑变量。<br>• PCA 统计风险模型：比较 PCA 因子与基本面因子解释力。<br>• GARCH VaR/ES：对指数或 crypto 做 VaR 例外回测。 |
| 验收标准 | • 风险报告能解释策略收益来自哪个因子/行业/特质。<br>• 风控限额可被机器执行：最大杠杆、最大行业暴露、最大单名、最大回撤、最大订单。<br>• 压力情景明确：历史情景、假设情景、相关性上升、流动性折价。 |
| 资源/论文 | R6, R7, R8, R13；论文：Engle ARCH、Bollerslev GARCH、Barra-like literature、AFML 回测统计。 |

## ୨୧ 4.6 风险控制与执行：把研究信号接到订单系统

```text
目标：理解实盘交易链路：signal -> portfolio -> order -> pre-trade risk -> execution algo -> broker/exchange -> fill -> post-trade risk。
```

| 环节 | 内容 |
| --- | --- |
| 最小理论 | • 执行成本包括显性佣金、买卖价差、临时/永久冲击、机会成本、延迟和滑点。<br>• 风控必须前置：下单前检查、盘中检查、熔断/kill switch、权限、日志、审计。<br>• 交易系统关注 determinism、latency、throughput、state recovery，而不是 notebook 中的平均收益。 |
| Python 落地 | • Python 适合策略编排、监控 dashboard、回放工具、报表；异步 IO/WebSocket 可用于低频到中频。<br>• FastAPI/Redis/PostgreSQL/Prometheus/Grafana 可作为实验级交易与监控栈。 |
| C++ 落地 | • C++ 实现订单状态机、FIX 会话、低延迟行情处理、pre-trade risk；QuickFIX 是学习 FIX 的合适入口。<br>• 需要 GoogleTest/Benchmark、日志重放、断线重连、幂等订单处理。 |
| 复现项目 | • TWAP/VWAP/POV 执行算法：在模拟成交环境下比较成本分布。<br>• Almgren-Chriss 最优执行：用 QP 求执行轨迹，加入风险厌恶参数。<br>• C++ OMS mini-project：New/Cancel/Replace/Fill 状态机 + risk limit + replay log。 |
| 验收标准 | • 每个订单都有唯一 ID、状态迁移、时间戳、风险检查记录。<br>• 模拟交易支持断点恢复和日志重放。<br>• 有 kill switch：单日亏损、净/毛暴露、订单频率、异常成交价格。 |
| 资源/论文 | R17, R8, R13；论文：Almgren-Chriss、Kyle、Avellaneda-Stoikov。 |

## ୨୧ 4.7 衍生品：定价、Greeks、波动率和校准

目标：用 Python 快速验证模型，用 C++/QuantLib 实现定价和风险；覆盖 BSM、二叉树、PDE、蒙特卡洛、Heston、局部波动率。

| 环节 | 内容 |
| --- | --- |
| 最小理论 | • 风险中性定价、复制组合、无套利、贴现期望；Greeks 是风控语言。<br>• 模型的核心不是公式，而是 market convention、curve、vol surface、calendar、day count、settlement、exercise。<br>• 校准必须关注目标函数、bid-ask、参数边界、稳定性和再定价误差。 |
| Python 落地 | • QuantLib-Python 做产品/曲线/模型；SciPy 做校准；NumPy 实现公式和 Monte Carlo；matplotlib 输出 vol surface。<br>• 建立 option_pricer notebook：BSM -> Greeks -> implied vol -> surface -> Heston calibration。 |
| C++ 落地 | • QuantLib C++ 是主线；自写 Black-Scholes/Monte Carlo 作为理解和单元测试；pybind11 暴露 pricing API。<br>• C++ 定价服务应支持 instrument JSON -> price/risk JSON。 |
| 复现项目 | • BSM + implied vol solver + Greeks：Python/C++ 双实现。<br>• Heston calibration：用市场 IV surface 校准参数，比较再定价误差。<br>• Longstaff-Schwartz 美式期权：多项式基函数、路径数收敛、与 QuantLib 对照。 |
| 验收标准 | • BSM 与 QuantLib 结果误差在容忍范围内；Greeks 使用解析/有限差分/自动微分对比。<br>• 校准报告包括参数、误差热力图、稳定性和失败案例。<br>• 能清楚区分模型误差、数值误差、市场数据误差。 |
| 资源/论文 | R1；论文：Black-Scholes、Merton、Heston、Longstaff-Schwartz、Dupire。 |

## ୨୧ 4.8 固收：曲线、债券、互换和利率模型

目标：掌握 fixed income analytics：现金流、day count、yield、duration、convexity、zero curve、forward curve、swap、key-rate DV01。

| 环节 | 内容 |
| --- | --- |
| 最小理论 | • 固收落地首先是约定：日历、付息频率、计息规则、结算、假日、收益率口径。<br>• 曲线构建：deposit/futures/FRA/swap/bond bootstrapping；风险来自曲线节点。<br>• 利率模型：Vasicek/CIR/Hull-White 用于利率衍生品定价和情景模拟。 |
| Python 落地 | • QuantLib-Python 建立 yield curve、债券、swap、swaption；pandas 管理曲线节点和历史曲线。<br>• 写 curve_builder：输入报价表，输出 discount/zero/forward curve 和节点 DV01。 |
| C++ 落地 | • QuantLib C++ 实现曲线和产品；将常见产品封装成统一接口；用单元测试锁定 market convention。<br>• 用 Eigen 处理曲线 PCA、key-rate shocks 和情景矩阵。 |
| 复现项目 | • 国债/公司债现金流与 YTM：从头计算 dirty/clean price、accrued interest。<br>• USD/EUR/CNY swap curve bootstrapping：零息曲线与 forward rate 可视化。<br>• Hull-White calibration：校准 swaption volatility，输出 Bermudan swaption price。 |
| 验收标准 | • 每个产品都说明 day count、calendar、settlement、compounding。<br>• 风险报告包含 parallel DV01、key-rate DV01、curve scenario PnL。<br>• QuantLib 与自写简化公式结果可解释一致。 |
| 资源/论文 | R1；书：Hull、Björk、Brigo & Mercurio；论文：Vasicek、CIR、Hull-White。 |

## ୨୧ 4.9 信用：违约概率、信用利差、CDS 和组合信用风险

目标：建立信用风险最小可用系统：信用曲线、违约概率、回收率、CDS pricing、迁移矩阵、Merton distance-to-default。

| 环节 | 内容 |
| --- | --- |
| 最小理论 | • 结构模型从资产价值和资本结构推导违约；强度模型从 hazard rate 和 survival probability 定价。<br>• 信用产品落地关注 recovery、accrual on default、day count、curve、counterparty。<br>• 组合信用风险要处理相关性、集中度、行业/评级迁移、尾部损失。 |
| Python 落地 | • SciPy 求解 Merton 资产价值/波动率；QuantLib-Python 做 CDS helper 和 hazard curve；pandas 处理评级迁移。<br>• 建立 credit_lab：equity-implied DD、bond spread implied PD、CDS curve bootstrapping。 |
| C++ 落地 | • QuantLib C++ pricing；Eigen 做相关违约模拟和迁移矩阵；C++ 风控服务计算 exposure + expected loss。<br>• 把债券/发行人/评级/行业数据抽象成 point-in-time 数据模型。 |
| 复现项目 | • Merton model：用股票市值、负债、股价波动反推 DD 和 EDF proxy。<br>• CDS bootstrap：用不同期限 CDS spread 构建 survival curve，计算 upfront/running。<br>• 信用组合 VaR：迁移矩阵 + Gaussian copula 的简化实现。 |
| 验收标准 | • 能区分 risk-neutral PD 与 physical PD。<br>• 结果报告含 recovery 敏感性、curve 节点敏感性、issuer concentration。<br>• 模型局限明确：流动性、跳跃违约、财务数据滞后。 |
| 资源/论文 | R1；书：Duffie & Singleton；论文：Merton、Jarrow-Turnbull、Duffie-Singleton。 |

## ୨୧ 4.10 加密货币量化：交易所 API、永续合约、资金费率和做市

目标：在高噪声、高波动、7x24、交易所风险明显的市场中，建立数据采集、回测、执行和风控闭环。

| 环节 | 内容 |
| --- | --- |
| 最小理论 | • 加密市场结构：spot、perp、funding、basis、open interest、liquidation、maker/taker fee、exchange risk。<br>• 策略门类：横截面动量/反转、资金费率套利、期现/跨所 basis、统计套利、订单簿做市。<br>• 风险重点：API 限频、断线、极端波动、滑点、爆仓、交易所托管和合规。 |
| Python 落地 | • CCXT 统一 REST/WebSocket；Freqtrade 快速策略和回测；Hummingbot 学习做市/连接器/实盘框架。<br>• 建立 crypto_data_service：行情、订单簿、funding、open interest、fees、instrument metadata。 |
| C++ 落地 | • C++ websocket/orderbook builder、低延迟序列校验、增量快照恢复；Python 负责策略研究。<br>• 实现 L2 order book replay，输出 microprice、imbalance、spread、queue features。 |
| 复现项目 | • funding rate carry：筛选高资金费率合约，delta-hedged 或风险控制版。<br>• perp-spot basis：现货/永续价差回归和交易成本检验。<br>• Avellaneda-Stoikov crypto market making：库存限制、撤单频率、maker/taker fee。 |
| 验收标准 | • 回测考虑 maker/taker fee、funding、latency、partial fill、liquidation risk。<br>• 所有 API key 使用最小权限和环境变量；日志不泄漏密钥。<br>• 策略必须有交易所中断和极端价格保护。 |
| 资源/论文 | R14, R15, R16；论文：Avellaneda-Stoikov、Zhang et al.、market microstructure literature。 |

<div class="lace-break">⋆ ˚｡⋆୨୧˚ ⋆｡˚ ⋆</div>

# 🎀 5. 36 周执行计划

36 周不是唯一节奏。如果每周投入低于 10 小时，可把每一阶段拆成两倍时间；如果已有 Python/C++ 基础，可压缩准备和基础回测阶段。

| 阶段 | 周 | 主题 | 主要任务 | 交付/验收 |
| --- | --- | --- | --- | --- |
| 0. 准备 | 1-2 | 环境、数据、工程骨架 | Docker/conda、C++20/CMake、pytest、GoogleTest、Parquet 数据湖、统一配置 | 能一键跑通 download -> clean -> backtest -> report |
| 1. 数据与基础回测 | 3-6 | OHLCV/复权/日历/交易成本 | 均线/突破/再平衡策略；vectorbt + 自写简化回测器 | 输出第一份策略报告，含成本和参数敏感性 |
| 2. 因子投资 | 7-10 | 横截面因子和 Alphalens/Qlib | 复现 FF3/动量；实现中性化、IC、分组收益、多因子合成 | 每个因子有独立报告和无泄漏检查 |
| 3. 预测模型 | 11-14 | 金融 ML pipeline | triple-barrier、purged CV、LightGBM/Qlib、meta-labeling | 模型报告从 accuracy 转向交易收益与校准 |
| 4. 组合优化与风险 | 15-18 | alpha -> portfolio | CVXPY/PyPortfolioOpt/Riskfolio；MVO/BL/HRP/CVaR；daily risk report | 优化器可解释约束、边际风险、换手和成本 |
| 5. C++ 核心化 | 19-22 | 把慢/关键逻辑移到 C++ | Eigen/OSQP/pybind11；factor kernel、optimizer wrapper、event loop | Python 与 C++ 结果一致并有 benchmark |
| 6. 衍生品 | 23-26 | 期权定价与波动率 | BSM/Greeks/IV/Heston/LSM；QuantLib C++/Python | 定价报告可校准、可对照、可解释误差 |
| 7. 固收与信用 | 27-30 | 曲线、互换、CDS、违约模型 | QuantLib yield curve/swap/CDS；Merton DD；key-rate DV01 | 固收/信用 notebook + C++ product pricer |
| 8. 执行与风控 | 31-33 | 订单系统和风险控制 | QuickFIX 学习、OMS 状态机、pre-trade risk、TWAP/VWAP/AC | 订单生命周期和 kill switch 可回放 |
| 9. 加密货币与毕业项目 | 34-36 | CCXT/Freqtrade/Hummingbot + 总集成 | crypto data service、perp funding/basis、market making simulator | 完成一个端到端 capstone：研究、回测、风控、执行模拟、报告 |

## ୨୧ 5.1 每周固定工作流

| 步骤 | 动作 | 输出 |
| --- | --- | --- |
| 周初 | 选一个明确可复现目标：论文表格、框架示例、库函数重写或数据报告 | issue + config |
| 第 1-2 天 | 理论卡片：写出公式/假设/输入输出/失败场景，不超过一页 | theory_card.md |
| 第 3-4 天 | Python 实现：notebook 原型 + 模块化函数 + 单元测试 | notebook + src/ + tests/ |
| 第 5 天 | 对照验证：和论文/官方库/已知公式比较 | validation.md |
| 第 6 天 | C++ 或性能优化：只处理确实慢或交易关键路径 | cpp/ + benchmark |
| 第 7 天 | 复盘：记录错误、参数敏感性、下一步 | weekly_report.md |

## ୨୧ 5.2 复现报告模板

```markdown
# Reproduction Report
1. 目标：复现哪篇论文/哪一张表/哪一个框架示例？
2. 数据：来源、时间范围、字段、点时处理、缺失值、复权/退市。
3. 方法：公式、参数、调仓频率、成本、约束。
4. 结果：原文/官方结果 vs 本次结果；图表和误差。
5. 稳健性：时间分段、参数敏感性、成本敏感性、bootstrap。
6. 工程化：运行命令、依赖、随机种子、commit、耗时。
7. 结论：能否进入下一阶段？失败原因是什么？
```

<div class="lace-break">⋆ ˚｡⋆୨୧˚ ⋆｡˚ ⋆</div>

# 🎀 6. 经典论文复现清单

优先级建议：先做组合/因子/回测/ML，再做衍生品/固收/信用/执行/加密。每篇论文不要求完全复刻所有表格；最重要的是复现核心机制和工程产物。

表 6-1：组合、因子、协方差与金融 ML 复现任务

| 方向 | 作者/年份 | 题目 | 复现目标 | 实现建议 |
| --- | --- | --- | --- | --- |
| 组合/资产配置 | Markowitz (1952) | Portfolio Selection | 实现均值方差前沿；滚动窗口外样本对比 1/N | Python: CVXPY/PyPortfolioOpt；C++: Eigen+OSQP |
| 因子 | Fama & French (1993) | Common Risk Factors in the Returns on Stocks and Bonds | 下载 Ken French 因子；复现 FF3 回归、alpha、t-stat | statsmodels + 因子暴露矩阵 |
| 因子 | Carhart (1997) | On Persistence in Mutual Fund Performance | 加入 momentum；复现四因子绩效归因 | 自建 MOM 因子 + 回归 |
| 动量 | Jegadeesh & Titman (1993) | Returns to Buying Winners and Selling Losers | J-K 动量组合、跳过最近月、分组收益 | pandas/Polars 横截面排序 |
| 协方差 | Ledoit & Wolf (2004) | A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices | 实现 shrinkage covariance，比较 MVO 稳定性 | sklearn/PyPortfolioOpt + Eigen |
| 稳健组合 | DeMiguel, Garlappi & Uppal (2009) | Optimal Versus Naive Diversification | 滚动比较 MVO 与 1/N 的换手和 out-of-sample Sharpe | CVXPY + 回测器 |
| 层次风险 | López de Prado (2016) | Building Diversified Portfolios that Outperform Out of Sample | 复现 HRP 聚类、准对角化、递归二分 | scipy/skfolio/PyPortfolioOpt |
| 金融ML | López de Prado (2018) | Advances in Financial Machine Learning | triple barrier、meta-labeling、purged K-fold、deflated Sharpe | mlfinlab/自写实现 |
| AI平台 | Yang et al. (2020) | Qlib: An AI-oriented Quantitative Investment Platform | 跑通 Qlib Alpha158/Alpha360，替换模型并做 walk-forward | Qlib + LightGBM/PyTorch |
| 强化学习 | Liu et al. (2021) | FinRL | 复现股票/组合/crypto DRL pipeline；强调风控和评价 | FinRL + baseline 回测 |
| 加密 | Zhang et al. (2022) | A Data Science Pipeline for Algorithmic Trading | 股票/crypto 策略统一 pipeline；复现 MA/VWAP/情绪/统计套利 | CCXT + pandas + 回测器 |

表 6-2：衍生品、固收、信用、执行与做市复现任务

| 方向 | 作者/年份 | 题目 | 复现目标 | 实现建议 |
| --- | --- | --- | --- | --- |
| 期权 | Black & Scholes (1973) | The Pricing of Options and Corporate Liabilities | 从公式到 Greeks；Python/C++ 单元测试 | NumPy + C++ 模板函数 |
| 期权 | Merton (1973) | Theory of Rational Option Pricing | 理解 BSM 扩展和股息/无风险资产设定 | QuantLib 对照 |
| 随机波动率 | Heston (1993) | A Closed-Form Solution for Options with Stochastic Volatility | 实现/调用 Heston pricing；校准 IV surface | QuantLib + SciPy optimize |
| 美式期权 | Longstaff & Schwartz (2001) | Valuing American Options by Simulation | LSM 蒙特卡洛回归；比较二叉树/QuantLib | NumPy/C++ Monte Carlo |
| 利率 | Vasicek (1977) | An Equilibrium Characterization of the Term Structure | 短端模型模拟、债券价格闭式解 | QuantLib + C++ |
| 利率 | Cox, Ingersoll & Ross (1985) | A Theory of the Term Structure of Interest Rates | CIR 路径与零息债价格；比较 Vasicek | QuantLib + 自写模拟 |
| 利率 | Hull & White (1990) | Pricing Interest-Rate-Derivative Securities | 曲线拟合、短端模型校准、swaption 定价 | QuantLib |
| 信用 | Merton (1974) | On the Pricing of Corporate Debt | 股票价值+波动率反推资产价值/违约距离 | SciPy root finding + Eigen |
| 信用 | Jarrow & Turnbull (1995) | Pricing Derivatives on Financial Securities Subject to Credit Risk | 强度模型、违约概率曲线、信用价差 | pandas + QuantLib credit |
| 执行 | Kyle (1985) | Continuous Auctions and Insider Trading | 理解 price impact 与订单流；做市场景模拟 | 订单流仿真 |
| 执行 | Almgren & Chriss (2001) | Optimal Execution of Portfolio Transactions | 最优执行轨迹、冲击成本、风险惩罚 | CVXPY/OSQP + C++ |
| 做市 | Avellaneda & Stoikov (2008) | High-frequency trading in a limit order book | 库存惩罚、报价偏移、PnL 分布 | 事件驱动回测 + crypto order book |

<div class="lace-break">⋆ ˚｡⋆୨୧˚ ⋆｡˚ ⋆</div>

# 🎀 7. 书、论文、官方文档与数据资源

## ୨୧ 7.1 核心书单

| 层级/方向 | 作者 | 书名 | 为什么读 | 读法 |
| --- | --- | --- | --- | --- |
| 入门落地 | Yves Hilpisch | Python for Finance, 2nd ed. | Python 金融数据、衍生品、回测与交互式分析；配套 notebook 适合复现 | 先读代码，再回看公式 |
| 金融机器学习 | Marcos López de Prado | Advances in Financial Machine Learning | 金融标签、样本权重、purged CV、回测统计、组合建仓思想 | 作为预测模型模块主线 |
| 系统交易实践 | Andreas F. Clenow | Trading Evolved | 系统交易、期货/股票策略、Python 回测和策略工程 | 适合第一阶段策略复现 |
| 投资组合 | Grinold & Kahn | Active Portfolio Management | IC、IR、组合构建、主动风险预算、组合经理语言 | 因子投资和风险预算核心 |
| 组合优化 | Boyd & Vandenberghe | Convex Optimization | 凸优化、KKT、二次规划、约束建模 | 只精读组合优化相关章节 |
| 衍生品 | John C. Hull | Options, Futures, and Other Derivatives | 期权、期货、互换、风险中性定价、Greek、波动率 | 理论回顾+QuantLib 实现 |
| 连续时间 | Tomas Björk | Arbitrage Theory in Continuous Time, 4th ed. | 风险中性测度、随机微积分、衍生品定价严格框架 | 作为推导参考，不必通读 |
| 利率/固收 | Brigo & Mercurio | Interest Rate Models: Theory and Practice | 曲线、短端模型、市场模型、校准 | 固收模块精读 |
| 信用 | Duffie & Singleton | Credit Risk | 结构化/强度模型、违约、信用衍生品 | 信用模块参考 |
| 执行/微观结构 | Cartea, Jaimungal & Penalva | Algorithmic and High-Frequency Trading | 最优执行、做市、订单簿、微观结构 | 执行和加密做市模块 |

## ୨୧ 7.2 官方框架与资源

| 编号 | 资源 | 用途 | 链接 |
| --- | --- | --- | --- |
| R1 | QuantLib 官方网站与文档 | C++/Python 衍生品、固收、信用定价和风险管理 | https://www.quantlib.org/ ; https://www.quantlib.org/docs.shtml |
| R2 | vectorbt 文档 | pandas/NumPy/Numba/Rust 风格的向量化研究和回测 | https://vectorbt.dev/ |
| R3 | Microsoft Qlib | AI-oriented quant investment platform；数据、模型、回测、工作流 | https://github.com/microsoft/qlib ; https://arxiv.org/abs/2009.11189 |
| R4 | Alphalens | 预测因子分析：IC、分组收益、换手、tear sheet | https://github.com/quantopian/alphalens |
| R5 | PyPortfolioOpt | 均值方差、Black-Litterman、HRP、协方差估计 | https://pyportfolioopt.readthedocs.io/ |
| R6 | Riskfolio-Lib | CVXPY 上层的组合优化库，覆盖多种风险度量 | https://riskfolio-lib.readthedocs.io/ |
| R7 | CVXPY | Python 嵌入式凸优化建模语言 | https://www.cvxpy.org/ |
| R8 | OSQP | C/C++/Python 可用的凸二次规划求解器 | https://osqp.org/docs/ |
| R9 | TA-Lib | C/C++ 核心的技术指标库，提供 Python API | https://ta-lib.org/ |
| R10 | pybind11 | C++ 与 Python 绑定，适合把 C++ 定价/回测内核暴露给 Python | https://pybind11.readthedocs.io/ |
| R11 | Numba | Python/NumPy 子集 JIT 编译，适合滚动窗口、事件循环加速 | https://numba.pydata.org/ |
| R12 | Cython | Python/C 扩展的静态编译路线 | https://cython.org/ |
| R13 | Eigen | C++ 矩阵、分解、数值线性代数基础库 | https://libeigen.gitlab.io/ |
| R14 | CCXT | 统一的加密货币交易所 API，Python/JS/PHP/C#/Go/Java | https://docs.ccxt.com/ |
| R15 | Freqtrade | Python 开源加密交易机器人，含回测、绘图、资金管理和优化 | https://www.freqtrade.io/ |
| R16 | Hummingbot | 开源 Python 框架，用于 CEX/DEX 自动化策略和做市 | https://hummingbot.org/docs/ |
| R17 | QuickFIX | C++/Python/Ruby 等语言绑定的 FIX 协议引擎 | https://quickfixengine.org/ |
| R18 | Kenneth French Data Library | Fama-French 因子数据和组合收益数据 | https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html |
| R19 | NYSE TAQ / WRDS TAQ | 美股逐笔交易与报价数据，适合微观结构与执行研究 | https://www.nyse.com/market-data/historical ; https://wrds-www.wharton.upenn.edu/pages/about/data-vendors/nyse-trade-and-quote-taq/ |
| R20 | vn.py / VeighNa | Python 开源量化交易系统，底层和性能敏感基础设施使用 C++ | https://github.com/vnpy/vnpy |
| R21 | RQAlpha / Ricequant 文档 | 可扩展 Python 回测与交易框架；中文生态资源 | https://github.com/ricequant/rqalpha ; https://www.ricequant.com/doc/ |
| R22 | JoinQuant / 聚宽 API 文档 | 中文量化投研平台、数据、回测和 API | https://www.joinquant.com/api |

## ୨୧ 7.3 数据资源路线

| 数据类别 | 免费/低成本起步 | 专业/机构级 | 注意事项 |
| --- | --- | --- | --- |
| 股票日频 | Stooq、Yahoo/yfinance、Alpha Vantage、交易所公开数据、聚宽/米筐试用 | CRSP/Compustat、Bloomberg、Refinitiv、FactSet、Wind、Choice | 免费源适合学习，不适合严肃研究；注意复权、退市、生存者偏差 |
| 因子数据 | Ken French Data Library | WRDS、Barra/Axioma/自建风险模型 | 因子定义和构造口径必须记录 |
| 高频/订单簿 | 加密交易所公开 API、部分 broker demo | NYSE TAQ、LOBSTER、交易所直连、专门数据商 | 时区、序列号、丢包、撮合规则、延迟极重要 |
| 宏观/利率 | FRED、Treasury、央行网站 | Bloomberg、Refinitiv、Markit、Wind | 发布日期和修订值需要 point-in-time |
| 期权/衍生品 | CBOE 部分公开、交易所样例、数据商试用 | OptionMetrics、ORATS、Bloomberg、交易所数据 | IV surface 需要清洗 bid-ask、异常报价和到期日 |
| 加密 | CCXT 交易所 OHLCV/orderbook/funding、Binance/OKX API | Kaiko、Coin Metrics、CryptoQuant、Amberdata | 交易所口径不一致；永续合约资金费率和指数价格必须入库 |

<div class="lace-break">⋆ ˚｡⋆୨୧˚ ⋆｡˚ ⋆</div>

# 🎀 8. 质量控制清单与毕业项目

## ୨୧ 8.1 回测和研究防坑清单

| 检查项 | 标准 |
| --- | --- |
| 数据时点 | 任何财报、成分股、评级、宏观数据必须使用发布日期/可得日期，而不是报告期或文件日期。 |
| 复权与退市 | 股票研究必须处理 split/dividend/delisting；指数成分股不能用今天的成分回测过去。 |
| 训练验证 | 时间序列使用 walk-forward；横截面模型用 purging/embargo；禁止随机 K-fold 直接用于金融时间序列。 |
| 成本模型 | 至少有 commission、spread、slippage、market impact、borrow/funding；加密还需 funding 和 maker/taker fee。 |
| 约束 | 组合权重、个股上限、行业/风格暴露、换手、杠杆、做空、可交易性都必须显式建模。 |
| 统计显著性 | 报告 deflated/probabilistic Sharpe、bootstrap、参数敏感性；警惕 data snooping。 |
| 会计一致性 | cash、position、market value、realized/unrealized PnL、fees 必须逐笔可追踪。 |
| 可复现 | 数据快照、配置、随机种子、代码 commit、依赖版本、报告版本必须记录。 |
| 性能 | 先 profile 再 C++；C++ 模块要有 correctness tests 和 benchmark。 |
| 安全 | API key 不进代码和日志；交易权限最小化；实盘有 kill switch 和人工确认流程。 |

## ୨୧ 8.2 毕业项目选题

毕业项目要把至少四个模块连起来：数据、模型/因子、回测、组合/风险、报告；若选择交易系统方向，则要加入订单状态机和风控。

| 项目 | 必须包含 | 适合方向 |
| --- | --- | --- |
| 多因子股票组合 | 因子库 + Qlib/Alphalens + CVXPY 优化 + 风险模型 + 月度再平衡 | 适合想做股票多空/指数增强 |
| 期权波动率研究 | BSM/IV surface + Heston calibration + Greeks risk + hedging backtest | 适合衍生品/做市方向 |
| 固收曲线与互换 | curve bootstrap + swap pricing + key-rate DV01 + Hull-White calibration | 适合固收量化/风险方向 |
| 信用风险小系统 | Merton DD + CDS bootstrap + issuer concentration + credit VaR | 适合信用/多资产风控 |
| 加密资金费率/做市 | CCXT 数据 + perp funding/basis + event-driven fill + exchange risk limits | 适合 crypto quant/交易系统 |
| C++ 回测/执行内核 | event queue + order state machine + pre-trade risk + Python bindings | 适合量化开发/交易系统工程 |

## ୨୧ 8.3 最终验收标准

1.  一键复现：从配置文件出发，能生成数据样例、模型输出、回测结果和报告。

2.  可解释：每个收益来源、风险来源、成本来源都能归因。

3.  可测试：关键函数有单元测试；Python 与 C++ 核心输出一致。

4.  可扩展：新增资产、因子、模型、优化约束时，不需要重写整个系统。

5.  可风控：有 pre-trade limit、portfolio risk、drawdown/kill switch、日志审计。

6.  可复盘：每次实验记录数据版本、参数、随机种子、代码 commit 和结果摘要。

<div class="lace-break">⋆ ˚｡⋆୨୧˚ ⋆｡˚ ⋆</div>

# 🎀 附录 A：推荐学习顺序（极简版）

| 顺序 | 先做什么 | 不要先做什么 |
| --- | --- | --- |
| 1 | 先把数据、复权、回测会计和交易成本做对 | 不要一上来调深度学习模型 |
| 2 | 先复现简单因子和简单组合优化 | 不要直接追求复杂另类数据 |
| 3 | 先建立报告模板和防泄漏检查 | 不要只看单条 equity curve |
| 4 | 先用 Python 跑通，再把瓶颈下沉 C++ | 不要为了 C++ 而 C++ |
| 5 | 先做低频/中频闭环，再做订单簿/低延迟 | 不要用日频 bar 推断高频成交 |
| 6 | 先完成一个毕业项目，再扩展资产类别 | 不要所有门类同时浅尝辄止 |

<div class="lace-break">⋆ ˚｡⋆୨୧˚ ⋆｡˚ ⋆</div>

# 🎀 附录 B：C++ 与 Python 分工边界

| 场景 | 留在 Python | 下沉 C++ 的信号 | 接口建议 |
| --- | --- | --- | --- |
| 因子计算 | 探索式特征、一次性研究 | 横截面/滚动窗口在全市场多参数下成为瓶颈 | pybind11 函数，输入 NumPy/Arrow，输出 ndarray |
| 回测 | 日频向量化、多参数扫描 | 事件循环、订单簿、撮合和会计成为瓶颈 | C++ engine + Python config/report |
| 优化 | CVXPY 建模和诊断 | 同类 QP 高频重复求解、需要 warm start | OSQP C++ wrapper，Python 构造矩阵 |
| 定价 | 公式验证、校准脚本 | 大批量产品/场景定价、风险重估 | QuantLib C++ service 或 pybind11 |
| 执行 | 低频交易、监控、配置 | 订单状态机、FIX、行情处理、低延迟风控 | C++ service + message queue/FIX |
| 加密订单簿 | REST 数据下载、研究 | WebSocket 增量深度、序列校验、L2 回放 | C++ orderbook builder + Python features |

<div class="lace-break">⋆ ˚｡⋆୨୧˚ ⋆｡˚ ⋆</div>

# 🎀 附录 C：第一周可执行任务清单

1.  创建 quant-lab 仓库，加入 pyproject.toml、environment.yml、CMakeLists.txt、pre-commit。

2.  下载一个公开日频价格数据集和 Ken French 因子数据；保存为 Parquet；写 schema.md。

3.  实现 returns.py：simple/log returns、rolling vol、drawdown、turnover。

4.  实现第一个向量化策略：月度 12-1 动量多空或均线交叉。

5.  实现第一个报告：收益曲线、回撤、年化收益/波动/Sharpe、换手、成本敏感性。

6.  写 test_no_lookahead.py：确保信号只能使用调仓日前可见数据。

7.  写第一份 weekly_report.md：记录数据源、假设、失败点、下一周任务。

<div class="lace-break">⋆ ˚｡⋆୨୧˚ ⋆｡˚ ⋆</div>

# 🎀 附录 D：参考资料引用说明

本文档中的官方框架和资源链接以 2026-06-20 查询结果为基础。开源项目版本和维护状态会变化，实际学习时应以官方文档、GitHub release 和许可证为准。

对论文复现，优先使用期刊页面、作者页面、SSRN/arXiv 或学校镜像。不要依赖来路不明的盗版 PDF；若无访问权限，可先复现公开摘要、公式和可获得数据的核心机制。

