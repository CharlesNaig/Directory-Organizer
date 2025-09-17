import os
import shutil
import pygame
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import sys
from datetime import datetime

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BG_COLOR = (30, 30, 40)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER_COLOR = (100, 160, 210)
TEXT_COLOR = (255, 255, 255)
SUCCESS_COLOR = (50, 205, 50)
ERROR_COLOR = (220, 20, 60)

# File categories with comprehensive formats
FILE_CATEGORIES = {
    'Images': {
        'folder': 'Images',
        'extensions': ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.ico', '.tiff', 
                      '.tif', '.webp', '.raw', '.heif', '.heic', '.psd', '.ai', '.eps',
                      '.xcf', '.cdr', '.wmf', '.emf', '.dng', '.cr2', '.nef', '.orf',
                      '.sr2', '.arw', '.rw2', '.dds', '.tga', '.pcx', '.pbm', '.pgm',
                      '.ppm', '.pnm', '.mng', '.apng', '.jp2', '.j2k', '.jpf', '.jpx',
                      '.jpm', '.mj2', '.svgz', '.cgm', '.pat', '.gbr', '.gih', '.ora']
    },
    'Videos': {
        'folder': 'Videos',
        'extensions': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v',
                      '.mpg', '.mpeg', '.3gp', '.3g2', '.f4v', '.f4p', '.f4a', '.f4b',
                      '.vob', '.ogv', '.ogg', '.drc', '.gif', '.gifv', '.mng', '.qt',
                      '.yuv', '.rm', '.rmvb', '.asf', '.amv', '.m4p', '.svi', '.mxf',
                      '.roq', '.nsv', '.ts', '.m2ts', '.mts', '.dvr-ms', '.wtv', '.h264',
                      '.h265', '.hevc', '.av1', '.divx', '.xvid', '.vp8', '.vp9']
    },
    'Audio': {
        'folder': 'Audio',
        'extensions': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.opus',
                      '.ape', '.alac', '.dts', '.ac3', '.amr', '.au', '.aiff', '.aif',
                      '.aifc', '.caf', '.m4b', '.m4r', '.mmf', '.mpc', '.msv', '.nmf',
                      '.oga', '.mogg', '.ra', '.ram', '.raw', '.rex', '.rf64', '.sln',
                      '.tta', '.voc', '.vox', '.wv', '.webm', '.8svx', '.cda', '.dsf',
                      '.dff', '.mid', '.midi', '.kar', '.s3m', '.xm', '.it', '.mod']
    },
    'Documents': {
        'folder': 'Documents',
        'extensions': ['.pdf', '.doc', '.docx', '.txt', '.odt', '.xls', '.xlsx', '.ppt',
                      '.pptx', '.csv', '.rtf', '.tex', '.ods', '.odp', '.odg', '.odf',
                      '.odb', '.odm', '.ott', '.ots', '.otp', '.otg', '.otf', '.oti',
                      '.oth', '.fodt', '.fods', '.fodp', '.fodg', '.pages', '.numbers',
                      '.key', '.wpd', '.wps', '.xlr', '.xlt', '.xltx', '.xlsm', '.xlsb',
                      '.xltm', '.dotx', '.dotm', '.docm', '.dot', '.wri', '.wpt', '.lwp',
                      '.hwp', '.sxw', '.sxc', '.sxi', '.sxd', '.stw', '.stc', '.sti',
                      '.std', '.sgml', '.xml', '.xsl', '.xslt', '.mml', '.dbk']
    },
    'Archives': {
        'folder': 'Archives',
        'extensions': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.z', '.lz',
                      '.lzma', '.lzo', '.rz', '.sz', '.dz', '.zst', '.lz4', '.cab',
                      '.iso', '.dmg', '.img', '.vcd', '.vhd', '.vhdx', '.vmdk', '.wim',
                      '.swm', '.esd', '.deb', '.rpm', '.msi', '.pkg', '.mpkg', '.appx',
                      '.appxbundle', '.snap', '.flatpak', '.jar', '.war', '.ear', '.sar',
                      '.tgz', '.tbz', '.tbz2', '.tlz', '.txz', '.tzst', '.tar.gz',
                      '.tar.bz2', '.tar.xz', '.tar.lz', '.tar.lzma', '.tar.Z', '.arj',
                      '.lzh', '.ace', '.uue', '.bz', '.rz', '.7z.001', '.zipx', '.sit',
                      '.sitx', '.sea', '.sqx', '.pea', '.rar5', '.zz', '.par', '.par2']
    },
    'Programs': {
        'folder': 'Programs',
        'extensions': ['.exe', '.msi', '.app', '.deb', '.rpm', '.dmg', '.pkg', '.run',
                      '.sh', '.bat', '.cmd', '.com', '.ps1', '.vbs', '.js', '.jar',
                      '.air', '.appimage', '.apk', '.ipa', '.xap', '.xpi', '.crx',
                      '.gadget', '.scr', '.hta', '.cpl', '.msc', '.inf', '.ins',
                      '.inx', '.isu', '.job', '.jse', '.lnk', '.msh', '.msh1', '.msh2',
                      '.mshxml', '.msh1xml', '.msh2xml', '.paf', '.pif', '.prg', '.reg',
                      '.rgs', '.sct', '.shb', '.shs', '.u3p', '.vb', '.vbe', '.vbscript',
                      '.ws', '.wsf', '.wsh', '.xbap', '.ahk', '.applescript', '.as',
                      '.awk', '.cgi', '.pl', '.py', '.rb', '.tcl', '.dll', '.so', '.dylib']
    },
    'Code': {
        'folder': 'Code',
        'extensions': ['.py', '.java', '.cpp', '.c', '.h', '.hpp', '.cs', '.php', '.rb',
                      '.go', '.rs', '.swift', '.kt', '.scala', '.r', '.m', '.mm', '.cc',
                      '.cxx', '.hxx', '.hh', '.cp', '.c++', '.h++', '.tcc', '.ino',
                      '.sql', '.html', '.htm', '.css', '.scss', '.sass', '.less', '.js',
                      '.jsx', '.ts', '.tsx', '.vue', '.svelte', '.json', '.yaml', '.yml',
                      '.toml', '.ini', '.cfg', '.conf', '.properties', '.gradle', '.maven',
                      '.ant', '.makefile', '.cmake', '.dockerfile', '.jenkinsfile', '.tf',
                      '.hcl', '.nix', '.vim', '.emacs', '.atom', '.sublime', '.vscode',
                      '.gitignore', '.gitattributes', '.editorconfig', '.prettierrc',
                      '.eslintrc', '.babelrc', '.webpack', '.cargo', '.cabal', '.stack',
                      '.gemfile', '.podfile', '.pubspec', '.package', '.lock', '.sum',
                      '.mod', '.nimble', '.julia', '.dart', '.elm', '.erl', '.ex', '.exs',
                      '.fs', '.fsx', '.fsi', '.ml', '.mli', '.pas', '.pp', '.lpr', '.dfm',
                      '.clj', '.cljs', '.cljc', '.edn', '.lua', '.p', '.pl', '.pm', '.t',
                      '.pod', '.psgi', '.raku', '.rakumod', '.rakutest', '.nqp', '.6pl',
                      '.6pm', '.p6', '.p6l', '.p6m', '.pl6', '.pm6', '.rkt', '.rktd',
                      '.rktl', '.scrbl', '.scm', '.ss', '.lisp', '.lsp', '.cl', '.fasl',
                      '.sld', '.el', '.elc', '.hy', '.asm', '.s', '.nasm', '.masm', '.tasm']
    },
    'Ebooks': {
        'folder': 'Ebooks',
        'extensions': ['.epub', '.mobi', '.azw', '.azw3', '.azw4', '.kfx', '.kf8', '.fb2',
                      '.fb2.zip', '.lit', '.pdb', '.pml', '.prc', '.tcr', '.snb', '.rb',
                      '.txtz', '.tpz', '.opf', '.ncx', '.cbr', '.cbz', '.cbt', '.cba',
                      '.cb7', '.djvu', '.djv', '.ibooks', '.oxps', '.xps', '.comic']
    },
    'Data': {
        'folder': 'Data',
        'extensions': ['.json', '.xml', '.csv', '.tsv', '.sql', '.db', '.sqlite', '.mdb',
                      '.accdb', '.dbf', '.pdb', '.ndf', '.frm', '.myd', '.myi', '.ibd',
                      '.odb', '.fdb', '.gdb', '.bak', '.dmp', '.sav', '.rdata', '.rds',
                      '.feather', '.parquet', '.orc', '.avro', '.pickle', '.pkl', '.hdf',
                      '.hdf5', '.h5', '.mat', '.nc', '.netcdf', '.fits', '.grib', '.grib2',
                      '.shp', '.shx', '.dbf', '.prj', '.kml', '.kmz', '.gpx', '.osm',
                      '.geojson', '.topojson', '.msgpack', '.bson', '.protobuf', '.arrow']
    },
    'Fonts': {
        'folder': 'Fonts',
        'extensions': ['.ttf', '.otf', '.woff', '.woff2', '.eot', '.fon', '.fnt', '.vlw',
                      '.sfd', '.pfa', '.pfb', '.pfm', '.afm', '.tfm', '.bdf', '.snf',
                      '.pcf', '.pmf', '.gdr', '.gdf', '.psf', '.vnf', '.chr', '.vfb']
    },
    '3D_Models': {
        'folder': '3D_Models',
        'extensions': ['.obj', '.fbx', '.dae', '.3ds', '.blend', '.stl', '.ply', '.gltf',
                      '.glb', '.usdz', '.usd', '.usda', '.usdc', '.abc', '.x3d', '.x3db',
                      '.x3dv', '.x3dvz', '.x3dbz', '.wrl', '.vrml', '.bvh', '.ase', '.dxf',
                      '.nff', '.off', '.raw', '.ter', '.mdl', '.md2', '.md3', '.md5',
                      '.mdc', '.ndo', '.tri', '.wings', '.q3d', '.q3o', '.q3s', '.qc',
                      '.cfg', '.csm', '.mdx', '.mdlx', '.smd', '.vta', '.vtf', '.vtx',
                      '.dmx', '.dx90', '.ani', '.scn', '.xgl', '.zgl', '.ac', '.acc',
                      '.amt', '.bsp', '.e57', '.ms3d', '.lwo', '.lws', '.lxo', '.jas',
                      '.jt', '.ogre', '.mesh', '.skeleton', '.material', '.pk3', '.msh']
    }
}

