# pyinstaller.spec

# Import necessary modules from PyInstaller
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# Collect all submodules and data files from your Python module
hidden_imports = collect_submodules('utils')
datas = collect_data_files('utils')

# Analysis block
a = Analysis(
    ['app.py'],  # Entry point of your application
    pathex=['utils'],  # Path to search for imports
    binaries=[],  # List of additional binary files to include
    datas=datas,  # Data files to include
    hiddenimports=hidden_imports,  # Hidden imports to include
    hookspath=[],  # Custom hooks
    runtime_hooks=[],  # Runtime hooks
    excludes=[],  # List of module names to exclude
    win_no_prefer_redirects=False,  # Windows specific option
    win_private_assemblies=False,  # Windows specific option
    cipher=None,  # Cipher for encrypting Python bytecode
    noarchive=False  # Whether to bundle everything in a single archive
)

# PyZ block
pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=None
)

# EXE block
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='app',  # Name of the executable
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # Use UPX to compress the executable
    upx_exclude=[],  # Files to exclude from UPX compression
    runtime_tmpdir=None,
    console=True  # Whether to show a console window
)

# Collect block
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app'
)
