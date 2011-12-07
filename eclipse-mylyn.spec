%if 0%{?rhel} >= 6
%global debug_package %{nil}
%endif

%define eclipse_base        %{_libdir}/eclipse
%define install_loc         %{eclipse_base}/dropins
# Taken from update site so we match upstream
# http://download.eclipse.org/tools/mylyn/update/e3.5/
%define qualifier           v20100222-0100-e3x

# Prevent brp-java-repack-jars from being run.  Spaces in the paths of
# the help content are broken by it.
%define __jar_repack 0

Name: eclipse-mylyn
Summary: Mylyn is a task-focused UI for Eclipse
Version: 3.3.2
Release: 4.5%{?dist}
License: EPL and ASL 2.0
URL: http://www.eclipse.org/mylyn

# mkdir temp && cd temp
# sh fetch-mylyn.sh
Source0: org.eclipse.mylyn-R_3_3_2-fetched-src.tar.bz2
Source1: fetch-mylyn.sh

# This is a dependency declared by the Orbit xmlrpc JAR.  We don't use
# their JAR and the part of Mylyn using xmlrpc isn't using the
# javax.xml.bind-using part(s) of xmlrpc.
# This patch is not suitable for upstream.
Patch0: %{name}-nojaxb.patch
# Our xmlrpc packages are split into JARs differently than Orbit
# This patch is not suitable for upstream.
Patch1: %{name}-splitxmlrpc.patch
Patch2: %{name}-wikitext_builddoc.patch

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:    java-devel >= 1.5.0

%if 0%{?rhel} >= 6
ExclusiveArch: i686 x86_64
%else
BuildArch: noarch
%endif

BuildRequires: eclipse-pde >= 1:3.4.0
BuildRequires: eclipse-cdt
BuildRequires: jakarta-commons-lang >= 2.3-2.3
BuildRequires: ws-commons-util >= 1.0.1-5
BuildRequires: xmlrpc3-client >= 3.0-2.8
BuildRequires: xmlrpc3-common >= 3.0-2.8
BuildRequires: ws-jaxme >= 0.5.1-2.4
BuildRequires: rome
BuildRequires: jdom >= 1.0-5.5
Requires: eclipse-platform >= 1:3.4.0
Requires: jakarta-commons-lang >= 2.3-2.3
Requires: ws-commons-util >= 1.0.1-5
Requires: xmlrpc3-client >= 3.0-2.8
Requires: xmlrpc3-common >= 3.0-2.8
Requires: ws-jaxme >= 0.5.1-2.4
Provides: eclipse-mylar = 2.0.0-1.fc7
Obsoletes: eclipse-mylar < 2.0.0
Provides: eclipse-mylyn-ide = %{version}-%{release}
Obsoletes: eclipse-mylyn-ide < 3.0.0
Provides: eclipse-bugzilla = 1:0.2.4-4.fc6
Obsoletes: eclipse-bugzilla < 1:0.2.5
Provides: eclipse-mylar-bugzilla = 2.0.0-1.fc7
Obsoletes: eclipse-mylar-bugzilla < 2.0.0
Provides: eclipse-mylyn-bugzilla = %{version}-%{release}
Obsoletes: eclipse-mylyn-bugzilla < 3.0.0

Group: Development/Tools

%description
Mylyn integrates task support into Eclipse.  It supports offline editing
for certain task repositories and monitors work activity to hide
information that is not relevant to the current task.  Also included is
the Mylyn Focused UI for reducing information overload when working with
tasks and the Bugzilla task connector.

%package  trac
Summary:  Mylyn Trac Connector
Requires: %{name} = %{version}-%{release}
Group: Development/Tools
Provides: eclipse-mylar-trac = 2.0.0-1.fc7
Obsoletes: eclipse-mylar-trac < 2.0.0

%description trac
Trac client integrated with Eclipse and Mylyn; can be used standalone.

%package  java
Summary:  Mylyn Bridge:  Java Development
Requires: eclipse-jdt
Requires: %{name}-ide = %{version}-%{release}
Group: Development/Tools

%description java
Mylyn Task-Focused UI extensions for JDT.  Provides focusing of Java
element views and editors.

%package  pde
Summary:  Mylyn Bridge:  Plug-in Development
Requires: eclipse-pde
Requires: %{name}-java = %{version}-%{release}
Group: Development/Tools

%description pde
Mylyn Task-Focused UI extensions for PDE, Ant, Team Support and CVS.

%package  webtasks
Summary:  Mylyn Connector:  Web Templates
Requires: %{name} = %{version}-%{release}
Requires: rome
Requires: jdom
Group: Development/Tools

