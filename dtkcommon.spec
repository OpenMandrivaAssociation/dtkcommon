# This package contains files under %%_libdir but no binary files
%global debug_package %{nil}

%define devname %mklibname -d dtkcommon

Name:           dtkcommon
Version:        5.6.32
Release:        1
Summary:        DTK common files
Group:          System/Deepin
License:        BSD-3-Clause
URL:            https://github.com/linuxdeepin/dtkcommon
Source0:        https://github.com/linuxdeepin/dtkcommon/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake

%description
This package contains common configuration files for DTK.


%package -n %{devname}
Summary:        Development package for %{name}
Requires:       %{name} = %{EVRD}
Provides:       dtkcommon-devel = %{EVRD}

%description -n %{devname}
This package contains common build configuration files for DTK.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
%license LICENSE
%doc README.md
%{_datadir}/dsg/configs/org.deepin.dtk.preference.json

%files -n %{devname}
%{_libdir}/cmake/Dtk/
%{_libdir}/cmake/Dtk6/
%{_libdir}/cmake/DtkBuildHelper/
