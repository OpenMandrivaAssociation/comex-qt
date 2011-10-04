Summary:   QT user interface for comex project
Name:      comex-qt
Version:   0.1.6.0
Release:   %mkrel 1
License:   GPLv2
#ExcludeArch: ppc64
Group:     Office
Source:    http://comex-project.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL:       http://comex-project.googlecode.com/
BuildArch: noarch
# don't generate debug file because is empty
# % define debug_package %{nil}

BuildRequires: mono
BuildRequires: log4net-devel
BuildRequires: comex-base-devel >= 0.1.8.4
BuildRequires: qyoto
BuildRequires: qyoto-devel
BuildRequires: pinentry-qt4
BuildRequires: pkgconfig

Requires: mono
Requires: log4net
Requires: comex-base >= 0.1.8.4
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
* Thu Sep 29 2011 Armando Basile <hmandevteam@gmail.com> 0.1.6.0-1mdv2012.0
- release 0.1.6.0

* Thu Sep 01 2011 Armando Basile <hmandevteam@gmail.com> 0.1.5.2-1mdv2012.0
- release 0.1.5.2
