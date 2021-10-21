%global         pypi_name           colour
%global         pypi_version        0.1.5

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1
Summary:        Converts and manipulates common color representation (RGB, HSL, web, ...)
License:        BSD-3-Clause
URL:            https://github.com/vaab/%{pypi_name}
Source0:        https://github.com/vaab/%{pypi_name}/archive/refs/tags/v%{pypi_version}.tar.gz#/%{pypi_name}-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-pip python3-devel python3-setuptools python3-wheel git

%description
Converts and manipulates various color representation (HSL, RVB, web, X11, ...)


%package        -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-nose

%description    -n python3-%{pypi_name}
Converts and manipulates various color representation (HSL, RVB, web, X11, ...)


%prep
%autosetup -n %{pypi_name}-%{pypi_version} -S git
%{__git} tag -a %{pypi_version} -m "%{_vendor} build"
pip3 config set global.index-url https://mirrors.huaweicloud.com/repository/pypi/simple
pip3 config set global.trusted-host https://mirrors.huaweicloud.com


%build
./autogen.sh
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info
%{python3_sitelib}/__pycache__/*


%changelog
* Wed Sep 29 2021 herengui <herengui@uniontech.com> - 0.1.5-1
- Initial package.
