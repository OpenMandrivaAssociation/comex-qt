Summary:   QT user interface for comex project
Name:      comex-qt
Version:   0.1.6.2
Release:   2
License:   GPLv2
#ExcludeArch: ppc64
Group:     Office
Source:    http://comex-project.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL:       https://comex-project.googlecode.com/
BuildArch: noarch
# don't generate debug file because is empty
# % define debug_package %{nil}

BuildRequires: mono
BuildRequires: log4net-devel
BuildRequires: comex-base-devel >= 0.1.8.5
BuildRequires: qyoto
BuildRequires: qyoto-devel
BuildRequires: pinentry-qt4
BuildRequires: pkgconfig

Requires: mono
Requires: log4net
Requires: comex-base >= 0.1.8.5
Requires: qyoto
Requires: qyoto-devel


%description
Is QT user interface of a simple application that can be used to exchange
data with smartcards using PC/SC standard readers or smartmouse
phoenix serial reader.


%prep
%setup -q

%build
%configure2_5x --libdir=%_prefix/lib 
%make

%install
rm -fr %{buildroot}
%makeinstall_std


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc copying.gpl comex-qt/readme
%{_bindir}/%{name}
%_prefix/lib/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop



%changelog
* Sun Oct 30 2011 Armando Basile <hman@mandriva.org> 0.1.6.2-1
+ Revision: 707882
- release 0.1.6.2

* Tue Oct 04 2011 Armando Basile <hman@mandriva.org> 0.1.6.0-1
+ Revision: 702989
- removed changelog section from spec file
- added tarball
- release 0.1.6.0

* Mon Sep 26 2011 Armando Basile <hman@mandriva.org> 0.1.5.2-2
+ Revision: 701399
- added qyoto-devel as requires, qyoto use libqyoto.so that is in qyoto-devel package
- import comex-qt

