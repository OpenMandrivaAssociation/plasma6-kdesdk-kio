Summary:	KDE SDK KIO modules
Name:		plasma6-kdesdk-kio
Version:	24.01.95
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kdesdk-kio-%{version}.tar.xz
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	perl-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
Suggests:	kio-perldoc = %{EVRD}

%description
KIO slaves for:
 - Perl documentation

%files

#----------------------------------------------------------------------------

%package -n kio-perldoc
Summary:	A KIO interface for Perl documentation
Group:		Graphical desktop/KDE
Requires:	perl(Pod::Perldoc)
Conflicts:	kdesdk4-core < 1:4.11.0
%rename kio4-perldoc

%description -n kio-perldoc
A KIO interface for Perl documentation.

%files -n kio-perldoc -f kio5_perldoc.lang
%{_libdir}/qt6/plugins/kf6/kio/perldoc.so
%{_datadir}/kio_perldoc

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n kdesdk-kio-%{version}

%build
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build
%find_lang kio5_perldoc
