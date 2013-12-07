%define major 2
%define libname %mklibname oggz %{major}
%define devname %mklibname oggz -d

Summary:	Simple programming interface for Ogg files and streams
Name:		liboggz
Version:	1.1.1
Release:	5
Group:		System/Libraries
License:	BSD-like
Url:		http://www.xiph.org/oggz/
Source0:	http://downloads.xiph.org/releases/liboggz/%{name}-%{version}.tar.gz
BuildRequires:	docbook-utils
BuildRequires:	pkgconfig(ogg)

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

%package -n %{devname}
Summary:	Files needed for development using liboggz
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
This package contains the header files and documentation needed for development
using liboggz.

%package tools
Summary:	Various tools using the liboggz library
Group:		Development/C

%description tools
This package contains various tools using the liboggz library.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%check
#make check

%install
%makeinstall_std

# cleanup
rm -rf %{buildroot}%{_docdir}/liboggz

%files -n %{libname}
%{_libdir}/liboggz.so.%{major}*

%files -n %{devname}
%doc doc/liboggz/html/*
%doc AUTHORS ChangeLog README
%dir %{_includedir}/oggz
%{_includedir}/oggz/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/oggz.pc

%files tools
%{_bindir}/oggz*
%{_mandir}/man1/*




%changelog
* Tue Aug 03 2010 Funda Wang <fwang@mandriva.org> 1.1.1-1mdv2011.0
+ Revision: 565337
- new version 1.1.1

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1.0-1mdv2010.1
+ Revision: 462443
- Update to new version 1.1.0 (new major)

* Fri Sep 25 2009 Frederik Himpe <fhimpe@mandriva.org> 1.0.0-1mdv2010.0
+ Revision: 449173
- update to new version 1.0.0

* Sun Sep 13 2009 Thierry Vignaud <tv@mandriva.org> 0.9.8-2mdv2010.0
+ Revision: 438722
- rebuild

* Wed Jan 07 2009 Emmanuel Andry <eandry@mandriva.org> 0.9.8-1mdv2009.1
+ Revision: 326870
- New version 0.9.8
- protect major
- disable doxygen for now, breaks build

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.9.7-2mdv2009.0
+ Revision: 267964
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri May 23 2008 Funda Wang <fwang@mandriva.org> 0.9.7-1mdv2009.0
+ Revision: 210295
- New version 0.9.7

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.9.5-2mdv2008.1
+ Revision: 136557
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.5-2mdv2008.0
+ Revision: 83599
- new devel naming


* Sat Dec 09 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.5-1mdv2007.0
+ Revision: 94249
- Import liboggz

* Mon Aug 07 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.5-1mdv2007.0
- initial Mandriva package (fc5 extras import)

