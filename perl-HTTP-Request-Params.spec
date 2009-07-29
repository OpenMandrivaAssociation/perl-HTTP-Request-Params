%define upstream_name	 HTTP-Request-Params
%define upstream_version 1.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Retrieve GET/POST Parameters from HTTP Requests
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Email::MIME::Modifier)
BuildRequires:	perl(CGI)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:  perl(Email::Simple)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This software does all the dirty work of parsing HTTP Requests to find incoming
query parameters.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/HTTP
%{_mandir}/*/*
