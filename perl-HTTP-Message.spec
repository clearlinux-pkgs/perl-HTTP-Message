#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v20
# autospec commit: 4d029647d79e
#
Name     : perl-HTTP-Message
Version  : 7.00
Release  : 69
URL      : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-Message-7.00.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-Message-7.00.tar.gz
Summary  : 'HTTP style message (base class)'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTTP-Message-license = %{version}-%{release}
Requires: perl-HTTP-Message-perl = %{version}-%{release}
Requires: perl(Clone)
BuildRequires : buildreq-cpan
BuildRequires : perl(Clone)
BuildRequires : perl(Encode::Locale)
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(IO::HTML)
BuildRequires : perl(LWP::MediaTypes)
BuildRequires : perl(Test::Needs)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(URI)
BuildRequires : perl(URI::URL)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# NAME
HTTP::Message - HTTP style message (base class)
# VERSION
version 7.00
# SYNOPSIS

%package dev
Summary: dev components for the perl-HTTP-Message package.
Group: Development
Provides: perl-HTTP-Message-devel = %{version}-%{release}
Requires: perl-HTTP-Message = %{version}-%{release}

%description dev
dev components for the perl-HTTP-Message package.


%package license
Summary: license components for the perl-HTTP-Message package.
Group: Default

%description license
license components for the perl-HTTP-Message package.


%package perl
Summary: perl components for the perl-HTTP-Message package.
Group: Default
Requires: perl-HTTP-Message = %{version}-%{release}

%description perl
perl components for the perl-HTTP-Message package.


%prep
%setup -q -n HTTP-Message-7.00
cd %{_builddir}/HTTP-Message-7.00

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTTP-Message
cp %{_builddir}/HTTP-Message-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-HTTP-Message/94e4633cce6dfabd6d1cce9321c2d5365568c677 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTTP::Config.3
/usr/share/man/man3/HTTP::Headers.3
/usr/share/man/man3/HTTP::Headers::Auth.3
/usr/share/man/man3/HTTP::Headers::ETag.3
/usr/share/man/man3/HTTP::Headers::Util.3
/usr/share/man/man3/HTTP::Message.3
/usr/share/man/man3/HTTP::Request.3
/usr/share/man/man3/HTTP::Request::Common.3
/usr/share/man/man3/HTTP::Response.3
/usr/share/man/man3/HTTP::Status.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTTP-Message/94e4633cce6dfabd6d1cce9321c2d5365568c677

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
