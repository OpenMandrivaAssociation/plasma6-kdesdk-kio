#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Summary:	KDE SDK KIO modules
Name:		plasma6-kdesdk-kio
Version:	24.08.3
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
Source0:	https://invent.kde.org/sdk/kdesdk-kio/-/archive/%{gitbranch}/kdesdk-kio-%{gitbranchd}.tar.bz2#/kdesdk-kio-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kdesdk-kio-%{version}.tar.xz
%endif
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	perl-devel
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
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

%files -n kio-perldoc -f kio6_perldoc.lang
%{_libdir}/qt6/plugins/kf6/kio/perldoc.so
%{_datadir}/kio_perldoc

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n kdesdk-kio-%{?git:%{gitbranchd}}%{!?git:%{version}}

%install -a
%find_lang kio6_perldoc
