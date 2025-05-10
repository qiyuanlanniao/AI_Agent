# AI Agent: 智能应用平台 🚀

一个多功能 AI Agent 应用，利用大型语言模型 (LLM)、检索增强生成 (RAG)、自动化工具调度、持久化记忆和情绪感知能力。本项目旨在为特定场景提供智能对话、自动化任务执行以及无缝的语音交互。

## 🌟 项目概览

本项目展示了一款先进 AI Agent 的设计与开发。它集成了专业知识库（通过 RAG），允许动态调用工具以执行复杂任务，并通过持久化、具备情绪感知的记忆模块来维护对话上下文。该系统专为稳健的 LLM 操作而设计，并通过标准化 API 暴露其功能，从而能够与 Telegram 机器人和语音服务等外部系统集成。

该项目是作为专业实习的一部分开发的，专注于攻克 LLM 工程化难题并构建实用型 AI 驱动应用。

## ✨ 核心功能

*   **🧠 LLM 驱动核心：** 利用大型语言模型（例如通过 LangChain）作为中央决策引擎。
*   **📚 RAG 增强知识库：** 与向量数据库 (Qdrant) 和自定义加载器集成，实现检索增强生成，为 Agent 提供专业知识的访问能力。
*   **🛠️ 动态工具调用：** 使用 LangChain ToolKits 和自定义工具，允许 Agent 自主选择并执行各种功能以完成复杂任务。
*   **💾 持久化与情绪感知记忆：** 实现 LangChain Memory 模块以支持多轮对话上下文，并探索情绪感知以实现更细致的交互。
*   **🗣️ 语音与文本交互：** 支持基于文本（例如 Telegram 机器人）和基于语音（通过 SpeechSDK）的交互。
*   **🔌 标准化 API 层：** 使用 FastAPI 构建，为前端应用和第三方集成提供简洁、高效且可扩展的 API。
*   **🐳 Docker 化部署：** 配置为 Docker 部署，简化环境配置并确保环境一致性。
*   **📊 Langsmith 监控：** 集成 Langsmith 以实现对 LLM 链和 Agent 行为的可观测性、调试与监控。
*   **🔧 LLM 工程化实践：** 解决 LLM 应用开发中的常见挑战，包括自定义工具集成、记忆持久化、多工具参数校验等。

## 🛠️ 技术栈

*   **AI & LLM：**
    *   Python 3.10
    *   LangChain (Loader, Vectorization, Vector DB, Chains, Memory, ToolKit, Chatdoc)
    *   检索增强生成 (RAG)
*   **后端 (Backend)：**
    *   FastAPI
*   **数据库 (Database)：**
    *   Qdrant (向量数据库)
*   **外部服务与集成 (External Services & Integrations)：**
    *   Telebot (Python Telegram Bot API)
    *   Microsoft SpeechSDK (用于语音合成/识别)
*   **DevOps & 工具 (DevOps & Tools)：**
    *   Docker
    *   Langsmith
    *   Git & GitHub

## 🏗️ 架构概览 (概念性)

系统采用模块化架构设计：

1.  **输入/输出层 (Input/Output Layer)：** 通过 API (FastAPI)、Telegram 机器人 (Telebot) 和语音 (SpeechSDK) 处理交互。
2.  **LLM 核心引擎 (LLM Core Engine)：** 中央 LangChain Agent 或 Chain，负责处理输入、做出决策并编排任务。
3.  **记忆模块 (Memory Module)：** LangChain Memory 组件，用于保留对话历史和上下文。
4.  **RAG 模块 (RAG Module)：**
    *   **知识库 (Knowledge Base)：** 存储和处理的文档/数据。
    *   **向量化 (Vectorization)：** LangChain Loaders 和 Embeddings 将文本转换为向量。
    *   **向量存储 (Vector Store)：** Qdrant 数据库，用于高效的语义搜索。
    *   **检索器 (Retriever)：** 为 LLM 获取相关上下文。
5.  **工具管理与执行 (Tool Manager & Execution)：** LangChain ToolKits 和自定义工具，LLM 可以调用它们来执行特定操作（例如 API 调用、数据库查询、计算）。
6.  **监控与日志 (Monitoring & Logging)：** 集成 Langsmith 进行跟踪和调试。

## 🚀 快速开始

### 环境要求 (Prerequisites)

*   Python 3.9+
*   Docker
*   LLM API 访问权限(ChatGpt)
*   Qdrant 实例 (可以通过 Docker 运行)
*   Telegram Bot Token (如果使用 Telegram 集成)
*   Microsoft SpeechSDK 订阅密钥和区域 (如果使用语音功能)
*   Langsmith API Key (可选, 用于监控)

### 安装步骤 (Installation)

1.  **克隆仓库：**
    ```bash
    git clone https://github.com/你的用户名/你的AI_AGENT仓库名.git
    cd 你的AI_AGENT仓库名
    ```

2.  **创建并激活虚拟环境 (推荐)：**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows 系统: venv\Scripts\activate
    ```

3.  **安装依赖：**
    ```bash
    pip install -r requirements.txt
    ```

### 运行应用 (Running the Application)

1.  **启动 FastAPI 服务：**
    ```bash
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```
    (假设您的 FastAPI 应用实例在 `main.py` 文件中，并且名为 `app`)

2.  **运行 Telegram Bot (如适用)：**
    您可能有一个单独的脚本来运行 Telegram Bot，例如：
    ```bash
    python telegram_bot.py
    ```

## 🎮 使用说明 (Usage)

*   **API 端点 (API Endpoints)：** 应用通过 FastAPI 暴露了多个 API 端点。您可以在服务运行时通过浏览器访问 API 文档 (Swagger UI 或 ReDoc)，通常地址为 `http://localhost:8000/docs` 或 `http://localhost:8000/redoc`。
    *   例如：`POST /chat`，请求体为 JSON 格式，如 `{"message": "你好 Agent"}`。
*   **Telegram Bot (电报机器人)：** 通过向您配置的 Telegram Bot 发送消息来与 Agent 互动。
*   **语音交互 (Voice Interaction)：** (如果通过特定接口实现，请描述如何触发语音输入/输出)。
