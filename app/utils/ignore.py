IGNORED_FILES = {
    ".gitignore",
    "package-lock.json",
    "yarn.lock",
    ".DS_Store",
    ".ipynb_checkpoints",
    "*.pyc",
    "*.pyo",
    "*.o",
    "*.class",
    "*.dll",
    "*.so",
    "*.dylib",
    "*.exe",
    "*.zip",
    "*.tar",
    "*.gz",
    "*.rar",
    "*.7z",
    "*.pdf",
    "*.docx",
    "*.pptx",
    "*.xlsx",
    "*.png",
    "*.jpg",
    "*.jpeg",
    "*.gif",
    "*.bmp",
    "*.ico",
    "*.svg",
    "*.mp3",
    "*.wav",
    "*.mp4",
    "*.avi",
    "*.mov",
    "*.wmv"
}

IGNORED_FOLDERS = {
    ".git",
    "__pycache__",
    ".vscode",
    ".idea",
    ".venv",
    ".gitattributes",
    ".gitkeep",
    ".dockerignore",
    "node_modules",
    "venv",
    "build",
    "dist",
    "out",
    "output",
    "target",
    "images",
    "videos",
    "docs",
    "logs",
    "tmp",
    "temp",
    "backup",
    "cache",
    "test",
    "tests"
}

# Combine all ignored patterns into a single set for easy lookup
IGNORED_PATTERNS = IGNORED_FILES.union(IGNORED_FOLDERS)
