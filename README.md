# Latest Repo Searcher

A professional, terminal-based Python tool to search for repositories across GitHub, GitLab, and Bitbucket with a 1-year time filter.

## 🚀 Features

-   **Parallel Processing**: Uses `concurrent.futures.ThreadPoolExecutor` for high-speed concurrent searches across GitHub, GitLab, and Bitbucket.
-   **URI Security**: Automatic parameter encoding via `requests` to prevent query injection and malformed URL errors.
-   **Robust Error Handling**: Precise detection of platform-specific errors, including HTTP 403 (Rate Limiting).
-   **Unified CLI**: Supports both interactive mode and command-line arguments for seamless automation.

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your Linux system:

*   **Python 3**
*   **Git**
*   **python3-pip**
*   **python3-venv**

## 🛠️ Installation & Setup

Follow these steps to get the environment ready and run the program:

### 1. Update System & Install Dependencies

Open your terminal and run:
```bash
sudo apt update && sudo apt install git python3 python3-pip python3-venv -y
```

### 2. Clone the Repository

Clone the project to your local machine:
```bash
git clone https://github.com/hiddendestroyer1945/search-laterepo.git
cd search-laterepo/
```

### 3. Set Up the Virtual Environment

To keep your system clean, create and activate a virtual environment:
```bash
# Create the environment
python3 -m venv venv

# Activate the environment
source venv/bin/activate
```

### 4. Install Required Packages

Use the `requirements.txt` file to install necessary libraries:
```bash
pip install -r requirements.txt
```

## 💻 Usage

Once the environment is activated, you can run the program in two ways:

**Interactive Mode:**
```bash
python3 searchlaterepo.py
```

**CLI Argument Mode:**
```bash
python3 searchlaterepo.py "your keyword"
```

## 📖 Platform Reference List

The program searches the following platforms using their official APIs:

| Platform | Search Type | Result Limit |
| :--- | :--- | :--- |
| **GitHub** | Public Repositories | Top 10 |
| **GitLab** | Public Projects | Top 10 |
| **Bitbucket** | Public Repositories | Top 10 |

## License

This program is released under the GNU General Public License v3.0 (GPL-3.0).

## Author

[hiddendestroyer1945](https://github.com/hiddendestroyer1945)
