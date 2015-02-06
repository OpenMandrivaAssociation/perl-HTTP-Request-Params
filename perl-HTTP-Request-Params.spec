%define upstream_name	 HTTP-Request-Params
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Retrieve GET/POST Parameters from HTTP Requests
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:         perl-HTTP-Request-Params-1.01-fix-build.patch

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
%patch0 -p1 -b .fix-build

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
