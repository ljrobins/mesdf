from distutils.core import setup
from pybind11.setup_helpers import Pybind11Extension
import eigency
import platform
from glob import glob

opt_arg = "-O3"
std_arg = "-std=c++17"
if platform.system() == "Windows":
    std_arg = "/std:c++17"
    opt_arg = "/O2"

ext_modules = [
    Pybind11Extension(
        name="mesdf",
        sources=[*glob("src/*.cpp")],
        include_dirs=[
            "include/sdf",
            "include/sdf/internal",
            *tuple(eigency.get_includes()),
        ],
        extra_compile_args=[std_arg, opt_arg],
    ),
]

setup(name="mesdf", ext_modules=ext_modules)
