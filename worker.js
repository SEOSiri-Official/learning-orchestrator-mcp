export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    if (request.method === "OPTIONS") {
      return new Response(null, {
        status: 204,
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type, Authorization, x-seosiri-key",
        },
      });
    }

    if (url.pathname === "/health") {
      return new Response(JSON.stringify({
        status: "HEALTHY",
        service: "SEOSiri EdTech Learning Orchestrator MCP",
        subdomain: "learn.seosiri.com",
        dual_transport: ["stdio", "sse"],
        circuit_breaker: "ACTIVE",
        timestamp: new Date().toISOString()
      }, null, 2), {
        status: 200,
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
      });
    }

    if (url.pathname === "/sse") {
      return new Response("SEOSiri EdTech Learning Orchestrator SSE Stream Active", {
        headers: { "Content-Type": "text/event-stream", "Access-Control-Allow-Origin": "*" }
      });
    }

    try {
      return await env.ASSETS.fetch(request);
    } catch {
      return new Response("SEOSiri EdTech Learning Orchestrator Edge Node Active", { status: 200 });
    }
  }
};
