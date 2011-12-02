#
# crash core analysis suite
#
Summary: trace extension module for the crash utility
Name: crash-trace-command
Version: 1.0
Release: 3%{?dist}
License: GPLv2
Group: Development/Debuggers
Source: %{name}-%{version}.tar.gz
URL: http://people.redhat.com/anderson/extensions/trace.c
Vendor: Fujitsu Limited
Packager: Lai Jiangshan <laijs@cn.fujitsu.com>
ExclusiveOS: Linux
ExclusiveArch: x86_64 %{ix86} ppc64 ia64 s390 s390x
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: crash-devel zlib-devel
Patch0: s390.patch
Patch1: trace_show_segv.patch

%description
Command for reading ftrace data from a dumpfile.

%prep
%setup -n %{name}-%{version}
%patch0 -p1 -b s390.patch
%patch1 -p1 -b trace_show_segv.patch

%build
make

%install
mkdir -p %{buildroot}%{_libdir}/crash/extensions/
cp %{_builddir}/%{name}-%{version}/trace.so %{buildroot}%{_libdir}/crash/extensions/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/crash/extensions/trace.so
%doc COPYING

%changelog
* Wed Jun  9 2010 Dave Anderson <anderson@redhat.com> - 1.0-3
- Remove trace_dump.patch, which requires a kernel later than
  the RHEL6 base of 2.6.32.
  Resolves: rbhz#601536

* Mon May 24 2010 Dave Anderson <anderson@redhat.com> - 1.0-2
- Fix for segmentation violation with "trace show -c cpu" command,
  and add "trace dump -t" command.
  Resolves: rbhz#592887

* Wed Dec 09 2009 Dave Anderson <anderson@redhat.com> - 1.0-1.2
- fix Makefile to account for s390 build
- change exclusive arch entry from i386 to %{ix86}
- Resolves: rbhz#545564

* Tue Dec 08 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.0-1.1
- Rebuilt for RHEL 6

* Fri Sep 25 2009  Dave Anderson <anderson@redhat.com>
- Initial crash-trace-command package

