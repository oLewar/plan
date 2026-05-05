---
title: "TencentCloud/CubeSandbox: Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents."
source: "https://github.com/TencentCloud/CubeSandbox"
author:
published:
created: 2026-04-28
description: "Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents. - TencentCloud/CubeSandbox"
tags:
  - "clippings"
---
[![Cube Sandbox Logo](https://github.com/TencentCloud/CubeSandbox/raw/master/docs/assets/cube-sandbox-logo.png)](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/assets/cube-sandbox-logo.png)

## CubeSandbox

**Instant, Concurrent, Secure & Lightweight Sandbox Service for AI Agents**

[**中文文档**](https://github.com/TencentCloud/CubeSandbox/blob/master/README_zh.md) · [**Quick Start**](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/guide/quickstart.md) · [**Documentation**](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/index.md) · [**Discord**](https://discord.gg/kkapzDXShb)

---

Cube Sandbox is a high-performance, out-of-the-box secure sandbox service built on RustVMM and KVM. It supports both single-node deployment and can be easily scaled to a multi-node cluster. It is compatible with the E2B SDK, capable of creating a hardware-isolated sandbox environment with full service capabilities in under 60ms, while maintaining less than 5MB memory overhead.

[![](https://github.com/TencentCloud/CubeSandbox/raw/master/docs/assets/readme_speed_en_1.png)](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/assets/readme_speed_en_1.png) [![](https://github.com/TencentCloud/CubeSandbox/raw/master/docs/assets/readme_overhead_en_1.png)](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/assets/readme_overhead_en_1.png)

## Demos

| 1.cubesandbox.-.mp4<video src="https://private-user-images.githubusercontent.com/63215266/579121140-f87c409e-29fc-4e86-9eac-dbeaff2aca18.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzc0MDc3MDksIm5iZiI6MTc3NzQwNzQwOSwicGF0aCI6Ii82MzIxNTI2Ni81NzkxMjExNDAtZjg3YzQwOWUtMjlmYy00ZTg2LTllYWMtZGJlYWZmMmFjYTE4Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA0MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNDI4VDIwMTY0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTNlNTVmMzE2ZjllYjk0NzQxMjVjZTE4ODIwNzc3NWM1NDIxMGNlZDM4NzY2M2RhYzJhOTFiNDM3OWE3NGMyMjQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT12aWRlbyUyRm1wNCJ9.TpIQBfS0uxO0TDf__umnSUcQgvE1V4oKlDZtNXWvB-A" controls="controls"></video> | 2.cubesandbox.demo.mp4<video src="https://private-user-images.githubusercontent.com/63215266/579121164-50e7126e-bb73-4abc-aa85-677fdf2e8c67.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzc0MDc3MDksIm5iZiI6MTc3NzQwNzQwOSwicGF0aCI6Ii82MzIxNTI2Ni81NzkxMjExNjQtNTBlNzEyNmUtYmI3My00YWJjLWFhODUtNjc3ZmRmMmU4YzY3Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA0MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNDI4VDIwMTY0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdhMzRjZjkzOWJlNWU3ZTkzYTY1ZDdmNWEwNTA1NjQyZDEzNDkxMjBmN2QyZjM5MzljYzQ0ZWY1MWVkNTM2ZDEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT12aWRlbyUyRm1wNCJ9.GKNlgE5MSqmiBKM5-fjw2HzTqbna2F98UzJ56wbCUw8" controls="controls"></video> | Cube-Sandbox.RL.demo.mp4<video src="https://private-user-images.githubusercontent.com/63215266/579120806-052e0e77-e2d9-409e-90b8-d13c28b80495.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzc0MDc3MDksIm5iZiI6MTc3NzQwNzQwOSwicGF0aCI6Ii82MzIxNTI2Ni81NzkxMjA4MDYtMDUyZTBlNzctZTJkOS00MDllLTkwYjgtZDEzYzI4YjgwNDk1Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA0MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNDI4VDIwMTY0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWY5YzMzNWM2NzMzOWFjZWY3YWRlNWZlM2I2MzAzYjYyYzRhNWUyMDdiY2I3YjJkNmU4NGRjNzIzMDIxNGEyYjYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT12aWRlbyUyRm1wNCJ9.NEIgq4g0jHIO3CNa0ME3VWhwXCpZJAQaZRWKLyKcN-Q" controls="controls"></video> |
| --- | --- | --- |
| *Installation & Demo* | *Performance Test* | *RL (SWE-Bench)* |

## Core Highlights

- **Blazing-fast cold start:** Built on resource pool pre-provisioning and snapshot cloning technology, skipping time-consuming initialization entirely. Average end-to-end cold start time for a fully serviceable sandbox is < 60ms.
- **High-density deployment on a single node:** Extreme memory reuse via CoW technology combined with a Rust-rebuilt, aggressively trimmed runtime keeps per-instance memory overhead below 5MB — run thousands of Agents on a single machine.
- **True kernel-level isolation:** No more unsafe Docker shared-kernel (Namespace) hacks. Each Agent runs with its own dedicated Guest OS kernel, eliminating container escape risks and enabling safe execution of any LLM-generated code.
- **Zero-cost migration (E2B drop-in replacement):** Natively compatible with the E2B SDK interface. Just swap one URL environment variable — no business logic changes needed — to migrate from expensive closed-source sandboxes to free Cube Sandbox with better performance.
- **Network security:** CubeVS, powered by eBPF, enforces strict inter-sandbox network isolation at the kernel level with fine-grained egress traffic filtering policies.
- **Ready to use out of the box:** One-click deployment with support for both single-node and cluster setups.
- **Event-level snapshot rollback (coming soon):** High-frequency snapshot rollback at millisecond granularity, enabling rapid fork-based exploration environments from any saved state.
- **Production-ready:** Cube Sandbox has been validated at scale in Tencent Cloud production environments, proven stable and reliable.

## Benchmarks

In the context of AI Agent code execution, CubeSandbox achieves the perfect balance of security and performance:

| Metric | Docker Container | Traditional VM | CubeSandbox |
| --- | --- | --- | --- |
| **Isolation Level** | Low (Shared Kernel Namespaces) | High (Dedicated Kernel) | **Extreme (Dedicated Kernel + eBPF)** |
| **Boot Speed**   \*Full-OS boot duration | 200ms | Seconds | **Sub-millisecond (<60ms)** |
| **Memory Overhead** | Low (Shared Kernel) | High (Full OS) | **Ultra-low (Aggressively stripped, <5MB)** |
| **Deployment Density** | High | Low | **Extreme (Thousands per node)** |
| **E2B SDK Compatible** | / | / | **✅ Drop-in** |

- *Cold start benchmarked on bare-metal. 60ms at single concurrency; under 50 concurrent creations, avg 67ms, P95 90ms, P99 137ms — consistently sub-150ms.*
- *Memory overhead measured with sandbox specs ≤ 32GB. Larger configurations may see a marginal increase.*

For detailed metrics on startup latency and resource overhead, please refer to:

<table align="center"><tbody><tr align="center"><td width="33%"><a href="https://github.com/TencentCloud/CubeSandbox/blob/master/docs/assets/1-concurrency-create.png"><img src="https://github.com/TencentCloud/CubeSandbox/raw/master/docs/assets/1-concurrency-create.png"></a></td><td width="33%"><a href="https://github.com/TencentCloud/CubeSandbox/blob/master/docs/assets/50-concurrency-create.png"><img src="https://github.com/TencentCloud/CubeSandbox/raw/master/docs/assets/50-concurrency-create.png"></a></td><td width="33%"><a href="https://github.com/TencentCloud/CubeSandbox/blob/master/docs/assets/cube-sandbox-mem-overhead.png"><img src="https://github.com/TencentCloud/CubeSandbox/raw/master/docs/assets/cube-sandbox-mem-overhead.png"></a></td></tr><tr align="center"><td colspan="2"><em>Sub-150ms sandbox delivery under both single and high-concurrency workloads</em></td><td><em>CubeSandbox base memory footprint across various instance sizes</em><br><sup>(*Blue: Sandbox specifications; Orange: Base memory overhead). Note that memory consumption increases only marginally as instance sizes scale up.</sup></td></tr></tbody></table>

## Quick Start

[![Cube Sandbox fast start walkthrough](https://github.com/TencentCloud/CubeSandbox/raw/master/docs/assets/fast-start.gif)](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/guide/quickstart.md)

*⚡ Millisecond-level startup — watch the fast-start flow, then jump into the [Quick Start guide](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/guide/quickstart.md).*

Cube Sandbox requires a KVM-enabled x86\_64 Linux environment — **WSL 2**, a **Linux physical machine**, or a **cloud bare-metal server** all work.

> Don't have one yet?
> 
> - **Windows users**: run `wsl --install` in an admin PowerShell to set up WSL 2 (requires Windows 11 22H2+, with nested virtualization enabled in BIOS / WSL).
> - **Others**: grab an x86\_64 Linux physical machine, or rent a bare-metal server from a cloud provider.

Once your environment is ready, launch your first sandbox in four steps:

1. **Prepare the runtime environment** (skip this step if you already have an x86\_64 bare-metal Linux server)

Run the following on your WSL / Linux machine:

```
git clone https://github.com/tencentcloud/CubeSandbox.git
# For faster access from mainland China, clone from the mirror instead:
# git clone https://cnb.cool/CubeSandbox/CubeSandbox

cd CubeSandbox/dev-env
./prepare_image.sh   # one-off: download and initialize the runtime image
./run_vm.sh          # boot the environment; keep this terminal open (Ctrl+a x to exit)
```

In a second terminal, log into the environment you just prepared:

```
cd CubeSandbox/dev-env && ./login.sh
```

> This drops you into a disposable Linux environment where all the subsequent installation happens, so your host stays clean. See [Development Environment](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/guide/dev-environment.md) for details.

2. **Start the Cube Sandbox Service**

Inside the environment you entered via `login.sh` (or directly on your bare-metal server), run **one** of the following commands depending on your location:

- **Global Users** (downloads from GitHub):
	```
	curl -sL https://github.com/tencentcloud/CubeSandbox/raw/master/deploy/one-click/online-install.sh | bash
	```
- **中国用户请执行这条命令 (Mainland China)**:
	```
	curl -sL https://cnb.cool/CubeSandbox/CubeSandbox/-/git/raw/master/deploy/one-click/online-install.sh | MIRROR=cn bash
	```

> See [Quick Start — China mainland mirror](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/guide/quickstart.md#step-2-install) for details.

3. **Create a Code Interpreter Sandbox Template**

After installation, create a code interpreter template from the prebuilt image:

```
cubemastercli tpl create-from-image \
  --image ccr.ccs.tencentyun.com/ags-image/sandbox-code:latest \
  --writable-layer-size 1G \
  --expose-port 49999 \
  --expose-port 49983 \
  --probe 49999
```

Then run the following command to monitor the build progress:

```
cubemastercli tpl watch --job-id <job_id>
```

**⚠️**

**The image is fairly large** — downloading, extracting, and building the template may take a while; please be patient.

Wait for the command above to finish and the template status to reach `READY`. Note the **template ID** (`template_id`) from the output — you will need it in the next step.

4. **Run Your First Agent Code**

Install the Python SDK:

```
yum install -y python3 python3-pip
pip install e2b-code-interpreter
```

Set environment variables:

```
export E2B_API_URL="http://127.0.0.1:3000"
export E2B_API_KEY="dummy"
export CUBE_TEMPLATE_ID="<your-template-id>"  # template ID obtained from Step 3
export SSL_CERT_FILE="/root/.local/share/mkcert/rootCA.pem"
```

Run code inside an isolated sandbox:

```
import os
from e2b_code_interpreter import Sandbox  # drop-in E2B SDK

# Cube Sandbox transparently intercepts all requests
with Sandbox.create(template=os.environ["CUBE_TEMPLATE_ID"]) as sandbox:
    result = sandbox.run_code("print('Hello from Cube Sandbox, safely isolated!')")
    print(result)
```

> See [Quick Start — Step 4](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/guide/quickstart.md#step-4-run-your-first-agent) for the full variable reference and more examples.

Want to explore more? Check out the 📂 [`examples/`](https://github.com/TencentCloud/CubeSandbox/blob/master/examples) directory, covering scenarios like: code execution, Shell commands, file operations, browser automation, network policies, pause/resume, OpenClaw integration, and RL training.

### Deep Dive

- 📖 [Documentation Home](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/index.md) - Complete guide and API reference
- 🔧 [Template Concepts](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/guide/templates.md) - Image-to-Template concepts and workflows
- 🌟 [Example Projects](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/guide/tutorials/examples.md) - Hands-on examples demonstrating various Cube Sandbox use cases (Browser automation, OpenClaw integration, RL training workflows, etc.)
- 💻 [Development Environment (QEMU VM)](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/guide/dev-environment.md) - No bare-metal? Spin up a disposable OpenCloudOS 9 VM and run Cube Sandbox inside it

## Architecture

[![Cube Sandbox Architecture](https://github.com/TencentCloud/CubeSandbox/raw/master/docs/assets/cube-sandbox-arch.png)](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/assets/cube-sandbox-arch.png)

| Component | Responsibility |
| --- | --- |
| **CubeAPI** | High-concurrency REST API Gateway (Rust), compatible with E2B. Swap the URL for seamless migration. |
| **CubeMaster** | Cluster orchestrator. Receives API requests and dispatches them to corresponding Cubelets. Manages resource scheduling and cluster state. |
| **CubeProxy** | Reverse proxy, compatible with the E2B protocol, routing requests to the appropriate sandbox instances. |
| **Cubelet** | Compute node local scheduling component. Manages the complete lifecycle of all sandbox instances on the node. |
| **CubeVS** | eBPF-based virtual switch, providing kernel-level network isolation and security policy enforcement. |
| **CubeHypervisor & CubeShim** | Virtualization layer — CubeHypervisor manages KVM MicroVMs, CubeShim implements the containerd Shim v2 API to integrate sandboxes into the container runtime. |

👉 For more details, please read the [Architecture Design Document](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/architecture/overview.md) and [CubeVS Network Model](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/architecture/network.md).

## Community & Contributing

We welcome contributions of all kinds—whether it’s a bug report, feature suggestion, documentation improvement, or code submission!

- 🐞 **Found a Bug?** Submit an issue on [GitHub Issues](https://github.com/tencentcloud/CubeSandbox/issues).
- 💡 **Have an Idea?** Join the conversation in [GitHub Discussions](https://github.com/tencentcloud/CubeSandbox/discussions).
- 🛠️ **Want to Code?** Check out our [CONTRIBUTING.md](https://github.com/TencentCloud/CubeSandbox/blob/master/CONTRIBUTING.md) to learn how to submit a Pull Request.
- 💬 **Want to Chat?** Join our [Discord](https://discord.gg/kkapzDXShb).

## License

CubeSandbox is released under the [Apache License 2.0](https://github.com/TencentCloud/CubeSandbox/blob/master/LICENSE).

The birth of CubeSandbox stands on the shoulders of open-source giants. Special thanks to [Cloud Hypervisor](https://github.com/cloud-hypervisor/cloud-hypervisor), [Kata Containers](https://github.com/kata-containers/kata-containers), virtiofsd, containerd-shim-rs, ttrpc-rust, and others. We have made tailored modifications to some components to fit the CubeSandbox execution model, and the original in-file copyright notices are preserved.