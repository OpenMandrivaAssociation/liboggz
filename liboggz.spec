%define	major 1
%define libname %mklibname oggz %{major}
%define develname %mklibname oggz -d

Summary:	Simple programming interface for Ogg files and streams
Name:		liboggz
Version:	0.9.5
Release:	%mkrel 2
Group:		System/Libraries
License:	BSD
URL:		http://www.annodex.net/
Source0:	http://www.annodex.net/software/liboggz/download/%{name}-%{version}.tar.bz2
BuildRequires:	libogg-devel >= 1.0
BuildRequires:	doxygen
BuildRequires:	docbook-utils
BuildRequires:	autoconf2.5
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Oggz provides a simple programming interface for reading and writing Ogg files
and streams. Ogg is an interleaving data container developed by Monty at
Xiph.Org, originally to support the Ogg Vorbis audio format.

%package -n	%{libname}
Summary:	Simple programming interface for Ogg files and streams
Group:          System/Libraries

%description -n	%{libname}
Oggz provides a simple programming interface for reading and writing Ogg files
and streams. Ogg is an interleaving data container developed by Monty at
Xiph.Org, originally to support the Ogg Vorbis audio format.

%package -n	%{develname}
Summary:	Files needed for development using liboggz
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname oggz 1 -d}

%description -n	%{develname}
Oggz provides a simple programming interface for reading and writing Ogg files
and streams. Ogg is an interleaving data container developed by Monty at
Xiph.Org, originally to support the Ogg Vorbis audio format.

This package contains the header files and documentation needed for development
using liboggz.

%package	tools 
Summary:	Various tools using the liboggz library
Group:		Development/C
Requires:	%{libname} = %{version}

%description	tools
This package contains various tools using the liboggz library.

%prep

%setup -q -n %{name}-%{version}

%build

%configure2_5x

%make

%check
make check

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

# cleanup
rm -rf %{buildroot}%{_docdir}/liboggz

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc doc/liboggz/html/*
%dir %{_includedir}/oggz
%{_includedir}/oggz/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/oggz.pc

%files tools
%defattr(-,root,root)
%{_bindir}/oggz*
%{_mandir}/man1/*
