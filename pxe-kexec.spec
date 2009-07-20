Summary:	Linux boots Linux via network
Name:		pxe-kexec
Version:	0.1.7
Release:	0.1
License:	GPL v2+
Group:		Applications/System
URL:		http://pxe-kexec.berlios.de/
Source0:	http://download.berlios.de/pxe-kexec/%{name}-%{version}.tar.bz2
# Source0-md5:	3aa6f95a31a3e7eadc363dec9d8321d7
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
Requires:	kexec-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pxe-kexec reads a PXELINUX configuration file, prompts the user for an
entry like the PXELINUX program would do and finally boots that entry
using Kexec.

%prep
%setup -q

%build
%cmake . \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCURSES_INCLUDE_PATH=/usr/include/ncurses

%{__make} VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README ChangeLog
%attr(755,root,root) %{_sbindir}/pxe-kexec
%{_mandir}/man8/pxe-kexec.8*
