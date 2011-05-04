Summary: GUI login manager for LXDE
Name: lxdm
Version: 0.2.0
Release: %mkrel 2
License: GPLv2+
Group: Graphical desktop/Other
Source0: http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
Source1: 27%{name}.conf
Patch0: lxdm-0.2.0-mdv-customization.patch
URL: http://www.lxde.org
BuildRequires: intltool
BuildRequires: consolekit-devel
BuildRequires: libxmu-devel
BuildRequires: pam-devel
BuildRequires: iso-codes
BuildRequires: gtk+2-devel
Requires: iso-codes
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A lightweight dropped-in replacement for GDM or KDM.

%prep
%setup -q
%patch0 -p0 -b .mdv
rm -f data/lxdm.conf

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# dm conf file
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/X11/dm.d/27%{name}.conf

%{find_lang} %{name}

%files -f %{name}.lang
%defattr(-, root, root)
%dir %{_sysconfdir}/lxdm
%{_sysconfdir}/lxdm/Xsession
%config(noreplace) %{_sysconfdir}/lxdm/lxdm.conf
%config(noreplace) %{_sysconfdir}/lxdm/LoginReady
%config(noreplace) %{_sysconfdir}/lxdm/PostLogin
%config(noreplace) %{_sysconfdir}/lxdm/PostLogout
%config(noreplace) %{_sysconfdir}/lxdm/PreLogin
%config(noreplace) %{_sysconfdir}/lxdm/PreReboot
%config(noreplace) %{_sysconfdir}/lxdm/PreShutdown
%config(noreplace) %{_datadir}/X11/dm.d/27%{name}.conf
%{_sysconfdir}/pam.d/*
%{_libexecdir}/lxdm-greeter-gtk
%{_sbindir}/lxdm*
%{_datadir}/%{name}
