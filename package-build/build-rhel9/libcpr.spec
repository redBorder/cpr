Name:           libcpr
Version:        1.10.4
Release:        1%{?dist}
Summary:        C++ Requests: Curl for People (static library)

License:        MIT
URL:            https://github.com/libcpr/cpr
Source0:        libcpr-%{version}.tar.gz

# disable automatic debug subpackages
%define debugsource    %{nil}
%define debug_package  %{nil}
# allow unowned files (e.g. CMake config) in buildroot
%define _unpackaged_files_terminate_build 0

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  curl-devel
BuildRequires:  openssl-devel

%description
This package provides **libcpr.a**, the static archive for libcpr (“Curl for People”).

%package devel
Summary:        Development files for libcpr (headers & CMake config)
Requires:       libcpr = %{version}-%{release}

%description devel
This package contains the public headers and any CMake export files you need
to compile and link against libcpr.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake \
    -DCPR_USE_SYSTEM_CURL=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=OFF \
    -DCMAKE_INSTALL_PREFIX=%{_prefix}
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc    README.md
%{_libdir}/libcpr.a

%files devel
%{_includedir}/cpr/

%changelog
* Thu Apr 24 2025 Miguel Álvarez <malvarez@redborder.com> - 1.10.4-1
- switch to RPM CMake macros to fix stray “-D…” shell errors
- build static archive only (libcpr.a) and split headers/CMake config into -devel
- added openssl-devel to BuildRequires

