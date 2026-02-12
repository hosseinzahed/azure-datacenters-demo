# 🌍 Azure Datacenters Demo

> A demonstration project showcasing **GitHub Copilot's advanced features** through building an interactive 3D visualization of Azure datacenter locations worldwide.

[![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-Enabled-blue?logo=github)](https://github.com/features/copilot)
[![Docker](https://img.shields.io/badge/Docker-Required-2496ED?logo=docker)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Latest-336791?logo=postgresql)](https://www.postgresql.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Python-009688?logo=fastapi)](https://fastapi.tiangolo.com/)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Prerequisites](#-prerequisites)
- [Project Architecture](#-project-architecture)
- [Implementation Guide](#-implementation-guide)
- [Final Output](#-final-output)

---

## 🎯 Overview

This project demonstrates how to leverage **GitHub Copilot** with different AI models and modes to build a complete full-stack application. The application visualizes Azure datacenter locations on an interactive 3D globe.

### Key Components

- **🎨 Frontend**: Interactive 3D globe using `three-globe` JavaScript library
- **⚙️ Backend**: FastAPI service with Python (runs on port `8000`)
- **🗄️ Database**: PostgreSQL running in Docker container
- **🤖 AI-Powered Development**: Built using various GitHub Copilot models and modes

---

## 📦 Prerequisites

Before starting this project, ensure you have the following tools installed:

### 1. 🤖 GitHub Copilot

**What it is**: AI pair programmer that helps you write code faster and with fewer errors.

**Installation Steps**:

1. **Subscribe to GitHub Copilot**:
   - Visit [GitHub Copilot](https://github.com/features/copilot)
   - Click "Get GitHub Copilot" and choose a plan (Individual, Business, or Enterprise)
   - Students, teachers, and maintainers of popular open-source projects can get it for free

2. **Install in Visual Studio Code**:
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X / Cmd+Shift+X)
   - Search for "GitHub Copilot"
   - Install the following extensions:
     - **GitHub Copilot** (by GitHub)
     - **GitHub Copilot Chat** (by GitHub)
   - Sign in with your GitHub account when prompted

3. **Verify Installation**:
   - Look for the Copilot icon in the VS Code status bar (bottom right)
   - Open Copilot Chat with `Ctrl+Shift+I` / `Cmd+Shift+I`

**Resources**:
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)

---

### 2. 🐳 Docker Desktop

**What it is**: Platform for developing, shipping, and running applications in containers. Required for running PostgreSQL database.

**Installation Steps**:

**Windows**:
1. Visit [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)
2. Click "Download for Windows"
3. Run the installer (Docker Desktop Installer.exe)
4. Follow the installation wizard
5. Enable WSL 2 if prompted
6. Restart your computer
7. Launch Docker Desktop from the Start menu

**macOS**:
1. Visit [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)
2. Download the appropriate version:
   - **Apple Silicon** (M1/M2/M3): Choose "Mac with Apple chip"
   - **Intel**: Choose "Mac with Intel chip"
3. Open the downloaded `.dmg` file
4. Drag Docker to Applications folder
5. Launch Docker from Applications
6. Grant necessary permissions when prompted

**Linux**:
1. Visit [Docker Desktop for Linux](https://docs.docker.com/desktop/install/linux-install/)
2. Follow distribution-specific instructions (Ubuntu/Debian/Fedora/Arch)
3. Or use Docker Engine CLI: 
   ```bash
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   ```

**Verify Installation**:
```bash
docker --version
docker run hello-world
```

**Resources**:
- [Docker Desktop Documentation](https://docs.docker.com/desktop/)
- [Docker Getting Started](https://docs.docker.com/get-started/)

---

### 3. 📚 Microsoft Docs MCP Server

**What it is**: Model Context Protocol (MCP) server that provides GitHub Copilot with access to official Microsoft and Azure documentation using a remote server connection.

**Installation Steps**:

1. **Access MCP Marketplace in VS Code**:
   - Open Command Palette (Ctrl+Shift+P / Cmd+Shift+P)
   - Type "MCP: Add Server"
   - Select "Browse MCP Marketplace"

2. **Install Microsoft Docs MCP Server**:
   - Search for "Microsoft Docs" in the marketplace
   - Click on the "Microsoft Docs MCP Server"
   - Click "Install" or "Add Server"

3. **Configure Remote MCP Connection**:
   - When prompted, select **"Use remote server"**
   - The server will connect to Microsoft's hosted MCP endpoint
   - No local installation or npm packages required

4. **Verify Installation**:
   - Restart VS Code if prompted
   - Open GitHub Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
   - Try asking: `@microsoft-docs What are Azure regions?`
   - You should receive answers grounded in official Microsoft documentation

**Resources**:
- [MCP Documentation](https://modelcontextprotocol.io/)
- [Microsoft Docs MCP Server](https://github.com/microsoft/mcp-servers)

---

### 4. 🐍 Python (3.8 or higher)

**Installation**:
- **Windows/macOS**: Download from [python.org](https://www.python.org/downloads/)
- **Linux**: Usually pre-installed, or use package manager:
  ```bash
  sudo apt update && sudo apt install python3 python3-pip
  ```

**Verify**:
```bash
python --version
pip --version
```

---

### 5. 🗄️ PostgreSQL VS Code Extension

**Installation**:
1. Open VS Code Extensions (Ctrl+Shift+X)
2. Search for "PostgreSQL" by Microsoft
3. Install the extension
4. This enables database management directly from VS Code

---

## 🚀 Implementation Guide

Follow these steps to build the complete application using GitHub Copilot's various models and modes:

### Step 1: Generate User Stories (GPT-5.2-Codex - Plan Mode)

Use GitHub Copilot in Plan mode to analyze [Idea.md](Idea.md) and generate three separate user stories:
- Frontend features → `backlog/features-frontend.md`
- Backend features → `backlog/features-backend.md`
- Database schema → `backlog/features-database.md`

### Step 2: Implement Backend (Claude Sonnet 4.5 - Agent Mode)

Use Claude Sonnet 4.5 to implement the backend user story:
```
Implement the features-backend.md user story in the backend folder.
```

### Step 3: Implement Frontend (Claude Sonnet 4.5 - Agent Mode)

Use Claude Sonnet 4.5 to implement the frontend user story:
```
Implement the features-frontend.md user story in the frontend folder.
```

### Step 4: Generate Azure Datacenter Data (GPT-4.1 - Agent Mode)

Use GPT-4.1 to create the datacenter dataset from official Azure documentation:
```
Create a JSON array listing Azure datacenters based on official docs, including each region's location, country, and city. Save the output as a file in the .data directory.
```

### Step 5: Start PostgreSQL Database

Run the PostgreSQL container using Docker:
```bash
docker run --name local-postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=az-dc-db -p 5432:5432 -d postgres:latest
```

### Step 6: Connect to Database

Using the PostgreSQL VS Code extension:
1. Open the PostgreSQL panel in VS Code
2. Right-click on the database connection
3. Select "Connect in Agent mode"

### Step 7: Setup Database Schema (Claude Sonnet 4.5 - Agent Mode)

Use the `@pgsql` agent to implement the database user story:
```
@pgsql Implement the feature-database.md user story in the database. Use the json file in the .data folder for seeding.
```

### Step 8: Configure Environment

Create a `.env` file in the `backend` folder with the necessary configuration.

### Step 9: Run the Application (Auto - Agent Mode)

Use GitHub Copilot in Agent mode to set up and run both services:
```
Help me with preparing the environments and running both backend and frontend apps.
```

---

ℹ️ **Note**: The complete implementation can be found in the `final-output` branch.

---

## 📚 Additional Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [Microsoft Learn - GitHub Copilot](https://learn.microsoft.com/en-us/training/github/)

---

**Happy Coding! 🎉** May your code be clean and your Copilot suggestions be ever helpful!

