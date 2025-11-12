@echo off
echo Test1
python vfs_emulator.py --vfs_path ./test_vfs --log_path ./test1.xml --script_path test1.bat

echo Test2
python vfs_emulator.py --vfs_path ./vfs2 --log_path ./test2.xml --script_path test2.bat

echo Test3
python vfs_emulator.py --vfs_path ./default_vfs

pause
