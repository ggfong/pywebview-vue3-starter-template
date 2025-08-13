# pywebview-vue3-starter-template

This is a cross-platform desktop application template built with Python (uv) + Vue.js (Vite).

It uses `pnpm` as a monorepo manager to separate the Python backend and Vue.js frontend into different workspaces.

## Architecture

The project uses a monorepo structure with two core packages:

-   `packages/main`: Python Backend
    -   Uses `uv` for package and virtual environment management.
    -   Uses `pywebview` to create a window and load the frontend page.
    -   Responsible for handling core application logic.
    -   Uses `nuitka` to package the application into an executable for Windows and macOS.
-   `packages/renderer`: Vue.js Frontend
    -   Uses `Vite` for development and building.
    -   Provides the user interface.
    -   The built static files are referenced by the `main` package.

## Prerequisites

Before you begin, ensure you have the following tools installed:

-   [Node.js](https://nodejs.org/) (v18+), it is recommended to use `nvm` or `fnm` for management.
-   [pnpm](https://pnpm.io/installation) (v9+)
-   [Python](https://www.python.org/) (v3.10+)
-   [uv](https://github.com/astral-sh/uv) (Python package manager)

## Installation

1.  **Clone the repository**

    ```bash
    git clone https://github.com/ggfong/pywebview-vue3-starter-template
    cd pywebview-vue3-starter-template
    ```

2.  **Install dependencies**

    This command will install Node.js dependencies for the root directory and all workspaces (including `renderer`).
    The `postinstall` hook will automatically run `pnpm install:main` to install Python dependencies.

    ```bash
    pnpm install
    ```

    If the `postinstall` hook fails, you can manually install the Python dependencies:
    ```bash
    pnpm install:main
    ```

## Development

To run the application in development mode, execute the following command. It will start both the Vite development server and the Python backend simultaneously.

```bash
pnpm dev
```

This will:
-   Start the Vite hot-reloading server in `packages/renderer`.
-   Start the Python application in `packages/main`.

## Building

You can build a production version of the executable for Windows or macOS.

1.  **Build for Windows**

    ```bash
    pnpm build:win
    ```

2.  **Build for macOS**

    ```bash
    pnpm build:mac
    ```

The build process is as follows:
1.  Build the `renderer` package to generate static frontend files in `packages/renderer/dist`.
2.  Compile the Python code in the `main` package using `nuitka`.
3.  Include the build output of the `renderer` (`dist` directory) in the final executable.

The generated files will be located in the `dist` folder in the project root.

## Available Scripts

-   `pnpm dev`: Starts the frontend and backend development servers in parallel.
-   `pnpm dev:renderer`: Starts only the frontend Vite development server.
-   `pnpm dev:main`: Starts only the Python backend application.
-   `pnpm build:renderer`: Builds only the frontend application.
-   `pnpm build:win`: Builds the executable for Windows.
-   `pnpm build:mac`: Builds the application bundle for macOS.
-   `pnpm lint`: Lints the code in all packages.
-   `pnpm lint:fix`: Automatically fixes linting issues in all packages.
-   `pnpm clean`: Removes all files and folders not tracked by Git (use with caution).
-   `pnpm install:main`: Installs Python dependencies in `packages/main` using `uv`.

## Tech Stack

-   **Monorepo**: [pnpm workspaces](https://pnpm.io/workspaces)
-   **Backend**: [Python](https://www.python.org/)
-   **Desktop GUI**: [pywebview](https://pywebview.flowrl.com/)
-   **Python Package Management**: [uv](https://github.com/astral-sh/uv)
-   **Frontend**: [Vue.js 3](https://vuejs.org/)
-   **Frontend Build Tool**: [Vite](https://vitejs.dev/)
-   **Packaging**: [Nuitka](https://nuitka.net/)
-   **Concurrent Tasks**: [concurrently](https://github.com/open-cli/concurrently)
