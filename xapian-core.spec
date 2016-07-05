Name:          xapian-core
Version:       1.2.23
Release:       1%{?dist}
Summary:       The Xapian Probabilistic Information Retrieval Library

Group:         Applications/Databases
License:       GPLv2+
URL:           http://www.xapian.org/
Source0:       http://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.xz

BuildRequires: zlib-devel
BuildRequires: libuuid-devel
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}


%description
Xapian is an Open Source Probabilistic Information Retrieval Library. It
offers a highly adaptable toolkit that allows developers to easily add advanced
indexing and search facilities to applications

%package libs
Summary:       Xapian search engine libraries
Group:         System Environment/Libraries

%description libs
Xapian is an Open Source Probabilistic Information Retrieval framework. It
offers a highly adaptable toolkit that allows developers to easily add advanced
indexing and search facilities to applications. This package provides the
libraries for applications using Xapian functionality

%package devel
Group:         Development/Libraries
Summary:       Files needed for building packages which use Xapian
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
Requires:      libuuid-devel

%description devel
Xapian is an Open Source Probabilistic Information Retrieval framework. It
offers a highly adaptable toolkit that allows developers to easily add advanced
indexing and search facilities to applications. This package provides the
files needed for building packages which use Xapian

%prep
%setup -q

%build
# Disable SSE on x86, but leave it intact for x86_64
%ifarch x86_64
%configure --disable-static
%else
%configure --disable-static --disable-sse
%endif

# Remove rpath as per https://fedoraproject.org/wiki/Packaging/Guidelines#Beware_of_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

# Remove libtool archives
find $RPM_BUILD_ROOT -name '*.la' -delete

# Remove the dev docs, we pick them up below
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{_bindir}/xapian*
%{_bindir}/quest
%{_bindir}/delve
%{_bindir}/copydatabase
%{_bindir}/simpleindex
%{_bindir}/simplesearch
%{_bindir}/simpleexpand
# man pages may be gzipped, hence the trailing wildcard.
%{_mandir}/man1/xapian*
%{_mandir}/man1/quest.1*
%{_mandir}/man1/delve.1*
%{_mandir}/man1/copydatabase.1*

%files libs
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/libxapian.so.*

%files devel
%doc HACKING PLATFORMS docs/*html docs/apidoc docs/*pdf
%{_bindir}/xapian-config
%{_includedir}/xapian
%{_includedir}/xapian.h
%{_libdir}/libxapian.so
%{_libdir}/cmake/xapian
%{_libdir}/pkgconfig/xapian-core.pc
%{_datadir}/aclocal/xapian.m4
# man pages may be gzipped, hence the trailing wildcard.
%{_mandir}/man1/xapian-config.1*

%changelog
* Tue Jul  5 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.23-1
- Update to 1.2.23

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan  6 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.22-1
- Update to 1.2.22
- Use %%license

* Fri Nov 27 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.21-3
- Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.21-1
- Update to 1.2.21

* Wed Apr 15 2015 Petr Pisar <ppisar@redhat.com> - 1.2.20-2
- Rebuild owing to C++ ABI change in GCC-5 (bug #1195353)

* Sat Mar 21 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.20-1
- Update to 1.2.20

* Wed Feb 25 2015 Than Ngo <than@redhat.com> 1.2.19-3
- rebuilt against new gcc5

* Sat Feb 07 2015 Rex Dieter <rdieter@fedoraproject.org> 1.2.19-2
- rebuild (gcc)

* Tue Nov 11 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.19-1
- Update to 1.2.19

* Mon Sep  1 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.18-1
- Update to 1.2.18

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 15 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.17-1
- Update to 1.2.17

* Sun Jan 12 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.16-1
- Update to 1.2.16

* Fri Aug 23 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.15-1
- Update to 1.2.15

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.14
- Update to 1.2.14

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.12-1
- Update to 1.2.12

* Sun Apr 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.9-1
- Update to 1.2.9

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-2
- Rebuilt for c++ ABI breakage

* Sat Jan 21 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.8-1
- Update to 1.2.8

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 18 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.7-1
- Update to 1.2.7

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 16 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.4-1
- Update to 1.2.4

* Mon Aug 30 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3

* Thu Aug  5 2010 Adel Gadllah <adel.gadllah@gmail.com> - 1.2.2-5
- Reenable SSE on x86_64

* Thu Aug  5 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.2-4
- Disable SSE instructions by default

* Wed Jul 14 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.2-3
- And remove non spec cut-n-paste issue

* Wed Jul 14 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.2-2
- Add cmake stuff

* Wed Jul 14 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Fri May  7 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.0-4
- Move license to libs package, a few other spc cleanups

* Fri May  7 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.0-3
- Add the libtool archive (temporarily) to fix build of bindings

* Sat May  1 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.0-2
- Upload new source 

* Sat May  1 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0
