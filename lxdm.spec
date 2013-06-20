Summary:	GUI login manager for LXDE
Name:		lxdm
Version:	0.4.2
%define	gitdate	20121019
Release:	0.%{gitdate}.2
License:	GPLv2+
Group:		Graphical desktop/Other
Source0:	http://dfn.dl.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.xz
Source1:	27%{name}.conf
Patch0:		lxdm-0.2.0-mdv-customization.patch
Patch1:		lxdm-0.4.1-ui-src.patch
URL:		http://www.lxde.org
BuildRequires:	intltool
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pam-devel
BuildRequires:	iso-codes
BuildRequires:	pkgconfig(gtk+-x11-2.0)
BuildRequires:	pkgconfig(systemd)
Requires:	iso-codes

%description
A lightweight dropped-in replacement for GDM or KDM.

%prep
%setup -q
%patch0 -p0 -b .mdv~
%patch1 -p0 -b .ui~
rm data/lxdm.conf

%build
%configure2_5x	--disable-consolekit
%make

%install
%makeinstall_std

# dm conf file
install -m644 %{SOURCE1} -D %{buildroot}%{_datadir}/X11/dm.d/27%{name}.conf

%find_lang %{name}

%files -f %{name}.lang
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
%{_bindir}/lxdm-config
%{_libdir}/lxdm-greeter-gdk
%{_libdir}/lxdm-numlock
%{_unitdir}/lxdm.service

%changelog
* Tue Aug 02 2011 Александр Казанцев <kazancas@mandriva.org> 0.4.1-1mdv2012.0
+ Revision: 692766
- update to 0.4.1

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-2
+ Revision: 666112
- mass rebuild

  + Funda Wang <fwang@mandriva.org>
    - New version 0.2.0

* Wed Mar 10 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.1.0-4mdv2010.1
+ Revision: 517380
- add %%{_datadir}/X11/dm.d/27%%{name}.conf to make lxdm get listed in drakedm
- change mdv-customiztion patch to make lxdm use Ia Ora (Arctic for the moment)

* Fri Jan 15 2010 Funda Wang <fwang@mandriva.org> 0.1.0-3mdv2010.1
+ Revision: 491595
- bump rel
- use mandriva background
- update desc

* Tue Jan 12 2010 Funda Wang <fwang@mandriva.org> 0.1.0-2mdv2010.1
+ Revision: 490043
- requiresiso-codes
- import lxdm
