Summary:	Linux boots Linux via network
Summary(pl.UTF-8):	Uruchamianie Linuksa przez Linuksa po sieci
Name:		pxe-kexec
Version:	0.2.4
Release:	0.1
License:	GPL v2+
Group:		Applications/System
Source0:	http://download.berlios.de/pxe-kexec/%{name}-%{version}.tar.bz2
# Source0-md5:	2e6fd2e0e9fb0f0a006935c9d1860284
URL:		http://pxe-kexec.berlios.de/
BuildRequires:	cmake >= 2.4
BuildRequires:	curl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	perl-tools-pod
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.577
Requires:	kexec-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pxe-kexec reads a PXELINUX configuration file, prompts the user for an
entry like the PXELINUX program would do and finally boots that entry
using Kexec.

%description -l pl.UTF-8
pxe-kexec odczytuje plik konfiguracyjny bootloadera PXELINUX, pyta
użytkownika o opcję systemu w taki sam sposób, jak PXELINUX, a
następnie uruchamia system przy użyciu mechanizmu kexec.

%prep
%setup -q

%build
%cmake . \
	-DCMAKE_C_FLAGS_RELEASE="-DNDEBUG" \
	-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
	-DCURSES_INCLUDE_PATH=/usr/include/ncurses

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/pxe-kexec
%{_mandir}/man8/pxe-kexec.8*
