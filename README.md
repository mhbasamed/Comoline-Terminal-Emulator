# Comoline Terminal Emulator
Comoline is a Python-based **terminal emulator** that simulates a command-line interface (CLI) for interacting with the file system. It supports basic terminal commands for file management, directory navigation, and more. This emulator is designed to provide a lightweight and customizable terminal-like experience.

### Features of Comoline:
- File system operations (like `pwd`, `ls`, `mkdir`, `cp`, etc.)
- Output redirection (`>` and `>>` for overwriting and appending output to files)
- Command history tracking
- Customizable terminal-like interface with ASCII art and color-coded output

### Installation:
1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/mhbasamed/ComolineTerminal.git
   ```

2. **Create and Activate Virtual Environment**:  
   For Windows:  
   ```bash
   .\venv\Scripts\activate
   ```  
   For macOS/Linux:  
   ```bash
   source venv/bin/activate
   ```

3. **Install Dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Comoline**:  
   ```bash
   python comoline.py
   ```

### Command Examples:
- `pwd`: Print working directory
- `ls`: List files and directories
- `mkdir [directory]`: Create a directory
- `cp [source] [destination]`: Copy a file
- `mv [source] [destination]`: Move a file
- `history`: Show command history

