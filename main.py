import os
import shutil

def organize_files():
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    
    file_types = {
        "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"],
        "Executables": [".exe", ".msi"],
        "Scripts": [".py", ".bat", ".sh", ".js", ".ts", ".html", ".css", ".php", ".java", ".cpp", ".c", ".cs", ".rb", ".swift", ".go", ".rs", ".lua", ".pl", ".r", ".kt", ".dart"],
        "Documents": [".txt", ".pdf", ".docx", ".xlsx", ".pptx", ".csv", ".odt"],
        "Images": [".jpg", ".png", ".gif", ".bmp", ".jpeg", ".tiff", ".svg", ".webp"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Others": []
    }
    
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)
        
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            
            for category, extensions in file_types.items():
                if file_ext in extensions:
                    category_folder = os.path.join(downloads_folder, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    moved = True
                    break
            
            if not moved:
                other_folder = os.path.join(downloads_folder, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))
    
    print("Files organized successfully in Downloads folder.")

if __name__ == "__main__":
    organize_files()
