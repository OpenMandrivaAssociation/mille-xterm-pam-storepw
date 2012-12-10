Summary:	Pluggable Authentication Module for storing user password
Name:		mille-xterm-pam-storepw
Version:	1.0
Release:	%mkrel 7
License:	GPL
Group:		Networking/Other
URL:		http://silicon-verl.de/home/flo/software/pamcifs.html
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	pam-devel
BuildRequires:	perl
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
pam_storepw is a PAM module to store the user's password. It is used to
mount drives, use remote printers and generally connect to services where
the user would usually need to re-authenticate. The module stores the user
password in /var/run/pw/<USER>.

%prep

%setup -q 
perl -pi -e "s/-lpam_misc/-lpam_misc -lc/;" libpam-storepw-*/Makefile

%build
cd libpam-storepw-*/

%make CFLAGS="%{optflags} -fPIC"

%install
rm -rf %{buildroot}

install -d %{buildroot}/%{_lib}/security
install -d %{buildroot}/var/run/pw

install -m0755 libpam-storepw-*/pam_storepw.so %{buildroot}/%{_lib}/security

%clean
rm -rf %{buildroot}

%files 
%defattr(0644,root,root,0755)
%doc README AUTHORS Changelog COPYING INSTALL
/%{_lib}/security/pam_storepw*.so
%dir /var/run/pw




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-7mdv2011.0
+ Revision: 620335
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0-6mdv2010.0
+ Revision: 430033
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.0-5mdv2009.0
+ Revision: 252465
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0-3mdv2008.1
+ Revision: 136579
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-3mdv2008.0
+ Revision: 89930
- rebuild


* Thu Feb 08 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-2mdv2007.0
+ Revision: 117841
- bump release
- it needs fpic on x86_64
- Import mille-xterm-pam-storepw

* Fri Sep 29 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdk
- initial Mandriva package (mille-xterm import)

