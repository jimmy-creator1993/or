# DeepAgent + CopilotKit 聊天 Demo

一个最小全栈聊天 demo：Python 后端使用 LangChain DeepAgents，并通过 AG-UI 暴露；Next.js 前端使用 CopilotKit `CopilotChat`。

## 环境要求

- Python 3.11+
- Node.js 20+
- OpenAI API key

## 配置与启动

在项目根目录创建 `.env`：

```env
OPENAI_API_KEY=your-openai-api-key
MODEL=openai:gpt-4o-mini
```

后端终端：

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m backend.main
```

前端终端：

```bash
cd frontend
npm install
npm run dev
```

打开 http://localhost:3000。后端默认运行在 http://localhost:8124。

## 结构

- `backend/main.py`：DeepAgent + FastAPI AG-UI 端点
- `frontend/app/api/copilotkit/[[...slug]]/route.ts`：CopilotKit runtime 到 AG-UI 后端的代理
- `frontend/app/page.tsx`：仅显示对话框

对话记忆由进程内 `MemorySaver` 提供，重启后清空，适合本地 demo。
