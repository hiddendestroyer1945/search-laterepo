# Latest Repo Searcher

A professional, terminal-based Python tool to search for repositories across GitHub, GitLab, and Bitbucket with a 1-year time filter.
📋 Prerequisites

Before you begin, ensure you have the following installed on your Linux system:

    Python 3

    Git

    python3-venv

🛠️ Installation & Setup

Follow these steps to get the environment ready and run the program:

1. Update System & Install Dependencies

Open your terminal and run:
Bash

sudo apt update
sudo apt install python3 git python3-venv -y

2. Clone the Repository

Clone the project to your local machine:
Bash

git clone https://github.com/hiddendestroyer1945/search-laterepo.git
cd search-laterepo/

3. Set Up the Virtual Environment

To keep your system clean, create and activate a virtual environment:
Bash

# Create the environment
python3 -m venv venv

# Activate the environment
source venv/bin/activate

4. Install Required Packages

Use the requirements.txt file to install the necessary library (requests>=2.31.0):
Bash

pip install -r requirements.txt

💻 Usage

Once the environment is activated, run the program using:
Bash

python3 search-laterepo.py

How to use:

    Enter your keyword: Input the subject or topic you are looking for (e.g., linux-security, automation).

    The program will automatically calculate the date for the past year.

    The results will be displayed in a numbered list with direct links.

To exit the virtual environment when finished:
Bash

deactivate

📖 Platform Reference List

The program searches the following platforms using their official APIs:
Platform	Search Type	Result Limit
GitHub	Public Repositories	Top 10
GitLab	Public Projects	Top 10
Bitbucket	Public Repositories	Top 10
Contributing

Feel free to modify and improve the program. Pull requests are welcome!
License

This program is released under the GNU General Public License v3.0 (GPL-3.0) License (if applicable). If not, you can specify the license or terms of use.
Author

https://github.com/hiddendestroyer1945