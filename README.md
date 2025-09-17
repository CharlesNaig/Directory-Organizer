# File Organizer with Pygame GUI

A powerful desktop file organizer with a graphical user interface built using Pygame. This application helps you organize files in any directory by automatically categorizing them into appropriate folders based on their file extensions.

## Features

- **User-Friendly GUI**: Simple and intuitive Pygame interface
- **Smart Categorization**: Automatically organizes files into 12+ categories
- **Comprehensive File Support**: Recognizes 400+ file extensions
- **Duplicate Handling**: Automatically renames duplicates to prevent overwrites
- **Visual Feedback**: Real-time status updates and results display
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Categories

The organizer sorts files into the following categories:

1. **Images** - PNG, JPG, GIF, BMP, SVG, PSD, RAW formats, and more
2. **Videos** - MP4, AVI, MKV, MOV, WMV, FLV, and various codecs
3. **Audio** - MP3, WAV, FLAC, AAC, OGG, and music formats
4. **Documents** - PDF, DOC, DOCX, TXT, Excel, PowerPoint, and office formats
5. **Archives** - ZIP, RAR, 7Z, TAR, ISO, and compression formats
6. **Programs** - EXE, MSI, APP, installers, and scripts
7. **Code** - Programming languages, config files, and development files
8. **Ebooks** - EPUB, MOBI, AZW, PDF books, and comic formats
9. **Data** - JSON, XML, CSV, databases, and data science formats
10. **Fonts** - TTF, OTF, WOFF, and typography files
11. **3D_Models** - OBJ, FBX, STL, BLEND, and 3D formats
12. **Others** - Unrecognized files with extensions

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Clone or download this repository
2. Navigate to the project directory
3. Install required packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:

```bash
python main.py
```

2. The Pygame window will open with three buttons:
   - **Select Directory**: Choose the folder you want to organize
   - **Organize Files**: Start the organization process
   - **Exit**: Close the application

3. Click "Select Directory" and browse to the folder you want to organize

4. Click "Organize Files" to automatically sort all files into categorized folders

5. The application will display:
   - Status messages
   - Number of files moved to each category
   - Any errors encountered

## How It Works

The organizer:
1. Scans the selected directory for all files
2. Identifies file types by their extensions
3. Creates category folders if they don't exist
4. Moves files to their appropriate category folders
5. Handles duplicate filenames by appending numbers
6. Files with unrecognized extensions go to "Others" folder
7. Subdirectories are not affected

## File Organization Structure

After organizing, your directory will look like:

```
Selected_Directory/
├── Images/
│   ├── photo1.jpg
│   ├── screenshot.png
│   └── logo.svg
├── Videos/
│   ├── movie.mp4
│   └── clip.avi
├── Documents/
│   ├── report.pdf
│   └── notes.txt
├── Audio/
│   └── song.mp3
├── Archives/
│   └── backup.zip
├── Programs/
│   └── installer.exe
├── Code/
│   └── script.py
└── Others/
    └── unknown.xyz
```

## Safety Features

- **No Data Loss**: Files are moved, not deleted
- **Duplicate Protection**: Existing files are never overwritten
- **Directory Preservation**: Only files are moved, folders remain untouched
- **Error Handling**: Graceful handling of permission issues

## Customization

You can customize file categories by modifying the `FILE_CATEGORIES` dictionary in the main script. Add or remove extensions as needed for your specific use case.

## Troubleshooting

### Common Issues

1. **Permission Denied**: Run as administrator/sudo if organizing system directories
2. **No Files Moved**: Check if the directory contains files (not just folders)
3. **Window Not Appearing**: Ensure Pygame is properly installed
4. **Directory Selection Canceled**: The file dialog may appear behind other windows

### System Requirements

- **RAM**: 512MB minimum
- **Storage**: Minimal (few MB for the application)
- **Display**: 800x600 resolution minimum
- **OS**: Windows 10+, macOS 10.12+, Ubuntu 18.04+

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available for personal and commercial use.

## Support

For issues or questions, please check the documentation or create an issue in the repository.

## Version History

- **v1.0.0** - Initial release with 12 categories and 400+ file format support

## Acknowledgments

- Built with Python and Pygame
- Uses tkinter for native file dialogs
- Inspired by desktop organization needs

---

**Note**: Always backup important files before organizing. While the application is designed to be safe, it's good practice to maintain backups.