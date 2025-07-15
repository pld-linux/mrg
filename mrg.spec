Summary:	Microraptor GUI
Summary(pl.UTF-8):	Microraptor GUI - graficzny interfejs użytkownika
Name:		mrg
Version:	0.1.4
Release:	1
License:	LGPL v2+
Group:		Libraries
#Source0Download: https://github.com/hodefoting/mrg/releases
Source0:	https://github.com/hodefoting/mrg/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	94cfdaf46a65e292a86f2cbc01d89014
Patch1:		%{name}-format.patch
URL:		https://github.com/hodefoting/mrg/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	alsa-lib-devel
BuildRequires:	cairo-devel
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	mmm-devel >= 0.1.1
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
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
Requires:	mmm-libs >= 0.1.1

%description libs
Shared mrg library.

%description libs -l pl.UTF-8
Biblioteka współdzielona mrg.

%package devel
Summary:	Header files for mrg library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki mrg
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	alsa-lib-devel
Requires:	cairo-devel
Requires:	mmm-devel >= 0.1.1
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
%setup -q
%patch -P1 -p1

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/mrg

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmrg.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/mrg-0.1
%{_pkgconfigdir}/mrg.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmrg.a
