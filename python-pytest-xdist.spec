Name:		python-pytest-xdist
Version:	3.6.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-xdist/pytest_xdist-%{version}.tar.gz
Summary:	pytest xdist plugin for distributed testing, most importantly across multiple CPUs
URL:		https://pypi.org/project/pytest-xdist/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python%{pyver}dist(execnet) >= 1.1
BuildRequires:	python%{pyver}dist(filelock)
BuildRequires:	python%{pyver}dist(psutil) >= 3
BuildRequires:	python%{pyver}dist(pytest) >= 6
BuildRequires:	python%{pyver}dist(pytest-forked)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
Requires:	python%{pyver}dist(execnet) >= 1.1
BuildSystem:	python
BuildArch:	noarch

%description
pytest xdist plugin for distributed testing, most importantly across multiple CPUs

%prep
%autosetup -p1 -n pytest_xdist-%{version}

%files
%{py_sitedir}/xdist
%{py_sitedir}/pytest_xdist-%{version}.dist-info
