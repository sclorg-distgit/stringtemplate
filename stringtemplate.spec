%{?scl:%scl_package stringtemplate}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

Summary: A Java template engine
Name: %{?scl_prefix}stringtemplate
Version: 3.2.1
Release: 11.1%{?dist}
URL: http://www.stringtemplate.org/
Source0: http://www.stringtemplate.org/download/stringtemplate-%{version}.tar.gz
# Build jUnit tests + make the antlr2 generated code before preparing sources
Patch0: stringtemplate-3.1-build-junit.patch
License: BSD
Group: Development/Libraries
BuildArch: noarch
BuildRequires: %{?scl_prefix_java_common}ant-antlr, %{?scl_prefix_java_common}ant-junit
BuildRequires: %{?scl_prefix_java_common}antlr-tool
# Standard deps

BuildRequires: %{?scl_prefix_java_common}jpackage-utils
Requires: %{?scl_prefix_java_common}antlr-tool

%description
StringTemplate is a java template engine (with ports for 
C# and Python) for generating source code, web pages,
emails, or any other formatted text output. StringTemplate
is particularly good at multi-targeted code generators,
multiple site skins, and internationalization/localization.

%package        javadoc
Summary:        API documentation for %{pkg_name}
Group:          Documentation
Requires:       java-javadoc

%description    javadoc
API documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%setup -n %{pkg_name}-%{version} -q
%patch0
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
rm -rf lib target
ant jar
ant javadocs -Dpackages= -Djavadocs.additionalparam=
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
install -D build/stringtemplate.jar $RPM_BUILD_ROOT%{_datadir}/java/stringtemplate.jar
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{pkg_name}
cp -pR docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{pkg_name}

install -Dpm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{pkg_name}.pom
%add_maven_depmap JPP-%{pkg_name}.pom stringtemplate.jar
%{?scl:EOF}


%files -f .mfiles
%doc LICENSE.txt README.txt

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{pkg_name}

%changelog
* Tue Jul 07 2015 Mat Booth <mat.booth@redhat.com> - 3.2.1-11.1
- Import latest from Fedora

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Sep 05 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 3.2.1-10
- Fix for F21 XMvn changes (#1107380)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 3.2.1-8
- Use Requires: java-headless rebuild (#1067528)

* Wed Aug 14 2013 Mat Booth <fedora@matbooth.co.uk> - 3.2.1-7
- Fix FTBFS #993386

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 1 2013 Conrad Meyer <konrad@tylerc.org> - 3.2.1-5
- Add missing dep on antlr-tool (#904979)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 29 2010 Miloš Jakubíček <xjakub@fi.muni.cz> - 3.2.1-1
- Update to 3.2.1
- Supply maven POM files
- Drop stringtemplate-3.1-disable-broken-test.patch (merged upstream)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Apr 05 2008 Colin Walters <walters@redhat.com> - 3.1-1
- First version
