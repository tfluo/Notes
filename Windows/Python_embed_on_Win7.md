1. 解压python-3.8.10-embed-amd64.zip
2. 安装2个Windows补丁：KB2999226、KB3118401
    1. KB2999226微软下载链接：https://support.microsoft.com/en-us/help/2999226/update-for-universal-c-runtime-in-windows
    2. KB3118401微软下载链接：https://support.microsoft.com/en-us/help/3118401/update-for-universal-c-runtime-in-windows`
3. 修改python38._pth，去掉import site前的#
4. 修改环境变量：SET PATH=%PATH%;%PATH_TO_PYTHON%;%PATH_TO_PYTHON_SCRIPTS%
5. 安装pip：下载get-pip.py：https://bootstrap.pypa.io/get-pip.py
6. 安装和使用pyinstaller：
    1. 修改python38._pth：注释掉python38.zip
    2. 加上一行 Lib\\site-packages
    3. 解压python38.zip到Lib\site-packages
    4. 下载future-0.18.2.zip
    5. 解压future-0.18.2.zip，修改setup.py：在import src.future之前加上sys.path.append('')
    6. 安装future-0.18.2：python setup.py install
    7. 安装pyinstaller：pip install pyinstaller
    8. 打包：pyinstaller -F xxx.py --clean，可执行文件在 dist 目录下
7. 其他待补充...`
