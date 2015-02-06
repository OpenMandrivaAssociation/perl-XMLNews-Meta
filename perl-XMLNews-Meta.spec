%define module 	XMLNews-Meta
%define version 0.01
%define release 13

Summary:	%{module} perl module
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel 
BuildRequires:  perl(XML::Parser)
Requires:	perl 
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
Buildarch:	noarch

%description
%{module} - module designed to read and write an XML-based news metadata

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install

make PREFIX=$RPM_BUILD_ROOT%{_prefix} install DESTDIR=$RPM_BUILD_ROOT

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README MANIFEST Changes
%{perl_vendorlib}/XMLNews/
%_mandir/*/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.01-11mdv2010.0
+ Revision: 430665
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.01-10mdv2009.0
+ Revision: 268883
- rebuild early 2009.0 package (before pixel changes)

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-9mdv2009.0
+ Revision: 210962
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.01-8mdv2008.0
+ Revision: 23513
- rebuild


* Fri May 12 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.01-7mdk
- Fix Build
- Fix BuildRequires
- Fix Source URL
- use mkrel

* Tue Jun 29 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.01-6mdk
- rebuild

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.01-5mdk
- rebuild for new auto{prov,req}

