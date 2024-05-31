class TerminalColor:
    # 代表的な色
    INFO_BLUE = '\033[94m'
    INFO_GREEN = '\033[92m'
    WARN = '\033[93m'
    ERR = '\033[91m'

    # フォントスタイル
    MARKER = '\033[7m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # 末尾制御
    _END = '\033[0m'