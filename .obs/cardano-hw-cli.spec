#
# spec file for package cardano-hw-cli
#
# Copyright (c) 2022 PERLUR Group
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%global pkg_name cardano-hw-cli
%global pkg_version 1.9.1
%bcond_with tests
Name:     %{pkg_name}
Version:	%{pkg_version}
Release:	0
License:	MIT
Summary:	Parse argument options
Url:	    https://github.com/vacuumlabs/cardano-hw-cli
Group:	  Development/Libraries/Other

Source:	%{name}-%{version}.tar.xz
BuildRequires:	nodejs
BuildRequires:	nodejs-packaging 
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:	    noarch
%{?nodejs_requires}

%description
This module is the guts of optimist's argument parser 
without all the fanciful decoration.

%prep
%setup -q -n minimist-%{version}

%build

%install
%nodejs_install
rm %{buildroot}%{nodejs_modulesdir}/minimist/LICENSE
rm %{buildroot}%{nodejs_modulesdir}/minimist/readme.markdown

%files
%defattr(-,root,root)
%doc LICENSE readme.markdown
%{nodejs_modulesdir}/minimist

%changelog