%description webtasks
Provides Task List integration for several web-based issue trackers
and templates for example projects.

%package  wikitext
Summary:  Mylyn WikiText
Requires: %{name} = %{version}-%{release}
Group: Development/Tools

%description wikitext
Enables parsing and display of lightweight markup (wiki text).  Extends
the Mylyn task editor to create a markup-aware editor.

%package  cdt
Summary:  Mylyn Bridge:  C/C++ Development
Requires: %{name} = %{version}-%{release}
Requires: eclipse-cdt
Group: Development/Tools
Provides: eclipse-cdt-mylyn = 1:6.0.1-5.fc13
Obsoletes: eclipse-cdt-mylyn <= 1:6.0.1-5.fc13

%description cdt
Mylyn Task-Focused UI extensions for CDT.  Provides focusing of C/C++
element views and editors.

%prep
%setup -q -n org.eclipse.mylyn

# The tests have dependencies we don't need/want/have
rm -rf *tests*

mkdir orbitDeps
pushd orbitDeps
ln -s %{_javadir}/commons-lang.jar org.apache.commons.lang_2.4.0.jar
ln -s %{_javadir}/commons-logging-api.jar org.apache.commons.logging.api_1.0.4.jar
ln -s %{_javadir}/xmlrpc3-client-3.0.jar org.apache.xmlrpc.client_3.0.0.v20080530-1550.jar
ln -s %{_javadir}/xmlrpc3-common-3.0.jar org.apache.xmlrpc.common_3.0.0.v20080530-1550.jar
ln -s %{_javadir}/ws-commons-util-1.0.1.jar org.apache.ws.commons.util_1.0.0.v20080530-1550.jar
ln -s %{_javadir}/jdom.jar org.jdom_1.0.0.v200806100616.jar
ln -s %{_javadir}/rome-0.9.jar com.sun.syndication_0.9.0.v200803061811.jar
ln -s %{_javadir}/jaxme/jaxmeapi.jar javax.xml.bind.jar
popd

#javax.activation_1.1.0.v200806101325.jar
#javax.xml.bind_2.0.0.v20080604-1500.jar
#javax.mail_1.4.0.v200804091730.jar
#javax.servlet_2.4.0.v200806031604.jar
#org.apache.ant_1.7.0.v200803061910.zip,unpack=true
#javax.xml.rpc_1.1.0.v200806030420.zip,unpack=true
#javax.wsdl_1.5.1.v200806030408.jar
#javax.xml.soap_1.2.0.v200806030421.zip,unpack=true
#org.apache.axis_1.4.0.v200806030120.zip,unpack=true
#org.apache.commons.discovery_0.2.0.v200806030120.zip,unpack=true

%patch0
%patch1
%patch2

sed -i 's|bundle-version="2.3.0"|bundle-version="[2.3.0,3.0.0)"|g' org.eclipse.mylyn.commons.net/META-INF/MANIFEST.MF

find -name feature.xml |
  while read f; do
      sed -i "s/qualifier/%{qualifier}/g" $f
  done

%build
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar \
 -o `pwd`/orbitDeps
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.context_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar \
 -o `pwd`/orbitDeps
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.team_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar \
 -o `pwd`/orbitDeps
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.bugzilla_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar \
 -o `pwd`/orbitDeps
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.ide_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar \
 -o `pwd`/orbitDeps
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.trac_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar \
 -o `pwd`/orbitDeps
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.java_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar \
 -o `pwd`/orbitDeps
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.pde_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar \
 -o `pwd`/orbitDeps
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.web.tasks_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar \
 -o `pwd`/orbitDeps
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.wikitext_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar \
 -o `pwd`/orbitDeps
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.cdt.mylyn \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar \
 -o `pwd`/orbitDeps -d "cdt"

%install
rm -rf %{buildroot}
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}/mylyn
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}/mylyn-java
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}/mylyn-pde
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}/mylyn-trac
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}/mylyn-webtasks
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}/mylyn-wikitext

unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn \
 build/rpmBuild/org.eclipse.mylyn_feature.zip
unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn \
 build/rpmBuild/org.eclipse.mylyn.bugzilla_feature.zip
unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn \
 build/rpmBuild/org.eclipse.mylyn.context_feature.zip
unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn \
 build/rpmBuild/org.eclipse.mylyn.team_feature.zip
unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn \
 build/rpmBuild/org.eclipse.mylyn.ide_feature.zip
unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn-trac \
 build/rpmBuild/org.eclipse.mylyn.trac_feature.zip
unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn-java \
 build/rpmBuild/org.eclipse.mylyn.java_feature.zip
unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn-pde \
 build/rpmBuild/org.eclipse.mylyn.pde_feature.zip
unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn-webtasks \
 build/rpmBuild/org.eclipse.mylyn.web.tasks_feature.zip
unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn-wikitext \
 build/rpmBuild/org.eclipse.mylyn.wikitext_feature.zip
unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn-cdt \
 build/rpmBuild/org.eclipse.cdt.mylyn.zip

pushd $RPM_BUILD_ROOT%{install_loc}/mylyn/eclipse/plugins
rm org.apache.commons.codec_*.jar
rm org.apache.commons.httpclient_3.1.0.v20080605-1935.jar
rm org.apache.commons.lang_*.jar
rm org.apache.commons.logging_1.0.4.v20080605-1930.jar
ln -s %{_javadir}/commons-lang.jar org.apache.commons.lang_2.4.0.jar
ln -s %{_javadir}/commons-logging-api.jar org.apache.commons.logging.api_1.0.4.jar
popd

pushd $RPM_BUILD_ROOT%{install_loc}/mylyn-trac/eclipse/plugins
rm org.apache.ws.commons.util_1.0.0.%{qualifier}.jar
rm org.apache.xmlrpc_3.0.0.%{qualifier}.jar
ln -s %{_javadir}/xmlrpc3-client-3.0.jar org.apache.xmlrpc.client_3.0.0.v20080530-1550.jar
ln -s %{_javadir}/xmlrpc3-common-3.0.jar org.apache.xmlrpc.common_3.0.0.v20080530-1550.jar
ln -s %{_javadir}/ws-commons-util-1.0.1.jar org.apache.ws.commons.util_1.0.0.v20080530-1550.jar
ln -s %{_javadir}/jaxme/jaxmeapi.jar javax.xml.bind.jar
popd

#Do not use qualifier value for dependencies to not be forced to rebuild them for
# every mylyn
pushd $RPM_BUILD_ROOT%{install_loc}/mylyn-trac/eclipse/features
	find -name feature.xml |
	while read f; do
      sed -i "s/3.0.0.%{qualifier}/3.0.0.qualifier/g" $f
      sed -i "s/1.0.0.%{qualifier}/1.0.0.qualifier/g" $f
  	done
popd

pushd $RPM_BUILD_ROOT%{install_loc}/mylyn-webtasks/eclipse/plugins
rm org.jdom_*.jar
rm com.sun.syndication_0.9.0.v200803061811.jar
ln -s %{_javadir}/jdom.jar org.jdom_1.0.0.v200806100616.jar
ln -s %{_javadir}/rome-0.9.jar com.sun.syndication_0.9.0.v200803061811.jar
popd

%clean
rm -rf %{buildroot}

%files webtasks
%defattr(-,root,root,-)
%{install_loc}/mylyn-webtasks

%files wikitext
%defattr(-,root,root,-)
%{install_loc}/mylyn-wikitext

%files trac
%defattr(-,root,root,-)
%{install_loc}/mylyn-trac
# FIXME:  add the doc files back
#%doc %{install_loc}/features/org.eclipse.mylyn.trac_feature_*/license.html
#%doc %{install_loc}/features/org.eclipse.mylyn.trac_feature_*/epl-v10.html
#%doc %{install_loc}/features/org.eclipse.mylyn.trac_feature_*/about.html

%files java
%defattr(-,root,root,-)
%{install_loc}/mylyn-java
# FIXME:  add the doc files back
#%doc %{install_loc}/features/org.eclipse.mylyn.java_feature_*/license.html
#%doc %{install_loc}/features/org.eclipse.mylyn.java_feature_*/epl-v10.html
#%doc %{install_loc}/features/org.eclipse.mylyn.java_feature_*/about.html

%files pde
%defattr(-,root,root,-)
%{install_loc}/mylyn-pde
# FIXME:  add the doc files back
#%doc %{install_loc}/features/org.eclipse.mylyn.pde_feature_*/license.html
#%doc %{install_loc}/features/org.eclipse.mylyn.pde_feature_*/epl-v10.html
#%doc %{install_loc}/features/org.eclipse.mylyn.pde_feature_*/about.html

%files cdt
%defattr(-,root,root,-)
%{install_loc}/mylyn-cdt

%files
%defattr(-,root,root,-)
%{install_loc}/mylyn
# FIXME:  add the doc files back

