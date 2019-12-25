Name:           envconsul
Version:        0.9.1
Release:        1%{?dist}
Summary:        envconsul provides a convenient way to populate values from Consul into environment variables using the envconsul daemon.
Group:          Applications/System
License:        MPLv2.0
URL:            https://releases.hashicorp.com/hashicorp/%{name}
Source0:        https://releases.hashicorp.com/%{name}/%{version}/%{name}_%{version}_linux_amd64.tgz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
%endif

%description
envconsul provides a convenient way to populate values from Consul into process environment variables using the envconsul daemon.

The envconsul daemon allows you to configure applications with environment variables without knowing the existence of Consul. 

This greatly simplifies the configuration of applications.

%prep
%setup -q -c

%install
mkdir -p %{buildroot}/%{_bindir}
cp %{_builddir}/%{name}-%{version}/%{name} %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/%{name}

%doc

%changelog
* Wed Dec 25 2019 Valeriy Krasnikov <kww580@gmail.com>
- init v0.9.1
