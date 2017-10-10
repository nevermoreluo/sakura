import platform

if platform.system().lower() == 'darwin':
    from sakura.cpplib_osx import ConHash
else:
    from sakura.cpplib import ConHash
