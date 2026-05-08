---
title: "InsForge/InsForge: Give agents everything they need to ship fullstack apps. The backend built for agentic development."
source: "https://github.com/InsForge/InsForge"
author:
published:
created: 2026-05-05
description: "Give agents everything they need to ship fullstack apps. The backend built for agentic development.  - InsForge/InsForge: Give agents everything they need to ship fullstack apps. The backend built for agentic development."
tags:
  - "clippings"
---
[

![InsForge](../assets/external/github.com/e4be7889fe9d45e5.svg)

](https://insforge.dev/)

The backend built for agentic development.

[![InsForge%2FInsForge | Trendshift](../assets/external/camo.githubusercontent.com/f2e0982985fbad1e.svg)](https://trendshift.io/repositories/19834)  

⭐ *Help us reach more developers and grow the InsForge community. Star this repo!*

## InsForge

InsForge is a backend development platform built for AI coding agents and AI code editors. It exposes backend primitives like databases, auth, storage, and functions through a semantic layer that agents can understand, reason about, and operate end to end.

InsForge-readme.mp4<video src="https://github.com/user-attachments/assets/2e2a43c9-4664-48a6-b61b-4f7cf8eb0ebf" controls="controls"></video>

### How it works

InsForge acts as a semantic layer between AI coding agents and backend primitives. It performs backend context engineering so agents can understand, operate, and inspect backend systems.

- **Fetch backend context**: Agents can fetch documentation and available operations for the backend primitives they use.
- **Configure primitives**: Agents can configure backend primitives directly.
- **Inspect backend state**: Backend state and logs are exposed through structured schemas.

```
graph TB

    subgraph TOP[" "]
        AG[AI Coding Agents]
    end

    subgraph MID[" "]
        SL[InsForge Semantic Layer]
    end

    AG --> SL

    SL --> AUTH[Authentication]
    SL --> DB[Database]
    SL --> ST[Storage]
    SL --> EF[Edge Functions]
    SL --> MG[Model Gateway]
    SL --> DEP[Deployment]

    classDef bar fill:#0b0f14,stroke:#30363d,stroke-width:1px,color:#ffffff
    classDef card fill:#161b22,stroke:#30363d,stroke-width:1px,color:#ffffff

    class AG,SL bar
    class AUTH,DB,ST,EF,MG,DEP card

    style TOP fill:transparent,stroke:transparent
    style MID fill:transparent,stroke:transparent

    linkStyle default stroke:#30363d,stroke-width:1px
```

### Core Products:

- **Authentication**: User management, authentication, and sessions
- **Database**: Postgres relational database
- **Storage**: S3 compatible file storage
- **Model Gateway**: OpenAI compatible API across multiple LLM providers
- **Edge Functions**: Serverless code running on the edge
- **Site Deployment**: Site build and deployment

## ⭐️ Star the Repository

[![Star InsForge](../assets/external/github.com/75489941c45676eb.gif)](https://github.com/InsForge/InsForge/blob/main/assets/insforge-star.gif)

If you find InsForge useful or interesting, a GitHub Star ⭐️ would be greatly appreciated.

## Quickstart

### Cloud-hosted: insforge.dev

### Self-hosted: Docker Compose

Prerequisites: [Docker](https://www.docker.com/) + [Node.js](https://nodejs.org/)

#### 1\. Setup

You can run InsForge locally using Docker Compose. This will start a local InsForge instance on your machine.

[![Deploy on Docker](../assets/external/github.com/64580a81a02c2c8b.png)](https://github.com/InsForge/InsForge/blob/main/deploy/docker-deploy.md)

Or run from source:

```
# Run with Docker
git clone https://github.com/insforge/insforge.git
cd insforge
cp .env.example .env
docker compose -f docker-compose.prod.yml up
```

#### 2\. Connect InsForge MCP

Open [http://localhost:7130](http://localhost:7130/)

Follow the steps to connect InsForge MCP Server

[![Connect InsForge MCP](../assets/external/github.com/faf1c81593171e98.png)](https://github.com/InsForge/InsForge/blob/main/assets/connect.png)

#### 3\. Verify installation

To verify the connection, send the following prompt to your agent:

```
I'm using InsForge as my backend platform, call InsForge MCP's fetch-docs tool to learn about InsForge instructions.
```

#### 4\. Running Multiple Projects

You can run multiple InsForge projects on the same host by using different ports and project names.

```
# Create a separate env file for each project
cp .env.example .env.project1
cp .env.example .env.project2
```

Edit `.env.project2` with different ports:

```
POSTGRES_PORT=5442
POSTGREST_PORT=5440
APP_PORT=7230
AUTH_PORT=7231
DENO_PORT=7233
```

Start each project with a unique name:

```
docker compose -f docker-compose.prod.yml --env-file .env.project1 -p project1 up -d
docker compose -f docker-compose.prod.yml --env-file .env.project2 -p project2 up -d
```

Each project gets its own isolated database, storage, and configuration. Manage them with:

```
docker compose -f docker-compose.prod.yml --env-file .env.project1 -p project1 ps      # status
docker compose -f docker-compose.prod.yml --env-file .env.project1 -p project1 logs -f  # logs
docker compose -f docker-compose.prod.yml --env-file .env.project1 -p project1 down     # stop
```

### One-click Deployment

In addition to running InsForge locally, you can also launch InsForge using a pre-configured setup. This allows you to get up and running quickly with InsForge without installing Docker on your local machine.

| Railway | Zeabur | Sealos |
| --- | --- | --- |
| [![Deploy on Railway](../assets/external/camo.githubusercontent.com/70c5830b361062f0.svg)](https://railway.com/deploy/insforge) | [![Deploy on Zeabur](../assets/external/camo.githubusercontent.com/53d650517f022d1e.svg)](https://zeabur.com/templates/Q82M3Y) | [![Deploy on Sealos](../assets/external/camo.githubusercontent.com/f2b8f74841ad5910.svg)](https://sealos.io/products/app-store/insforge) |

## Contributing

**Contributing**: If you're interested in contributing, you can check our guide here [CONTRIBUTING.md](https://github.com/InsForge/InsForge/blob/main/CONTRIBUTING.md). We truly appreciate pull requests, all types of help are appreciated!

**Support**: If you need any help or support, we're responsive on our [Discord channel](https://discord.com/invite/MPxwj5xVvW), and also feel free to email us [info@insforge.dev](mailto:info@insforge.dev) too!

## Documentation & Support

### Documentation

- **[Official Docs](https://docs.insforge.dev/introduction)** - Comprehensive guides and API references

### Community

- **[Discord](https://discord.com/invite/MPxwj5xVvW)** - Join our vibrant community
- **[Twitter](https://x.com/InsForge_dev)** - Follow for updates and tips

### Contact

- **Email**: [info@insforge.dev](mailto:info@insforge.dev)

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](https://github.com/InsForge/InsForge/blob/main/LICENSE) file for details.

---

[![Star History Chart](../assets/external/camo.githubusercontent.com/b8b3259988de5656.svg)](https://www.star-history.com/#InsForge/insforge&Date)

## Badges

Show your project is built with InsForge.

### Made with InsForge

**Markdown:**

```
[![Made with InsForge](../assets/external/insforge.dev/7387dfb9916fa6f6.svg)](https://insforge.dev)
```

**HTML:**

```
<a href="https://insforge.dev">
  <img
    width="168"
    height="30"
    src="../assets/external/insforge.dev/7387dfb9916fa6f6.svg"
    alt="Made with InsForge"
  />
</a>
```

### Made with InsForge (dark)

**Markdown:**

```
[![Made with InsForge](../assets/external/insforge.dev/9acb795eaeaecf0e.svg)](https://insforge.dev)
```

**HTML:**

```
<a href="https://insforge.dev">
  <img
    width="168"
    height="30"
    src="../assets/external/insforge.dev/9acb795eaeaecf0e.svg"
    alt="Made with InsForge"
  />
</a>
```

⭐ **Star us on GitHub** to get notified about new releases!