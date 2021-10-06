Name:       sailfish-memory-watcher

# >> macros

# ignore installed files that are not packed to rpm
%define _unpackaged_files_terminate_build 0

# don't setup rpm provides
%define __provides_exclude_from ^%{_datadir}/.*$

# don't setup rpm requires
# list here all the libraries your RPM installs
%define __requires_exclude ^ld-linux$

# << macros

Summary:    Memory watcher for Sailfish
Version:    0.1
Release:    1
Group:      Qt/Qt
License:    GPLv2
URL:        https://github.com/Karry/sailfish-memory-watcher
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  cmake
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  git
BuildRequires:  qt5-qttools-linguist

%description
Tool for recoding application memory usage.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
#rm -rf rpmbuilddir-%{_arch}
mkdir -p rpmbuilddir-%{_arch}
cd rpmbuilddir-%{_arch} && cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_RPATH=%{_datadir}/%{name}/lib/: ../memory-watcher

cd ..
make -C rpmbuilddir-%{_arch} VERBOSE=1 %{?_smp_mflags}
# << build pre

# >> build post
# << build post

%install
# >> install pre
#rm -rf %{buildroot}
DESTDIR=%{buildroot} make -C rpmbuilddir-%{_arch} install
mkdir -p %{_bindir}
# << install pre

# >> install post

## Jolla harbour rules:

# -- ship all shared unallowed libraries with the app
mkdir -p %{buildroot}%{_datadir}/%{name}/lib

# << install post

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/%{name}/lib/
# >> files
# << files
