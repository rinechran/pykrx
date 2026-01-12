import platform
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import importlib.resources as resources
from . import bond
from . import stock
from pydatakrx.website.comm.webio import set_krx_login_info

os = platform.system()

if os == "Darwin":
    plt.rc('font', family="AppleGothic")

else:
    with resources.path('pydatakrx', 'NanumBarunGothic.ttf') as font_path:
        fe = fm.FontEntry(
            fname=str(font_path),
            name='NanumBarunGothic'
        )
        fm.fontManager.ttflist.insert(0, fe)
        plt.rc('font', family=fe.name)

plt.rcParams['axes.unicode_minus'] = False

__all__ = [
    'bond',
    'stock',
    'set_krx_login_info'
]