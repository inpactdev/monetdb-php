Name:		php-monetdb
Version:	1.0
Release:	3%{?dist}
Summary:	MonetDB php interface
Group: Applications/Databases

License:	MPLv2.0
URL:		http://www.monetdb.org/
Source0:	http://dev.monetdb.org/php/monetdb-php-%{version}.tar.bz2

Requires:	php-cli
Requires:	php-sockets
BuildArch:	noarch

Obsoletes:	MonetDB-client-php
%if (0%{?fedora} >= 22)
# no recommendations on old Fedora or RHEL
Recommends:	MonetDB-SQL-server5
%endif

%description
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package contains the files needed to use MonetDB from a PHP
program.


%prep
%autosetup -n monetdb-php-%{version}


%build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license COPYING.txt
%defattr(-,root,root)
%dir %{_datadir}/php/monetdb
%{_datadir}/php/monetdb/*



%changelog
* Mon Feb 13 2017 Sjoerd Mullender <sjoerd@acm.org> - 1.0-2
- Added full license text.

* Wed Sep 14 2016 Sjoerd Mullender <sjoerd@acm.org> - 1.0-1
- Initial independent version.

