Name:		tint2
Version:	16.6.1
Release:	1%{?dist}
Summary:	A lightweight X11 desktop panel and task manager

Group:		User Interface/Desktops
License:	GPLv2
URL:		https://gitlab.com/o9000/%{name}
Source0:	%url/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake3
BuildRequires:  ninja-build
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	gettext
BuildRequires:	desktop-file-utils

%description
tint2 is a simple panel/taskbar made for modern X window managers. It was
specifically made for Openbox3 but should also work with other window managers
(GNOME, KDE, etc...). It's based on ttm code http://code.google.com/p/ttm/.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
mkdir -p build
pushd build
%{cmake3} -DENABLE_EXAMPLES=ON -GNinja ..
%{ninja_build}
popd

%install
pushd build
%{ninja_install}
popd

rm -rf %{buildroot}%{_datadir}/doc/

install -p -m 0644 packaging/debian/tint2conf.1 %{buildroot}/%{_mandir}/man1/

desktop-file-install	\
	--set-key=NoDisplay  --set-value=true	\
	--delete-original	\
	--dir=%{buildroot}%{_datadir}/applications	\
	%{buildroot}/%{_datadir}/applications/tint2.desktop

desktop-file-install	\
	--delete-original	\
	--dir=%{buildroot}%{_datadir}/applications	\
	%{buildroot}/%{_datadir}/applications/tint2conf.desktop

%find_lang tint2conf

%if 0%{?rhel}
%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%files -f tint2conf.lang
%doc AUTHORS ChangeLog README.md doc/images/
%doc doc/manual.html doc/readme.html doc/tint2.md
%license COPYING
%{_bindir}/tint2
%{_bindir}/tint2conf
%dir %{_sysconfdir}/xdg/tint2/
%config(noreplace) %{_sysconfdir}/xdg/tint2/tint2rc
%{_datadir}/tint2/
%{_datadir}/applications/tint2conf.desktop
%{_datadir}/applications/tint2.desktop
%{_datadir}/icons/hicolor/scalable/apps/tint*
%{_datadir}/mime/packages/tint2conf.xml
%{_mandir}/man1/tint2*

%changelog
* Thu Aug 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 16.6.1-1
- New version 16.6.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 16.4-1
- New version 16.4

* Thu Feb 08 2018 Leigh Scott <leigh123linux@googlemail.com> - 16.2-2
- Fix epel7 build

* Thu Feb 08 2018 Leigh Scott <leigh123linux@googlemail.com> - 16.2-1
- New version 16.2

* Sat Jan 13 2018 Leigh Scott <leigh123linux@googlemail.com> - 16.1-1
- New version 16.1

* Fri Oct 27 2017 Leigh Scott <leigh123linux@googlemail.com> - 15.2-1
- New version 15.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.14.4-1
- New version 0.14.4
- Switch source to github
- Add tint2conf man page

* Mon Apr 24 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.14.3-1
- New version 0.14.3

* Thu Mar 16 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.13.1-1
- New version 0.13.1
- Fix un-owned directory
- Remove 'create tint2 config directory' hack
- Move sample configs from doc

* Sun Mar 05 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.13-1
- New version 0.13

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 06 2016 Leigh Scott <leigh123linux@googlemail.com> - 0.12.12-1
- New version 0.12.12

* Thu May 19 2016 Leigh Scott <leigh123linux@googlemail.com> - 0.12.11-1
- New version 0.12.11

* Wed Feb 24 2016 Leigh Scott <leigh123linux@googlemail.com> - 0.12.7-1
- New version 0.12.7

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.12.3-1
- New version 0.12.3

* Tue Aug 11 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.12.2-1
- New version 0.12.2

* Tue Aug 04 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.12.1-2
- upstream commit should fix bz 1249777

* Tue Aug 04 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.12.1-1
- New version 0.12.1

* Tue Jul 14 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.12-4
- add obsoletes tintwizard

* Tue Jul 14 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.12-3
- remove requires tintwizard

* Tue Jul 14 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.12-2
- fix source release version

* Tue Jul 14 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.12-1
- New version 0.12

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.11-13
- create tint2 config directory

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 24 2013 Germán A. Racca <skytux@fedoraproject.org> - 0.11-9
- Added dependency on tintwizard (BZ#880626)
- Replaced tabs by spaces in spec file

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 27 2011 Germán A. Racca <skytux@fedoraproject.org> 0.11-5
- Fixed unowned directory (BZ#744930)

* Wed Jun 01 2011 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.11-4
- Adding tint2-add-power-now-support.patch (BZ#709821)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 20 2010 Germán A. Racca <gracca@gmail.com> 0.11-2
- Removed tintwizard.py because it was packaged separately

* Fri Jul 02 2010 German A. Racca <gracca@gmail.com> 0.11-1
- New version 0.11
- Used %%{cmake} to perform compilation
- Compiled with examples enabled
- Now really fixed BuildRequires

* Thu Apr 22 2010 German A. Racca <gracca@gmail.com> 0.9-2
- Fixed BuildRequires

* Fri Mar 26 2010 German A. Racca <gracca@gmail.com> 0.9-1
- New version 0.9

* Sat Mar 20 2010 German A. Racca <gracca@gmail.com> 0.8-2
- Rearrangement of some commands for good rpm practice
- Removed zero-length file

* Fri Jan 15 2010 German A. Racca <gracca@gmail.com> 0.8-1
- New version

* Mon Dec 21 2009 German A. Racca <gracca@gmail.com> 0.7.1-1
- Initial release of RPM package
