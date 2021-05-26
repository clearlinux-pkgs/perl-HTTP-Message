#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTTP-Message
Version  : 6.32
Release  : 51
URL      : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-Message-6.32.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-Message-6.32.tar.gz
Summary  : 'HTTP style message (base class)'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTTP-Message-license = %{version}-%{release}
Requires: perl-HTTP-Message-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Encode::Locale)
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(IO::HTML)
BuildRequires : perl(LWP::MediaTypes)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(URI)
BuildRequires : perl(URI::URL)

%description
# NAME
HTTP::Message - HTTP style message (base class)
# VERSION
version 6.32
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
%setup -q -n HTTP-Message-6.32
cd %{_builddir}/HTTP-Message-6.32

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
cp %{_builddir}/HTTP-Message-6.32/LICENSE %{buildroot}/usr/share/package-licenses/perl-HTTP-Message/eeeb3a21464437014b95494ac4a3b662a0541bbb
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
/usr/share/package-licenses/perl-HTTP-Message/eeeb3a21464437014b95494ac4a3b662a0541bbb

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/HTTP/Config.pm
/usr/lib/perl5/vendor_perl/5.34.0/HTTP/Headers.pm
/usr/lib/perl5/vendor_perl/5.34.0/HTTP/Headers/Auth.pm
/usr/lib/perl5/vendor_perl/5.34.0/HTTP/Headers/ETag.pm
/usr/lib/perl5/vendor_perl/5.34.0/HTTP/Headers/Util.pm
/usr/lib/perl5/vendor_perl/5.34.0/HTTP/Message.pm
/usr/lib/perl5/vendor_perl/5.34.0/HTTP/Request.pm
/usr/lib/perl5/vendor_perl/5.34.0/HTTP/Request/Common.pm
/usr/lib/perl5/vendor_perl/5.34.0/HTTP/Response.pm
/usr/lib/perl5/vendor_perl/5.34.0/HTTP/Status.pm
