from py2exe import freeze

freeze(
    windows=['execute1.py', 'execute2.py', 'execute3.py'],
    zipfile=None,
    options={
        "bundle_files":1
    }
)