Summary:	Microraptor GUI
Summary(pl.UTF-8):	Microraptor GUI - graficzny interfejs użytkownika
Name:		mrg
Version:	0.1.2
%define 	gitref	ba04b1ee9c63cbd50ea0ac9211fad881a0724361
%define		snap	20190322
Release:	1.%{snap}.1
License:	LGPL v2+
Group:		Libraries
Source0:	https://github.com/hodefoting/mrg/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	5a2009b7431e6baeb067cce61851833f
Patch0:		%{name}-mm.patch
Patch1:		%{name}-format.patch
URL:		https://github.com/hodefoting/mrg/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	cairo-devel
BuildRequires:	mmm-devel >= 0-0.20171127.1
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Immediate UI framework with cairo. Also a minimal usable graphical
user environment built using the framework, including: a shell/host
for client programs, a terminal emulator, file browser and text editor
written using the library.

%description -l pl.UTF-8
Pośredni szkielet interfejsu użytkownika wykorzystujący cairo. Zawiera
także zbudowane przy użyciu tego szkieletu minimalne używalne
graficzne środowisko użytkownika, zawierające: powłokę/hosta dla
programów klienckich, emulator terminala, przeglądarkę plików oraz
edytor tekstu.

%package libs
Summary:	Shared mrg library
Summary(pl.UTF-8):	Biblioteka współdzielona mrg
Group:		Libraries

%description libs
Shared mrg library.

%description libs -l pl.UTF-8
Biblioteka współdzielona mrg.

%package devel
Summary:	Header files for mrg library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki mrg
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	cairo-devel
Requires:	mmm-devel >= 0-0.20171127.1
Requires:	gtk+3-devel >= 3.0

%description devel
Header files for mrg library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki mrg.

%package static
Summary:	Static mrg library
Summary(pl.UTF-8):	Statyczna biblioteka mrg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static mrg library.

%description static -l pl.UTF-8
Statyczna biblioteka mrg.

%prep
%setup -q -n %{name}-%{gitref}
%patch0 -p1
%patch1 -p1

%build
# not autoconf configure
./configure \
	CFLAGS="%{rpmcflags} -std=gnu99"\
	--prefix=%{_prefix} \
	--libdir=%{_libdir}
%{__make} \
	CC="%{__cc}" \
	LD="%{__cc}" \
	LD_FLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/mrg
%attr(755,root,root) %{_bindir}/mrg-browser
%attr(755,root,root) %{_bindir}/mrg-edit
%attr(755,root,root) %{_bindir}/mrg-host
%attr(755,root,root) %{_bindir}/mrg-terminal

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmrg.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/mrg
%{_pkgconfigdir}/mrg.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmrg.a
