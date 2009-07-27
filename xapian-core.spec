Summary: The Xapian Probabilistic Information Retrieval Library
Name: xapian-core
Version: 1.0.13
Release: 2%{?dist}
License: GPLv2+
Group: Applications/Databases
URL: http://www.xapian.org/
Requires: %{name}-libs = %{version}
Source0: http://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.gz
Patch0: multilib-devel-conflict-fix.patch
Patch1: xapian-core-1.0.9-includes.patch
BuildRequires: autoconf automake libtool
BuildRequires: zlib-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Xapian is an Open Source Probabilistic Information Retrieval Library. It
offers a highly adaptable toolkit that allows developers to easily add advanced
indexing and search facilities to applications

%package libs
Summary: Xapian search engine libraries
Group: System Environment/Libraries

%description libs
Xapian is an Open Source Probabilistic Information Retrieval framework. It
offers a highly adaptable toolkit that allows developers to easily add advanced
indexing and search facilities to applications. This package provides the
libraries for applications using Xapian functionality

%package devel
Group: Development/Libraries
Summary: Files needed for building packages which use Xapian
Requires: %{name} = %{version}
Requires: %{name}-libs = %{version}

%description devel
Xapian is an Open Source Probabilistic Information Retrieval framework. It
offers a highly adaptable toolkit that allows developers to easily add advanced
indexing and search facilities to applications. This package provides the
files needed for building packages which use Xapian

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .multilibfix
#%patch1 -p1 -b .includes

%build
# FC6 (at least) has a patched libtool which knows not to set rpath for
# /usr/lib64, which upstream libtool fails to do currently.  We can drop
# this "autoreconf --force" and the "BuildRequires:" for the autotools
# once upstream libtool is fixed.  Note: this overwrites INSTALL, but
# that doesn't matter here as we don't package it.
autoreconf --force -i
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
# makeinstall doesn't work properly with libtool built libraries
make DESTDIR=%{buildroot} install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# Move the docs to the right place
mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_datadir}/doc/%{name}-devel-%{version}
# Copy HACKING now, as "%doc HACKING" would overwrite everything
cp HACKING %{buildroot}%{_datadir}/doc/%{name}-devel-%{version}
# Copy the rest while we are in this directory
mkdir -p %{buildroot}%{_datadir}/doc/%{name}-%{version}
cp AUTHORS ChangeLog COPYING NEWS PLATFORMS README %{buildroot}%{_datadir}/doc/%{name}-%{version}

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/xapian-check
%{_bindir}/xapian-inspect
%{_bindir}/xapian-tcpsrv
%{_bindir}/xapian-progsrv
%{_bindir}/quartzcheck
%{_bindir}/quartzcompact
%{_bindir}/quartzdump
%{_bindir}/quest
%{_bindir}/delve
%{_bindir}/copydatabase
%{_bindir}/simpleindex
%{_bindir}/simplesearch
%{_bindir}/simpleexpand
%{_bindir}/xapian-compact
%doc %{_datadir}/doc/%{name}-%{version}
# man pages may be gzipped, hence the trailing wildcard.
%{_mandir}/man1/xapian-check.1*
%{_mandir}/man1/xapian-inspect.1*
%{_mandir}/man1/xapian-tcpsrv.1*
%{_mandir}/man1/xapian-progsrv.1*
%{_mandir}/man1/quartzcheck.1*
%{_mandir}/man1/quartzcompact.1*
%{_mandir}/man1/quartzdump.1*
%{_mandir}/man1/quest.1*
%{_mandir}/man1/delve.1*
%{_mandir}/man1/copydatabase.1*
%{_mandir}/man1/xapian-compact.1*

%files libs
%defattr(-, root, root)
%{_libdir}/libxapian.so.*

%files devel
%defattr(-, root, root)
%{_bindir}/xapian-config
%{_includedir}/xapian
%{_includedir}/xapian.h
%{_libdir}/libxapian.so
%{_datadir}/aclocal/xapian.m4
%doc %{_datadir}/doc/%{name}-devel-%{version}
# man pages may be gzipped, hence the trailing wildcard.
%{_mandir}/man1/xapian-config.1*

%changelog
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
