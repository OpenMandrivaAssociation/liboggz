%define	major 2
%define libname %mklibname oggz %{major}
%define develname %mklibname oggz -d

Summary:	Simple programming interface for Ogg files and streams
Name:		liboggz
Version:	1.1.1
Release:	2
Group:		System/Libraries
License:	BSD-like
URL:		http://www.xiph.org/oggz/
Source0:	http://downloads.xiph.org/releases/liboggz/%{name}-%{version}.tar.gz
BuildRequires:	libogg-devel >= 1.0
#disabling doxygen because of obsolete instructions
#BuildRequires:	doxygen
BuildRequires:	docbook-utils

%description
Oggz provides a simple programming interface for reading and writing Ogg files
and streams. Ogg is an interleaving data container developed by Monty at
Xiph.Org, originally to support the Ogg Vorbis audio format.

%package -n %{libname}
Summary:	Simple programming interface for Ogg files and streams
Group:		System/Libraries

%description -n	%{libname}
Oggz provides a simple programming interface for reading and writing Ogg files
and streams. Ogg is an interleaving data container developed by Monty at
Xiph.Org, originally to support the Ogg Vorbis audio format.

%package -n %{develname}
Summary:	Files needed for development using liboggz
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname oggz 1 -d} < 1.1.1

%description -n	%{develname}
Oggz provides a simple programming interface for reading and writing Ogg files
and streams. Ogg is an interleaving data container developed by Monty at
Xiph.Org, originally to support the Ogg Vorbis audio format.

This package contains the header files and documentation needed for development
using liboggz.

%package tools
Summary:	Various tools using the liboggz library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description tools
This package contains various tools using the liboggz library.

%prep

%setup -q

%build

%configure2_5x \
	--disable-static

%make

%check
make check

%install
%makeinstall_std

# cleanup
rm -rf %{buildroot}%{_docdir}/liboggz

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc doc/liboggz/html/*
%doc AUTHORS ChangeLog README
%dir %{_includedir}/oggz
%{_includedir}/oggz/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/oggz.pc

%files tools
%defattr(-,root,root)
%{_bindir}/oggz*
%{_mandir}/man1/*
