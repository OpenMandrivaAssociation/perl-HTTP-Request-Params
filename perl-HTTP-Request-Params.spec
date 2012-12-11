%define upstream_name	 HTTP-Request-Params
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Retrieve GET/POST Parameters from HTTP Requests
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Email::MIME::Modifier)
BuildRequires:	perl(CGI)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Email::Simple)
BuildArch:	noarch

%description
This software does all the dirty work of parsing HTTP Requests to find incoming
query parameters.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/HTTP
%{_mandir}/*/*

%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.10.0-1mdv2010.0
+ Revision: 403305
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.01-7mdv2009.0
+ Revision: 257253
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.01-5mdv2008.1
+ Revision: 122711
- kill re-definition of %%buildroot on Pixel's request


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-5mdv2007.0
- Rebuild

* Thu May 04 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-4mdk
- buildrequires fix
- better buildrequirres syntax
- better source URL

* Mon Apr 10 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.01-3mdk
- Add BuildRequires

* Tue Mar 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-2mdk
- fix buildrequires

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdk
- first mdk release

