%define pypi_name sshtunnel

%def_without check

Name:    python3-module-%{pypi_name}
Version: 0.4.0
Release: alt1

Summary: Pure python SSH tunnels
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/sshtunnel/
VCS:     https://github.com/pahaz/sshtunnel

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module postgresql-test-rpm-macros
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup
# Remove the python shebang from non-executable files.
sed -i '1{\@^#!/usr/bin/env python@d}' sshtunnel.py

# Update tests to import the built-in mock.
sed -i 's/^import mock/from unittest import mock/' tests/*.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest


%files
%doc README.rst
%python3_sitelibdir/sshtunnel.py
%python3_sitelibdir/sshtunnel-%version.dist-info

%changelog
* Thu Oct 12 2023 Danilkin Danila <danild@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus
