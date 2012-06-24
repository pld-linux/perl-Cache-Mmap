#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Cache
%define		pnam	Mmap
Summary:	Cache::Mmap - Shared data cache using memory mapped files
Summary(pl):	Cache::Mmap - Wsp�dzielony bufor danych, u�ywaj�cy mapowanych w pami�ci plik�w
Name:		perl-Cache-Mmap
Version:	0.05
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl(Storable)
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a shared data cache, using memory mapped files.
If routines are provided which interact with the underlying data,
access to the cache is completely transparent, and the module handles
all the details of refreshing cache contents, and updating underlying
data, if necessary.

%description -l pl
Ten modu� jest implementacj� wsp�dzielonego bufora (cache) danych,
u�ywaj�cego plik�w mapowanych w pami�ci. Je�li s� dostarczone funkcje
wsp�pracuj�ce z podlegaj�cymi danymi, dost�p do bufora jest
ca�kowicie przezroczysty, a modu� obs�uguje wszystkie szczeg�y
od�wie�ania zawarto�ci bufora i uaktualniania buforowanych danych w
miar� potrzeby.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README Todo
%dir %{perl_sitearch}/Cache
%{perl_sitearch}/Cache/*.pm
%dir %{perl_sitearch}/auto/Cache
%dir %{perl_sitearch}/auto/Cache/Mmap
%attr(755,root,root) %{perl_sitearch}/auto/Cache/Mmap/*.so
%{perl_sitearch}/auto/Cache/Mmap/*.bs
%{_mandir}/man3/*
