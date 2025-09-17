
# Directory Organizer with Pygame GUI

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://example.com/build)
[![Coverage Status](https://img.shields.io/badge/coverage-90%25-brightgreen.svg)](https://example.com/coverage)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://example.com/dependencies)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful desktop application that organizes files in a directory using a graphical user interface built with Pygame. It automatically categorizes files based on their extensions, helping you maintain a clean and organized file system.

## Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage](#usage)
- [File Organization Structure](#file-organization-structure)
- [Categories](#categories)
- [How It Works](#how-it-works)
- [Safety Features](#safety-features)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)
- [Version History](#version-history)
- [Acknowledgments](#acknowledgments)

## Features

- **User-Friendly GUI**: Simple and intuitive Pygame interface for easy interaction.
- **Smart Categorization**: Automatically sorts files into predefined categories based on their file extensions.
- **Comprehensive File Support**: Recognizes a wide range of file extensions (400+).
- **Duplicate Handling**: Automatically renames duplicate files to prevent overwrites and data loss.
- **Visual Feedback**: Provides real-time status updates and clear results during the organization process.
- **Cross-Platform Compatibility**: Works seamlessly on Windows, macOS, and Linux operating systems.

## Quick Start

1.  Install the application following the [Installation](#installation) instructions.
2.  Run the application using the command: `python main.py`.
3.  Click "Select Directory" to choose the directory you want to organize.
4.  Click "Organize Files" to start the automatic file categorization process.

## Installation

### Prerequisites

- Python 3.7 or higher is required.  Check your version with `python --version`.
- pip (Python package installer) should be installed.  Most Python installations include pip.

### Steps

1. Clone the repository to your local machine:

bash
python main.py
2.  The Pygame window will appear, presenting you with three options:
    -   **Select Directory**: Allows you to choose the directory you wish to organize.
    -   **Organize Files**: Initiates the file organization process.
    -   **Exit**: Closes the application.

3.  Click the "Select Directory" button and use the file dialog to navigate to and select the target directory.

4.  Click the "Organize Files" button to begin the automated file sorting process.

5.  The application will display status messages, the number of files moved to each category, and any errors encountered during the process.

## File Organization Structure

After running the organizer, your selected directory will be structured as follows:

1.  **Images**: Includes files with extensions like PNG, JPG, GIF, BMP, SVG, PSD, and RAW.
2.  **Videos**: Includes video files with extensions such as MP4, AVI, MKV, MOV, WMV, and FLV.
3.  **Audio**: Includes audio files with extensions like MP3, WAV, FLAC, AAC, and OGG.
4.  **Documents**: Includes documents with extensions like PDF, DOC, DOCX, TXT, Excel, and PPT.
5.  **Archives**: Includes archive files with extensions like ZIP, RAR, 7Z, TAR, and ISO.
6.  **Programs**: Includes executable files and installers with extensions like EXE, MSI, and APP.
7.  **Code**: Includes source code files and configuration files.
8.  **Ebooks**: Includes electronic books with extensions like EPUB, MOBI and AZW.
9.  **Data**: Includes data files with extensions like JSON, XML, and CSV.
10. **Fonts**: Includes font files with extensions like TTF, OTF, and WOFF.
11. **3D_Models**: Includes 3D model files with extensions like OBJ, FBX, STL, and BLEND.
12. **Others**: Includes files with unrecognized extensions.

## How It Works

The directory organizer operates through the following steps:

1.  **Directory Scanning**: Scans the selected directory to identify all files.
2.  **File Type Identification**: Determines the type of each file based on its extension.
3.  **Category Folder Creation**: Creates category folders if they do not already exist.
4.  **File Relocation**: Moves each file to its corresponding category folder.
5.  **Duplicate Handling**: Renames duplicate files by appending a number to the filename to avoid overwriting.
6.  **Unrecognized Files**: Places files with unrecognized extensions into the "Others" folder.
7.  **Subdirectory Preservation**: Ignores subdirectories, ensuring they remain untouched.

## Safety Features

-   **No Data Loss**: Files are moved, not deleted, ensuring no accidental data loss.
-   **Duplicate Protection**: Existing files are never overwritten, preventing any data corruption.
-   **Directory Preservation**: Only files are moved; folders remain untouched, maintaining the directory structure.
-   **Error Handling**: Graceful handling of permission issues and other potential errors.

## Customization

The file categories can be customized by modifying the `FILE_CATEGORIES` dictionary in the main script (`main.py`). You can add or remove extensions as needed to suit your specific requirements.

Example:

python
FILE_CATEGORIES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".csv"],
    # Add or modify categories as needed
}
1.  **Permission Denied Error**: If you encounter a "Permission Denied" error, try running the application as an administrator (Windows) or using `sudo` (macOS/Linux).
2.  **Files Not Being Moved**: Ensure the selected directory contains files and not just folders.  Also, verify that the file extensions are recognized by the application.
3.  **GUI Window Not Appearing**: Make sure that Pygame is installed correctly.  Try reinstalling it using `pip install pygame`.
4.  **Directory Selection Canceled**: The file selection dialog might appear behind other windows. Minimize other applications to locate it.

### System Requirements

-   **RAM**: 512MB minimum
-   **Storage**: Minimal (a few MB for the application)
-   **Display**: 800x600 resolution minimum
-   **Operating System**: Windows 10+, macOS 10.12+, Ubuntu 18.04+

## Contributing

Contributions are welcome! Feel free to submit issues, fork the repository, and create pull requests for any improvements or bug fixes.

> Please follow the contribution guidelines outlined in `CONTRIBUTING.md`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Support

For any issues or questions, please refer to the documentation or create an issue in the repository.

## Version History

-   **v1.0.0** - Initial release with 12 categories and support for 400+ file formats.

## Acknowledgments

-   Built with Python and Pygame.
-   Uses `tkinter` for native file dialogs.
-   Inspired by the need for efficient desktop organization.

---

**Note**: It is always recommended to back up important files before running any file organization tool. While this application is designed to be safe, maintaining backups is a good practice.
