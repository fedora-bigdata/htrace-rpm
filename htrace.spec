%global commit 7e8fe1aa4983469f46cbbc5e6dd8e31753ba85f0
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: htrace
Version: 2.03
Release: 1%{?dist}
Summary: Tracing framework for java based distributed systems
License: ASL 2.0
URL: http://github.com/cloudera/htrace
Source0: https://github.com/cloudera/htrace/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Patch0: htrace-fedora-jetty.patch
BuildRequires: java-devel
BuildRequires: jetty-util-ajax
BuildRequires: libthrift-java
BuildRequires: maven-local
Requires: java
BuildArch: noarch

%description
HTrace is a tracing framework intended for use with distributed systems
written in java. 

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -qn %{name}-%{commit}

%patch0 -p1

# Remove apache-rat-plugin because it causes build failure on xmvn generated
# files
%pom_remove_plugin org.apache.rat:apache-rat-plugin
%pom_remove_plugin org.apache.rat:apache-rat-plugin htrace-core
%pom_remove_plugin org.apache.rat:apache-rat-plugin htrace-zipkin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Oct  8 2013 Robert Rati <rrati@redhat> - 2.03-1
- Initial rpm