class FileOrganizer:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Desktop File Organizer")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        
        self.selected_directory = None
        self.status_message = ""
        self.status_color = TEXT_COLOR
        self.organize_complete = False
        self.files_moved = {}
        
        # Button definitions
        self.buttons = {
            'select': pygame.Rect(250, 200, 300, 60),
            'organize': pygame.Rect(250, 280, 300, 60),
            'exit': pygame.Rect(250, 360, 300, 60)
        }
        
        self.button_states = {
            'select': False,
            'organize': False,
            'exit': False
        }
    
    def draw_button(self, rect, text, hover=False):
        color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
        pygame.draw.rect(self.screen, color, rect, border_radius=10)
        pygame.draw.rect(self.screen, TEXT_COLOR, rect, 3, border_radius=10)
        
        text_surface = self.font_medium.render(text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)
    
    def select_directory(self):
        root = tk.Tk()
        root.withdraw()
        root.lift()
        root.attributes('-topmost', True)
        
        directory = filedialog.askdirectory(
            title="Select Directory to Organize",
            initialdir=os.path.expanduser("~/Desktop")
        )
        
        root.destroy()
        
        if directory:
            self.selected_directory = directory
            self.status_message = f"Selected: {os.path.basename(directory)}"
            self.status_color = SUCCESS_COLOR
        else:
            self.status_message = "No directory selected"
            self.status_color = ERROR_COLOR
    
    def organize_files(self):
        if not self.selected_directory:
            self.status_message = "Please select a directory first!"
            self.status_color = ERROR_COLOR
            return
        
        try:
            self.files_moved = {category: 0 for category in FILE_CATEGORIES}
            others_moved = 0
            
            # Create timestamp for backup reference
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Get all files in the directory
            for item in os.listdir(self.selected_directory):
                item_path = os.path.join(self.selected_directory, item)
                
                # Skip if it's a directory
                if os.path.isdir(item_path):
                    continue
                
                # Get file extension
                _, extension = os.path.splitext(item)
                extension = extension.lower()
                
                # Find matching category
                moved = False
                for category, info in FILE_CATEGORIES.items():
                    if extension in info['extensions']:
                        # Create category folder if it doesn't exist
                        category_folder = os.path.join(self.selected_directory, info['folder'])
                        os.makedirs(category_folder, exist_ok=True)
                        
                        # Move file to category folder
                        new_path = os.path.join(category_folder, item)
                        
                        # Handle duplicate filenames
                        if os.path.exists(new_path):
                            base, ext = os.path.splitext(item)
                            counter = 1
                            while os.path.exists(new_path):
                                new_name = f"{base}_{counter}{ext}"
                                new_path = os.path.join(category_folder, new_name)
                                counter += 1
                        
                        shutil.move(item_path, new_path)
                        self.files_moved[category] += 1
                        moved = True
                        break
                
                # If no category matched, move to Others folder
                if not moved and extension:  # Only move files with extensions
                    others_folder = os.path.join(self.selected_directory, 'Others')
                    os.makedirs(others_folder, exist_ok=True)
                    
                    new_path = os.path.join(others_folder, item)
                    
                    # Handle duplicate filenames
                    if os.path.exists(new_path):
                        base, ext = os.path.splitext(item)
                        counter = 1
                        while os.path.exists(new_path):
                            new_name = f"{base}_{counter}{ext}"
                            new_path = os.path.join(others_folder, new_name)
                            counter += 1
                    
                    shutil.move(item_path, new_path)
                    others_moved += 1
            
            # Update status
            total_moved = sum(self.files_moved.values()) + others_moved
            if total_moved > 0:
                self.status_message = f"Successfully organized {total_moved} files!"
                self.status_color = SUCCESS_COLOR
                self.organize_complete = True
            else:
                self.status_message = "No files to organize"
                self.status_color = TEXT_COLOR
            
        except Exception as e:
            self.status_message = f"Error: {str(e)}"
            self.status_color = ERROR_COLOR
    
    def draw(self):
        self.screen.fill(BG_COLOR)
        
        # Draw title
        title_text = self.font_large.render("File Organizer", True, TEXT_COLOR)
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, 80))
        self.screen.blit(title_text, title_rect)
        
        # Draw subtitle
        subtitle_text = self.font_small.render("Organize your desktop files into categories", True, TEXT_COLOR)
        subtitle_rect = subtitle_text.get_rect(center=(WINDOW_WIDTH // 2, 120))
        self.screen.blit(subtitle_text, subtitle_rect)
        
        # Get mouse position for hover effects
        mouse_pos = pygame.mouse.get_pos()
        
        # Draw buttons
        self.draw_button(self.buttons['select'], "Select Directory", 
                        self.buttons['select'].collidepoint(mouse_pos))
        self.draw_button(self.buttons['organize'], "Organize Files", 
                        self.buttons['organize'].collidepoint(mouse_pos))
        self.draw_button(self.buttons['exit'], "Exit", 
                        self.buttons['exit'].collidepoint(mouse_pos))
        
        # Draw selected directory
        if self.selected_directory:
            dir_text = self.font_small.render(f"Directory: {self.selected_directory}", True, TEXT_COLOR)
            dir_rect = dir_text.get_rect(center=(WINDOW_WIDTH // 2, 450))
            self.screen.blit(dir_text, dir_rect)
        
        # Draw status message
        if self.status_message:
            status_text = self.font_small.render(self.status_message, True, self.status_color)
            status_rect = status_text.get_rect(center=(WINDOW_WIDTH // 2, 490))
            self.screen.blit(status_text, status_rect)
        
        # Draw organization results
        if self.organize_complete:
            y_offset = 520
            results_text = self.font_small.render("Files moved:", True, TEXT_COLOR)
            self.screen.blit(results_text, (250, y_offset))
            
            y_offset += 25
            for category, count in self.files_moved.items():
                if count > 0:
                    result_line = f"{FILE_CATEGORIES[category]['folder']}: {count} files"
                    line_text = self.font_small.render(result_line, True, SUCCESS_COLOR)
                    self.screen.blit(line_text, (270, y_offset))
                    y_offset += 20
        
        pygame.display.flip()
    
    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    
                    if self.buttons['select'].collidepoint(mouse_pos):
                        self.select_directory()
                        self.organize_complete = False
                    
                    elif self.buttons['organize'].collidepoint(mouse_pos):
                        self.organize_files()
                    
                    elif self.buttons['exit'].collidepoint(mouse_pos):
                        running = False
            
            self.draw()
            self.clock.tick(30)
        
        pygame.quit()
        sys.exit()

def main():
    organizer = FileOrganizer()
    organizer.run()

if __name__ == "__main__":
    main()