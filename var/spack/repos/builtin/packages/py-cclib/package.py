# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCclib(PythonPackage):
    """Open source library for parsing and interpreting the results of
    computational chemistry packages"""

    homepage = "https://cclib.github.io/"

    version(
        "1.7.2",
        url = "https://github.com/cclib/cclib/releases/download/v1.7.2/cclib-1.7.2.tar.gz",
        sha256="aa1a2b2e26f7debbd98605d471d4dafe8cacf42db76b961df79b8cb29b2f3cdc"
    version(
        "1.5.post1",
        sha256="c2bf043432ab8df461d61b4289d0eb869fe134eee545ea5a78f8dea14b392f47",
        url="https://github.com/cclib/cclib/releases/download/v1.5/cclib-1.5.post1.tar.gz",
    )

    # pip silently replaces distutils with setuptools
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy@1.5:", type=("build", "run"))
    depends_on("periodictable", type=("build", "run"),when="@1.7.2:")
    depends_on("scipy@1.2.0:", type=("build", "run"),when="@1.7.2:")

    # maintainers
    maintainers=["amandadumi","berquist"]