#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	Cache
%define		pnam	Mmap
Summary:	Cache::Mmap - Shared data cache using memory mapped files
Summary(pl):	Cache::Mmap - Wspó³dzielony bufor danych, u¿ywaj±cy mapowanych w pamiêci plików
Name:		perl-Cache-Mmap
Version:	0.081
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3170cbdf4232f5b2c578d5cd81527693
BuildRequires:	perl-devel >= 5.8.0
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

%description -l pl
Ten modu³ jest implementacj± wspó³dzielonego bufora (cache) danych,
u¿ywaj±cego plików mapowanych w pamiêci. Je¶li s± dostarczone funkcje
wspó³pracuj±ce z podlegaj±cymi danymi, dostêp do bufora jest
ca³kowicie przezroczysty, a modu³ obs³uguje wszystkie szczegó³y
od¶wie¿ania zawarto¶ci bufora i uaktualniania buforowanych danych w
miarê potrzeby.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
