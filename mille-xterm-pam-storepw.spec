Summary:	Pluggable Authentication Module for storing user password
Name:		mille-xterm-pam-storepw
Version:	1.0
Release:	%mkrel 3
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


