Name     : jdk-arpack_combined_all
Version  : 0.1
Release  : 1
URL      : http://repo2.maven.org/maven2/net/sourceforge/f2j/arpack_combined_all/0.1/arpack_combined_all-0.1.jar
Source0  : http://repo2.maven.org/maven2/net/sourceforge/f2j/arpack_combined_all/0.1/arpack_combined_all-0.1.jar
Source1  : http://repo2.maven.org/maven2/net/sourceforge/f2j/arpack_combined_all/0.1/arpack_combined_all-0.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: jdk-arpack_combined_all-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-arpack_combined_all package.
Group: Data

%description data
data components for the jdk-arpack_combined_all package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/arpack_combined_all.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/arpack_combined_all.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/arpack_combined_all.xml \
%{buildroot}/usr/share/maven-poms/arpack_combined_all.pom \
%{buildroot}/usr/share/java/arpack_combined_all.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/arpack_combined_all.jar
/usr/share/maven-metadata/arpack_combined_all.xml
/usr/share/maven-poms/arpack_combined_all.pom
