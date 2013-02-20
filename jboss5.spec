Name            : jbossas5
Version         : 5.1.0.GA
Release         : 1
Group           : Internet/WWW/Servers
Summary         : JBoss Application Server
Vendor          : Red Hat
URL             : http://www.jboss.org/
BuildArch       : noarch
License         : LGPL
Source0         : http://downloads.sourceforge.net/project/jboss/JBoss/JBoss-5.1.0.GA/jboss-%{version}-jdk6.zip
Source1         : jboss_init_redhat.sh
BuildRoot       : %{_tmppath}/%{name}-%{version}-root
Requires        : shadow-utils
Requires(post)  : chkconfig
Requires(preun) : chkconfig
Requires(preun) : initscripts
Requires(postun): initscripts
 
%description
JBoss Application Server (or JBoss AS) is a free software/open-source
Java EE-based application server. An important distinction for this
class of software is that it not only implements a server that runs
on Java, but it actually implements the Java EE part of Java. Because
it is Java-based, the JBoss application server operates cross-platform:
usable on any operating system that supports Java. 
 
JBoss AS was developed by JBoss, now a division of Red Hat.
 
%prep
%setup -n jboss-%{version}
 
%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/opt/%{name}
cp -R . %{buildroot}/opt/%{name}
install -d -m 755 %{buildroot}%{_initrddir}
install -p -m 755 "%{SOURCE1}" %{buildroot}%{_initrddir}/%{name}
rm -rf %{buildroot}/opt/%{name}/server/*/deploy/ROOT.war
mkdir %{buildroot}/opt/%{name}/server/default/undeploy
mv %{buildroot}/opt/%{name}/server/default/deploy/admin-console.war \
	%{buildroot}/opt/%{name}/server/default/undeploy
mv %{buildroot}/opt/%{name}/server/default/deploy/jmx-console.war \
	%{buildroot}/opt/%{name}/server/default/undeploy
mv %{buildroot}/opt/%{name}/server/default/deploy/jbossws.sar \
	%{buildroot}/opt/%{name}/server/default/undeploy
mv %{buildroot}/opt/%{name}/server/default/deploy/jmx-remoting.sar \
	%{buildroot}/opt/%{name}/server/default/undeploy
mv %{buildroot}/opt/%{name}/server/default/deploy/profileservice-secured.jar \
	%{buildroot}/opt/%{name}/server/default/undeploy
mv %{buildroot}/opt/%{name}/server/default/deploy/xnio-provider.jar \
	%{buildroot}/opt/%{name}/server/default/undeploy
 
%clean
rm -rf %{buildroot}
 
%files
%defattr(-,jboss,jboss)
/opt/%{name}
%attr(0755,root,root) %{_initrddir}/%{name}
 
%pre
getent group jboss >/dev/null || groupadd -r jboss
getent passwd jboss >/dev/null || \
    useradd -r -g jboss -d /opt/${name} -s /bin/bash -c "JBoss AS Daemon" jboss
exit 0

%post
chkconfig --add %{name}
echo "Installation complete."

%preun
if [ $1 = 0 ] ; then
   service %{name} stop >/dev/null 2>&1 || :
   chkconfig --del %{name}
fi

%postun
if [ "$1" -ge "1" ] ; then
   service %{name} restart >/dev/null 2>&1 || :
fi

%changelog
* Mon Dec 6 2010 Martin Jackson 5.1.0.GA-1
- Initial creation