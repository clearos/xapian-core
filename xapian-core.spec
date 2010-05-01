Name:          xapian-core
Version:       1.2.0
Release:       1%{?dist}
Summary:       The Xapian Probabilistic Information Retrieval Library

Group:         Applications/Databases
License:       GPLv2+
URL:           http://www.xapian.org/
Source0:       http://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.gz
Patch0:        multilib-devel-conflict-fix.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: zlib-devel
BuildRequires: libuuid-devel
Requires:      %{name}-libs = %{version}

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
Requires:      %{name} = %{version}
Requires:      %{name}-libs = %{version}

%description devel
Xapian is an Open Source Probabilistic Information Retrieval framework. It
offers a highly adaptable toolkit that allows developers to easily add advanced
indexing and search facilities to applications. This package provides the
files needed for building packages which use Xapian

%prep
%setup -q
#%patch0 -p1 -b .multilibfix

%build
%configure --disable-static

# Remove rpath as per https://fedoraproject.org/wiki/Packaging/Guidelines#Beware_of_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags} V=1

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL='install -p'

# Remove libtool archives
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Remove the dev docs, we pick them up below
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/xapian*
%{_bindir}/quest
%{_bindir}/delve
%{_bindir}/copydatabase
%{_bindir}/simpleindex
%{_bindir}/simplesearch
%{_bindir}/simpleexpand
%{_bindir}/xapian-compact
# man pages may be gzipped, hence the trailing wildcard.
%{_mandir}/man1/xapian*
%{_mandir}/man1/quest.1*
%{_mandir}/man1/delve.1*
%{_mandir}/man1/copydatabase.1*

%files libs
%defattr(-, root, root)
%{_libdir}/libxapian.so.*

%files devel
%defattr(-, root, root)
%doc HACKING PLATFORMS docs/*html docs/apidoc docs/*pdf
%{_bindir}/xapian-config
%{_includedir}/xapian
%{_libdir}/libxapian.so
%{_datadir}/aclocal/xapian.m4
# man pages may be gzipped, hence the trailing wildcard.
%{_mandir}/man1/xapian-config.1*

%changelog
* Sat May  1 2010 Peter Robinson <pbrobinson@gmail.com> - 1.2.0-1
- Update to 1.2.0

* Sun Mar 21 2010 Peter Robinson <pbrobinson@gmail.com> - 1.0.18-1
- Update to 1.0.18

* Wed Dec  2 2009 Peter Robinson <pbrobinson@gmail.com> - 1.0.17-1
- Update to 1.0.17

* Sun Sep 19 2009 Peter Robinson <pbrobinson@gmail.com> - 1.0.16-1
- Update to 1.0.16, some spec file cleanups

* Thu Aug 27 2009 Peter Robinson <pbrobinson@gmail.com> - 1.0.15-1
- Update to 1.0.15

* Wed Jul 29 2009 Peter Robinson <pbrobinson@gmail.com> - 1.0.14-1
- Update to 1.0.14

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun  5 2009 Peter Robinson <pbrobinson@gmail.com> - 1.0.13-1
- Update to 1.0.13

* Sun Apr 12 2009 Peter Robinson <pbrobinson@gmail.com> - 1.0.12-1
- Update to 1.0.12

* Mon Apr 06 2009 Peter Robinson <pbrobinson@gmail.com> - 1.0.11-1
- Update to 1.0.11

* Wed Mar 04 2009 Caolán McNamara <caolanm@redhat.com> - 1.0.9-4
- include stdio.h for rename, fix bare #elif, EOF -> -1 for getopt

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 05 2008 Adel Gadllah <adel.gadllah@gmail.com> 1.0.9-2
- Fix build

* Sat Nov 29 2008 Adel Gadllah <adel.gadllah@gmail.com> 1.0.9-1
- Update to 1.0.9

* Sat Oct 11 2008 Adel Gadllah <adel.gadllah@gmail.com> 1.0.8-1
- Update to 1.0.8

* Sun Jul 20 2008 Adel Gadllah <adel.gadllah@gmail.com> 1.0.7-1
- Update to 1.0.7

* Sun Mar 30 2008 Adel Gadllah <adel.gadllah@gmail.com> 1.0.6-1
- Update to 1.0.6

* Sat Feb 09 2008 Adel Gadllah <adel.gadllah@gmail.com> 1.0.5-2
- Rebuild for gcc-4.3

* Thu Dec 27 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.0.5-1
- Update to 1.0.5

* Tue Oct 30 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.0.4-1
- Update to 1.0.4

* Fri Oct 25 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.0.2-7
- Fix up multilib patch

* Thu Oct 25 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.0.2-6
- Fix multilib conflict in devel package (RH #343471)

* Tue Aug 21 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.0.2-5
- Rebuild for BuildID and ppc32 bug

* Wed Aug 08 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.0.2-4
- Add disttag

* Wed Aug 08 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.0.2-3
- Bump to avoid tag conflict

* Wed Aug 08 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.0.2-2
- Add missing files
- Minor cleanups

* Wed Aug 08 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.0.2-1
- Update to 1.0.2
- Fix License tag

* Sat Jun 16 2007 Marco Pesenti Gritti <mpg@redhat.com> 1.0.1-1
- Update to 1.0.1

* Tue May  8 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.9.10-2.2.svn8397
- Initial build