%changelog
* Wed Mar 24 2010 Alexander Kurtakov <jjohnstn@redhat.com> 3.3.2-4.5
- Resolves: #557613
- Install into %%{_libdir}/eclipse/dropins now that we are no longer noarch.

* Tue Mar 23 2010 Alexander Kurtakov <akurtako@redhat.com> 3.3.2-4.4
- Fix jdom symlinking.

* Tue Mar 23 2010 Alexander Kurtakov <akurtako@redhat.com> 3.3.2-4.3
- Really fix commons-lang symlinking.

* Tue Mar 23 2010 Alexander Kurtakov <akurtako@redhat.com> 3.3.2-4.2
- Fix commons lang symlinking.

* Tue Mar 23 2010 Alexander Kurtakov <akurtako@redhat.com> 3.3.2-4.1
- Rebase to 3.3.2.

* Fri Feb 12 2010 Andrew Overholt <overholt@redhat.com> 3.3.1-2.4
- Don't build debuginfo if building arch-specific packages.

* Thu Jan 21 2010 Andrew Overholt <overholt@redhat.com> 3.3.1-2.3
- Make arch-specific.

* Thu Jan 07 2010 Andrew Overholt <overholt@redhat.com> 3.3.1-2.2
- Remove unnecessary unzipping of recently removed SOURCE2.

* Thu Jan 07 2010 Andrew Overholt <overholt@redhat.com> 3.3.1-2.1
- Remove Fedora customizations (adding bugzilla instances).

* Thu Jan 07 2010 Andrew Overholt <overholt@redhat.com> 3.3.1-2
- Update license field to add ASL 2.0 for wikitext.

* Thu Dec 17 2009 Alexander Kurtakov <akurtako@redhat.com> 3.3.1-1
- Update to 3.3.1 version.

* Sun Nov 22 2009 Alexander Kurtakov <akurtako@redhat.com> 3.3.0-4
- Fix build with newer common-codec.

* Wed Oct 28 2009 Alexander Kurtakov <akurtako@redhat.com> 3.3.0-3
- CDT subpackage obsoletes eclipse-cdt-mylyn.

* Tue Oct 27 2009 Alexander Kurtakov <akurtako@redhat.com> 3.3.0-2
- Fix cdt description. Bump qualifier to be newer than Galileo update site.

* Tue Oct 27 2009 Alexander Kurtakov <akurtako@redhat.com> 3.3.0-1
- Update to 3.3.0.
- Add cdt bridge.
- Remove BR/R which are required by eclipse itself now.

* Tue Sep 22 2009 Alexander Kurtakov <akurtako@redhat.com> 3.2.1-2
- Add patch for correct building of o.e.wikitext.help.ui.

* Tue Aug 4 2009 Alexander Kurtakov <akurtako@redhat.com> 3.2.1-1
- Update to 3.2.1.

* Wed Apr 22 2009 Andrew Overholt <overholt@redhat.com> 3.1.1-1
- 3.1.1
- Bug fixes from 3.1.0:  http://tinyurl.com/mylyn-3-1-1bugs
- Remove wikitext build patch that has been merged upstream.

* Wed Mar 25 2009 Alexander Kurtakov <akurtako@redhat.com> 3.1.0-3
- Fix documentation build.

* Mon Mar 23 2009 Alexander Kurtakov <akurtako@redhat.com> 3.1.0-2
- Rebuild to not ship p2 context.xml.

* Tue Mar 17 2009 Andrew Overholt <overholt@redhat.com> 3.1.0-1
- 3.1.0
- Add wikitext sub-package.
- Update to new Fedora customizations plugin.
- Don't repack JARs as it breaks help content.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 9 2009 Andrew Overholt <overholt@redhat.com> 3.0.4-1
- 3.0.4

* Wed Nov 12 2008 Andrew Overholt <overholt@redhat.com> 3.0.3-4
- Add patch for e.o#239435 (rhbz#470356).

* Fri Oct 31 2008 Alexander Kurtakov <akurtako@redhat.com> 3.0.3-3
- Don't apply nojaxb.patch.
- Fix eclipse-mylyn-splitxmlrpc.patch to Import-Package:org.apache.xmlrpc.

* Tue Oct 21 2008 Alexander Kurtakov <akurtako@redhat.com> 3.0.3-2
- BR ws-jaxme.
- Bump xmlrpc3 requires for proper OSGi metadata.
- Fix trac feature.xml to not require different qualifier for the deps.

* Tue Oct 21 2008 Alexander Kurtakov <akurtako@redhat.com> 3.0.3-1
- 3.0.3.
- Rebase addfedoracustomizations.patch.

