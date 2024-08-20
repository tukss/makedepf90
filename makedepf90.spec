Name:           makedepf90
Version:        3.0.1
Release:        %autorelease
Summary:        Creates Makefile-style dependency lists for Fortran source code
License:        GPL-2.0-only
URL:            https://salsa.debian.org/science-team/makedepf90
Source:         https://deb.debian.org/debian/pool/main/m/makedepf90/makedepf90_%{version}.orig.tar.xz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  bison
BuildRequires:  flex

%description
Makedepf90 is a program for automatic creation of Makefile dependency
lists for Fortran source code. Makedepf90 supports MODULE:s, INCLUDE:s,
cpp #include:s, f90ppr $include:s and coco ??include:s and set-files.

The original idea was to provide the same functionality for Fortran as

 gcc -MM *.c

does for C.

%prep
%autosetup


%build
%configure
sed -i -e 's/^\(exec_\)\?prefix = \(.*\)$/\1prefix = \$\{DESTDIR\}\2/' -e 's/^\(.*\)\?dir = \(.*\)$/\1dir = \$\{DESTDIR\}\2/' Makefile
%make_build


%install
%make_install


%files
%{_bindir}/makedepf90
%{_mandir}/man1/makedepf90.1.*
%license COPYING
%doc NEWS README README.submodules


%changelog
%autochangelog
