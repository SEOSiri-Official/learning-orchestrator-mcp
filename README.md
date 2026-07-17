# learning-orchestrator-mcp

An open-source, stateless, and high-performance Model Context Protocol (MCP) server designed to orchestrate progressive curriculum learning, track skills development using cognitive spacing, and securely interface with external AI educational platforms and LMS networks.

[![learning-orchestrator-mcp MCP server](https://glama.ai/mcp/servers/SEOSiri-Official/learning-orchestrator-mcp/badges/card.svg)](https://glama.ai/mcp/servers/SEOSiri-Official/learning-orchestrator-mcp)

## 💖 Sponsorship, B2B Custom Solutions & Attribution

### 👨‍💻 Lead Architect & Attribution
This framework is designed and engineered by **[Momenul Ahmad](https://github.com/MOBILEPHONE)**, Lead Architect and Founder of **[SEOSiri](https://seosiri.com)**.

Momenul Ahmad is the systems architect behind three globally registered open-source bio-robotic and safety innovations:
1. **[seosiri-biorobotics](https://github.com/SEOSiri-Official/biorobotics):** A stateless bio-robotic coordinate mapper translating genomic data to G-code.
2. **[seosiri-api-guard-mcp-server](https://github.com/SEOSiri-Official/seosiri-api-guard-mcp-server):** A multi-industry API validation proxy with a decoupled policy enforcement plane.
3. **[learning-orchestrator-mcp](https://github.com/SEOSiri-Official/learning-orchestrator-mcp):** This AI-driven pedagogical and spaced-repetition engine.

All three systems are developed under the official **[SEOSiri-Official](https://github.com/SEOSiri-Official)** open-source research initiative.

### 🚀 B2B Custom Solutions & Consulting
We offer high-ticket technical consulting and custom enterprise integrations for corporate training and educational networks:
- **AI-Driven LMS Integrations:** Connecting our pedagogical core securely to corporate Learning Management Systems (LMS) to automate employee onboarding using active recall and spaced repetition.
- **Custom Subject-Segment Mappings:** Designing and compiling custom progressive syllabi and automated assessment banks mapped to proprietary, closed-source company technical manuals.
- **Secure Cross-Platform Handshakes:** Designing custom, highly secure HMAC-SHA256 connection handshakes to link multi-agent AI ecosystems with student identity servers safely.

To discuss custom educational deployments, corporate onboarding setups, or licensing, contact the architecture team directly:
- **Official Website:** [seosiri.com](https://seosiri.com)
- **Enterprise Support Email:** [admin@seosiri.com](mailto:admin@seosiri.com)

### 🪙 Support the Research (Sponsorship)
If you wish to fund continued open-source safety research or help maintain our global MCP listings, consider sponsoring the core team:
- **GitHub Sponsors:** [Sponsor SEOSiri-Official](https://github.com/sponsors/SEOSiri-Official)

## Decoupled Subject Segments
- **Robotics & Kinematics:** Standard Cartesian coordinate space mapping, G-code instructions, and deck calibrations.
- **API Security & Compliance:** OWASP injections, HIPAA PII/PHI validations, and cryptographic signature checks.
- **Digital Marketing & SEO/AEO:** JSON-LD schema design, GDPR privacy structures, and conversational voice-search optimizations.

## Quickstart
1. **Install Package in Editable Mode:**
   ```bash
   pip install -e .

   #Verify the Pedagogical Test Suite:
   pytest tests/test_learning.py

   ##🔌 How to Connect to Claude Desktop or Cursor IDE
You can connect this server to your local AI clients using one of two standard methods.
Method 1: Direct Execution from GitHub (Zero-Setup, Recommended)
If you have uv installed, you can run the server directly from our public repository without cloning it locally.
Open your claude_desktop_config.json (Windows: %APPDATA%\Claude\claude_desktop_config.json | macOS: ~/Library/Application Support/Claude/claude_desktop_config.json) and add this configuration:
{
  "mcpServers": {
    "seosiri-learning-orchestrator": {
      "command": "uv",
      "args": [
        "run",
        "--github",
        "SEOSiri-Official/learning-orchestrator-mcp",
        "src/main_server.py"
      ]
    }
  }
}

#Method 2: Local Execution (If Cloned)
If you have cloned this repository to your local drive, configure your client to point to your local entry file:
{
  "mcpServers": {
    "seosiri-learning-orchestrator": {
      "command": "python",
      "args": [
        "D:/learning-orchestrator-mcp/src/main_server.py"
      ],
      "env": {
        "PYTHONPATH": "D:/learning-orchestrator-mcp"
      }
    }
  }
}