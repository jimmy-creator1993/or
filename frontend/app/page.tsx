"use client";

import { CopilotChat } from "@copilotkit/react-core/v2";

export default function Home() {
  return (
    <main className="chat-shell">
      <CopilotChat
        agentId="deep_agent"
        labels={{
          modalHeaderTitle: "DeepAgent",
          chatInputPlaceholder: "给 DeepAgent 发消息…",
          welcomeMessageText: "你好！我是 DeepAgent，有什么可以帮你？",
        }}
      />
    </main>
  );
}
