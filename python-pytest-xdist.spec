%define oname pytest_xdist
%bcond tests 1

Name:		python-pytest-xdist
Version:	3.8.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-xdist/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	pytest xdist plugin for distributed testing, most importantly across multiple CPUs
URL:		https://pypi.org/project/pytest-xdist/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(execnet) >= 1.1
BuildRequires:	python%{pyver}dist(filelock)
BuildRequires:	python%{pyver}dist(setproctitle)
BuildRequires:	python%{pyver}dist(psutil) >= 3
BuildRequires:	python%{pyver}dist(pytest) >= 6
BuildRequires:	python%{pyver}dist(pytest-forked)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
Requires:		python%{pyver}dist(execnet) >= 2.1
Requires:		python%{pyver}dist(pytest) >= 7.0.0
Recommends:		python%{pyver}dist(psutil) >= 3.0
Recommends:		python%{pyver}dist(filelock)
Recommends:		python%{pyver}dist(setproctitle)

# Update baipp to 2.14 #1266 https://github.com/pytest-dev/pytest-xdist/pull/1266/commits/46084729fd2785c626d8c4add0b5e695eb4fdde9
# Fix CI for pytest 9.0+ #1272 https://github.com/pytest-dev/pytest-xdist/pull/1272
%patchlist
https://github.com/pytest-dev/pytest-xdist/pull/1266/commits/46084729fd2785c626d8c4add0b5e695eb4fdde9.patch#/%{name}-3.8.0-update-biapp.patch
https://github.com/pytest-dev/pytest-xdist/pull/1272.patch#/%{name}-3.8.0-fix-for-pytest-9.0+.patch

%description
The pytest-xdist plugin extends pytest with new test execution
modes, the most used being distributing tests across multiple
CPUs to speed up test execution.

%prep
%autosetup -p1 -n %{oname}-%{version}
sed -i 's/\r//' README.rst

%if %{with tests}
%check
export CI=true
export PYTHONPATH=%{buildroot}%{python_sitearch}:%{python_sitearch}:%{buildroot}%{python_sitelib}:%{python_sitelib}
pytest
%endif

%files
%doc README.rst
%license LICENSE
%{py_sitedir}/xdist
%{py_sitedir}/%{oname}-%{version}.dist-info
