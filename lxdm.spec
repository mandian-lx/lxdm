Summary:	GUI login manager for LXDE
Name:		lxdm
Version:	0.5.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://wiki.lxde.org/en/LXDM
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
Source1:	27%{name}.conf
Patch0:		lxdm-0.2.0-mdv-customization.patch
#Patch1:		lxdm-0.4.1-ui-src.patch

BuildRequires:	intltool
BuildRequires:	iso-codes
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(gtk+-x11-2.0)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(xmu)

Requires:	iso-codes
#Requires:       mkxauth

%description
Lightweight X11 Desktop Environment project (a.k.a LXDE) aimed to provide a
new desktop environment which is useful enough and keep resource usage lower
at the same time. Useabiliy, speed, and memory usage are our main concern.

Unlike other tightly integrated desktops LXDE strives to be modular, so each
component can be used independently with few dependencies. This makes
porting LXDE to different distributions and platforms easier.

LXDM is the lightweight display manager aimed to replace gdm in LXDE
distros. The UI is implemented with GTK+. It is still in early stages
of development.

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
%{_libexecdir}/lxdm-greeter-gdk
%{_libexecdir}/lxdm-numlock
%{_libexecdir}/lxdm-session
%{_unitdir}/lxdm.service

#---------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

rm data/lxdm.conf

%build
%configure
%make

%install
%makeinstall_std

# dm conf file
install -dm 0755 %{buildroot}%{_datadir}/X11/dm.d/
install -pm 0644 %{SOURCE1} %{buildroot}%{_datadir}/X11/dm.d/27%{name}.conf

# locales
%find_lang %{name}

