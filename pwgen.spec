#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF2F95956950D81A3 (tytso@mit.edu)
#
Name     : pwgen
Version  : 2.08
Release  : 4
URL      : https://sourceforge.net/projects/pwgen/files/pwgen/2.08/pwgen-2.08.tar.gz
Source0  : https://sourceforge.net/projects/pwgen/files/pwgen/2.08/pwgen-2.08.tar.gz
Source1  : https://sourceforge.net/projects/pwgen/files/pwgen/2.08/pwgen-2.08.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: pwgen-bin = %{version}-%{release}
Requires: pwgen-license = %{version}-%{release}
Requires: pwgen-man = %{version}-%{release}

%description
No detailed description available

%package bin
Summary: bin components for the pwgen package.
Group: Binaries
Requires: pwgen-license = %{version}-%{release}

%description bin
bin components for the pwgen package.


%package license
Summary: license components for the pwgen package.
Group: Default

%description license
license components for the pwgen package.


%package man
Summary: man components for the pwgen package.
Group: Default

%description man
man components for the pwgen package.


%prep
%setup -q -n pwgen-2.08
cd %{_builddir}/pwgen-2.08

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604354427
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1604354427
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pwgen
cp %{_builddir}/pwgen-2.08/debian/copyright %{buildroot}/usr/share/package-licenses/pwgen/69e17895e260cf7d9bb3af5a224edf212aa6421d
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pwgen

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pwgen/69e17895e260cf7d9bb3af5a224edf212aa6421d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pwgen.1
