Summary: MySQL compatible Rijndael (AES) encryption in Perl
Name: crypt-rijndael-mysql
Version: 0.03
Release: 1%{?dist}
License: GPL v2
Vendor: codeholic <http://www.ivan.fomichev.name/>
Group: Encrypt/MySQL
URL: https://github.com/arstercz/crypt-rijndael-mysql
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.30
Requires: perl(Crypt::Rijndael)
Source0: crypt-rijndael-mysql-%{version}.tar.gz

%description
%{summary}.

%prep
%setup -q -n crypt-rijndael-mysql-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL
make %{?_smp_mflags} OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -a \( -name perllocal.pod -o -name .packlist \
  -o \( -name '*.bs' -a -empty \) \) -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

for brp in %{_prefix}/lib/rpm/%{_build_vendor}/brp-compress \
  %{_prefix}/lib/rpm/brp-compress
do
  [ -x $brp ] && $brp && break
done

find $RPM_BUILD_ROOT -type f \
| sed "s@^$RPM_BUILD_ROOT@@g" \
> %{name}-%{version}-%{release}-filelist

if [ "$(cat %{name}-%{version}-%{release}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit 1
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root,-)

%post

cat <<BANNER

------------------------------------------------------------
arstercz<arstercz@gmail.com>
------------------------------------------------------------
BANNER

%changelog
* Wed Oct 26 2022 arstercz <arstercz@gmail.com>
- Version 0.03

