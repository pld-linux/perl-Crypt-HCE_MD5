%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	HCE_MD5
Summary:	Crypt::HCE_MD5 Perl module - hash chaining encryption using MD5
Summary(pl):	Modu� Perla Crypt::HCE_MD5 - �a�cuchowe kodowanie z u�yciem MD5
Name:		perl-Crypt-HCE_MD5
Version:	0.60
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f3ac65480ab9cc7dbeb310db9d6eafbd
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Digest-MD5 >= 2
BuildRequires:	perl-MIME-Base64 >= 2
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Digest-MD5 >= 2
Requires:	perl-MIME-Base64 >= 2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a chaining block cipher using a one way hash.
This method of encryption is the same that is used by radius (RFC2138)
and is also described in Applied Cryptography.

%description -l pl
Ten modu� jest implementacj� �a�cuchowego szyfru blokowego przy u�yciu
jednokierunkowego mieszania. Jest to ta sama metoda, co u�ywana w
radiusie (RFC 2138) oraz opisana w Applied Cryptography.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Crypt/HCE_MD5.pm
%{perl_vendorlib}/auto/Crypt/HCE_MD5
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
