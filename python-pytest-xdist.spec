# Created by pyp2rpm-3.3.5
%global pypi_name pytest-xdist

Name:           python-%{pypi_name}
Version:        2.3.0
Release:        1
Summary:        pytest xdist plugin for distributed testing and loop-on-failing modes
Group:          Development/Python
License:        MIT
URL:            https://github.com/pytest-dev/pytest-xdist
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(execnet) >= 1.1
BuildRequires:  python3dist(filelock)
BuildRequires:  python3dist(psutil) >= 3
BuildRequires:  python3dist(pytest) >= 6
BuildRequires:  python3dist(pytest-forked)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)

Requires: python-execnet >= 1.1

%description
test run parallelization, if you have multiple CPUs or hosts you can use those
for a combined test run. This allows you to speed up development or to use 
special resources of remote machines

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/xdist
%{python3_sitelib}/pytest_xdist-%{version}-py%{python3_version}.egg-info

