# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Pages.py'],
             pathex=['C:\\Users\\dpmar\\Desktop\\Homework\\Databases\\FolderForFinalProject'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

a.datas +=  [('many_menus.png','C:\\Users\\dpmar\\Desktop\\Homework\\Databases\\FolderForFinalProject\\many_menus.png', "DATA")]
a.datas +=  [('pepper.ico','C:\\Users\\dpmar\\Desktop\\Homework\\Databases\\FolderForFinalProject\\pepper.ico', "DATA")]

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Pages',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