* Sat Oct 18 2008 Alexander Kurtakov <akurtako@redhat.com> 3.0.1-3
- Add >= for jdom to ensure proper OSGi metadata

* Mon Aug 11 2008 Andrew Overholt <overholt@redhat.com> 3.0.1-2
- Add >= for requirements to ensure proper OSGi metadata

* Fri Aug 08 2008 Andrew Overholt <overholt@redhat.com> 3.0.1-1
- Fix fuzz on adding Fedora customizations patch
- Add patch to make Red Hat bugzilla 3.0

* Thu Aug 07 2008 Andrew Overholt <overholt@redhat.com> 3.0.1-1
- Add webtasks sub-package

* Tue Aug 05 2008 Andrew Overholt <overholt@redhat.com> 3.0.1-1
- Update install locations
- Add qualifier hack for now

* Wed Jul 30 2008 Andrew Overholt <overholt@redhat.com> 3.0.1-1
- 3.0.1
- Add patch to not require jaxb (required by XML-RPC Orbit bundle)
- Fold -ide and -bugzilla into main package
- Add commented-out webtasks sub-package; to be enabled after rome
  review is complete

* Thu Jul 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.3.2-6
- fix license tag

* Wed May 14 2008 Andrew Overholt <overholt@redhat.com> 2.3.2-6
- ".qualifier" -> actual release qualifier in build (due to upstream
  build system change (e.o#108291, rh#446468).

* Tue Apr 15 2008 Andrew Overholt <overholt@redhat.com> 2.3.2-5
- Re-build to attempt to fix rhbz#442251 (broken cpio archive).

* Tue Apr 15 2008 Jesse Keating <jkeating@redhat.com> - 2.3.2-4
- Rebuild due to filesystem corruption

* Mon Apr 07 2008 Andrew Overholt <overholt@redhat.com> 2.3.2-3
- Fix commons-lang symlink.

* Mon Apr 07 2008 Andrew Overholt <overholt@redhat.com> 2.3.2-2
- Upload sources.

* Fri Apr 04 2008 Andrew Overholt <overholt@redhat.com> 2.3.2-1
- 2.3.2.
- Add jakarta-commons-lang dependency.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.1.0-2
- Autorebuild for GCC 4.3

* Wed Oct 24 2007 Andrew Overholt <overholt@redhat.com> 2.1.0-1
- 2.1.0
- Enable GNOME bugzilla by default

* Tue Oct 02 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-10
- Add %%post gcj blocks for sub-packages (thanks to David Walluck).
- Rename fetching script (s/mylar/mylyn/).

* Fri Sep 21 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-9
- Really remove all mylar references in mylyn feature - courtesy
  Mandriva package.

* Wed Sep 19 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-8
- Add patch and source to have common bugzilla servers by default.

* Tue Sep 18 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-7
- Fix filename of webcore jar.

* Tue Sep 18 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-6
- Re-add gcj support (accidentally removed the flag).

* Fri Sep 07 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-5
- Make web.core its own jar.
- Unpack web.core so we can symlink to dependencies.
- Symlink to dependencies of web.core.
- Remove rome jar and exports from web.core.
- BR/R all the versions of dependencies that have OSGi manifests.

* Fri Aug 24 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-4
- ExcludeArch ppc64 (no xmlrpc3 on ppc64 due to rh#239123).

* Thu Aug 23 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-3
- Add BR on eclipse-pde.

* Thu Aug 23 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-2
- Add BR and R on eclipse-cvs-client.

* Thu Aug 23 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-1
- Re-name to eclipse-mylyn.

* Fri Aug 10 2007 Ben Konrath <bkonrath@redhat.com> 2.0.0-1
- 2.0.0
- Add -java and -pde sub-packages.

* Wed Apr 25 2007 Andrew Overholt <overholt@redhat.com> 2.0-0.1.M2a.1
- 2.0M2a (a re-tag to fix some tagging issues).

* Wed Apr 18 2007 Andrew Overholt <overholt@redhat.com> 1.0-4
- Add workaround for missing method in GNU Classpath.

* Thu Apr 12 2007 Andrew Overholt <overholt@redhat.com> 1.0-3
- Add Obsoletes and Provides for eclipse-bugzilla on
  eclipse-mylar-bugzilla (comments in bug #222677).  If someone notices
  missing functionality to warrant removing the Provides, please file a
  bug.

* Tue Mar 20 2007 Andrew Overholt <overholt@redhat.com> 1.0-2
- Use xmlrpc3 jars instead of xmlrpc

* Fri Mar 16 2007 Andrew Overholt <overholt@redhat.com> 1.0-1
- Initial build
