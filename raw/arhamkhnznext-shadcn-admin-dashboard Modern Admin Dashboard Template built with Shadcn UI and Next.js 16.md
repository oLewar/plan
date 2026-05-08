---
title: "arhamkhnz/next-shadcn-admin-dashboard: Modern Admin Dashboard Template built with Shadcn UI and Next.js 16"
source: "https://github.com/arhamkhnz/next-shadcn-admin-dashboard"
author:
published:
created: 2026-05-07
description: "Modern Admin Dashboard Template built with Shadcn UI and Next.js 16 - arhamkhnz/next-shadcn-admin-dashboard"
tags:
  - "clippings"
---
## Next.js Admin Template with TypeScript & Shadcn UI

**Studio Admin** - Includes multiple dashboards, authentication layouts, customizable theme presets, and more.

[![Dashboard Screenshot](https://github.com/arhamkhnz/next-shadcn-admin-dashboard/raw/main/media/dashboard.png?version=5)](https://github.com/arhamkhnz/next-shadcn-admin-dashboard/blob/main/media/dashboard.png?version=5)

Most admin templates I found, free or paid, felt cluttered, outdated, or too rigid. I built this as a cleaner alternative with features often missing in others, such as theme toggling and layout controls, while keeping the design modern, minimal, and flexible.

> **View demo:** [studio admin](https://next-shadcn-admin-dashboard.vercel.app/)

> [!note] Note
> Looking for the Base UI version? Check out [next-shadcn-admin-dashboard-baseui](https://github.com/arhamkhnz/next-shadcn-admin-dashboard-baseui).

> [!tip] Tip
> I’m also working on Nuxt.js, Svelte, and React (Vite + TanStack Router) versions of this dashboard. They’ll be live soon.

## Features

- Built with Next.js 16, TypeScript, Tailwind CSS v4, and Shadcn UI
- Responsive and mobile-friendly
- Customizable theme presets (light/dark modes with color schemes like Tangerine, Brutalist, and more)
- Flexible layouts (collapsible sidebar, variable content widths)
- Authentication flows and screens
- Prebuilt dashboards (Default, CRM, Finance, Analytics, Productivity) plus legacy variants
- Role-Based Access Control (RBAC) with config-driven UI and multi-tenant support *(planned)*

> [!note] Note
> The default dashboard uses the **shadcn neutral** theme.  
> It also includes additional color presets inspired by [Tweakcn](https://tweakcn.com/):
> 
> - Tangerine
> - Neo Brutalism
> - Soft Pop
> 
> You can create more presets by following the same structure as the existing ones.

> Looking for the **Next.js 15** version?  
> Check out the [`archive/next15`](https://github.com/arhamkhnz/next-shadcn-admin-dashboard/tree/archive/next15) branch.  
> This branch contains the setup prior to upgrading to Next 16 and the React Compiler.

> Looking for the **Next.js 14 + Tailwind CSS v3** version?  
> Check out the [`archive/next14-tailwindv3`](https://github.com/arhamkhnz/next-shadcn-admin-dashboard/tree/archive/next14-tailwindv3) branch.  
> It has a different color theme and is not actively maintained, but I try to keep it updated with major changes.

## Tech Stack

- **Framework**: Next.js 16 (App Router), TypeScript, Tailwind CSS v4
- **UI Components**: Shadcn UI
- **Validation**: Zod
- **Forms & State Management**: React Hook Form, Zustand
- **Tables & Data Handling**: TanStack Table
- **Tooling & DX**: Biome, Husky

## Screens

### Available

- Default Dashboard
- CRM Dashboard
- Finance Dashboard
- Analytics Dashboard
- Productivity Dashboard
- Authentication (4 screens)
- Legacy: Default v1, CRM v1, Finance v1, Analytics v1

### Coming Soon

- E-commerce Dashboard
- Academy Dashboard
- Logistics Dashboard
- Email Page
- Chat Page
- Calendar Page
- Kanban Board
- Invoice Page
- Users Management
- Roles Management

## Colocation File System Architecture

This project follows a **colocation-based architecture** each feature keeps its own pages, components, and logic inside its route folder.  
Shared UI, hooks, and configuration live at the top level, making the codebase modular, scalable, and easier to maintain as the app grows.

For a full breakdown of the structure with examples, see the [Next Colocation Template](https://github.com/arhamkhnz/next-colocation-template).

## Getting Started

You can run this project locally, or deploy it instantly with Vercel.

### Deploy with Vercel

*Deploy your own copy with one click.*

### Run locally

1. **Clone the repository**
	```
	git clone https://github.com/arhamkhnz/next-shadcn-admin-dashboard.git
	```
2. **Navigate into the project**
	```
	cd next-shadcn-admin-dashboard
	```
3. **Install dependencies**
	```
	npm install
	```
4. **Start the development server**
	```
	npm run dev
	```

Your app will be running at [http://localhost:3000](http://localhost:3000/)

### Formatting and Linting

Format, lint, and organize imports

```
npx @biomejs/biome check --write
```

> For more information on available rules, fixes, and CLI options, refer to the [Biome documentation](https://biomejs.dev/).

---

> [!important] Important
> This project is updated frequently. If you’re working from a fork or an older clone, pull the latest changes before syncing. Some updates may include breaking changes.

---

Contributions are welcome. Feel free to open issues, feature requests, or start a discussion.

**Happy Vibe Coding!**