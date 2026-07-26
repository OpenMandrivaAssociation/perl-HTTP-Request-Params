%define upstream_name	 HTTP-Request-Params
Name:		perl-%{upstream_name}
Version:	1.02
Release:	2

Summary:	Retrieve GET/POST Parameters from HTTP Requests
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/HTTP-Request-Params
Source0:	https://cpan.metacpan.org/authors/id/K/KI/KIZ/HTTP-Request-Params-%{version}.tar.gz
Patch0:         perl-HTTP-Request-Params-1.01-fix-build.patch

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}
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
