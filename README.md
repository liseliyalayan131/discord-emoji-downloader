# Discord Emoji Downloader

A Python script to download all emojis from a specified Discord server and save them in a ZIP file. The script separates PNG and GIF emojis into different directories before zipping them and cleans up the directories after zipping.

## Prerequisites

- Python 3.7 or higher
- `discord.py==1.7.3`
- `requests`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/YourUsername/Discord-Emoji-Downloader.git
    cd Discord-Emoji-Downloader
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```sh
    python main.py
    ```

2. When prompted, enter your Discord token and the Guild ID (Server ID).

## Files

- `main.py`: The main script to download and zip emojis.
- `requirements.txt`: A file listing the required Python packages.
- `start.bat`: A batch file to start the script (optional).
