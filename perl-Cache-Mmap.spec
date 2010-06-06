#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	Cache
%define		pnam	Mmap
Summary:	Cache::Mmap - shared data cache using memory mapped files
Summary(pl.UTF-8):	Cache::Mmap - współdzielony bufor danych, używający mapowanych w pamięci plików
Name:		perl-Cache-Mmap
Version:	0.081
Release:	3
Epoch:		1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3170cbdf4232f5b2c578d5cd81527693
URL:		http://search.cpan.org/dist/Cache-Mmap/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a shared data cache, using memory mapped files.
If routines are provided which interact with the underlying data,
access to the cache is completely transparent, and the module handles
all the details of refreshing cache contents, and updating underlying
data, if necessary.

%description -l pl.UTF-8
Ten moduł jest implementacją współdzielonego bufora (cache) danych,
używającego plików mapowanych w pamięci. Jeśli są dostarczone funkcje
współpracujące z podlegającymi danymi, dostęp do bufora jest
całkowicie przezroczysty, a moduł obsługuje wszystkie szczegóły
odświeżania zawartości bufora i uaktualniania buforowanych danych w
miarę potrzeby.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README Todo
%dir %{perl_vendorarch}/Cache
%{perl_vendorarch}/Cache/*.pm
%dir %{perl_vendorarch}/auto/Cache
%dir %{perl_vendorarch}/auto/Cache/Mmap
%attr(755,root,root) %{perl_vendorarch}/auto/Cache/Mmap/*.so
%{perl_vendorarch}/auto/Cache/Mmap/*.bs
%{_mandir}/man3/*
