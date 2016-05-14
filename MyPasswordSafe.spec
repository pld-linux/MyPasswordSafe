Summary:	Password Safe - a password database utility
Summary(pl.UTF-8):	Password Safe - narzędzie do zarządzania bazą danych haseł
Name:		MyPasswordSafe
Version:	20061216
Release:	3
License:	GPL v2
Group:		Applications/Databases
Source0:	http://www.semanticgap.com/myps/release/%{name}-%{version}.src.tgz
# Source0-md5:	0fef98e77c8e593382fb201bd278cacf
Source1:	%{name}.desktop
Patch0:		build.patch
URL:		http://www.semanticgap.com/myps/
BuildRequires:	kde4-kde3support-devel
BuildRequires:	qmake
BuildRequires:	qt-linguist
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-proto-scrnsaverproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MyPasswordSafe is a straight-forward, easy-to-use password manager
that maintains compatibility with Password Safe files. MyPasswordSafe
has the following features:
- Safes are encrypted when they are stored to disk.
- Passwords never have to be seen, because they are copied to the
  clipboard.
- Random passwords can be generated.
- Window size, position, and column widths are remembered.
- Passwords remain encrypted until they need to be decrypted at the
  dialog and file levels.
- A safe can be made active so it will always be opened when
  MyPasswordSafe starts.
- Supports Unicode in the safes.

%description -l pl.UTF-8
MyPasswordSafe to prosty, łatwy w użyciu zarządca haseł utrzymujący
kompatybilność z plikami Password Safe. MyPasswordSafe ma następujące
możliwości:
- "Sejfy" z hasłami są szyfrowane przy zapisie na dysk.
- Haseł nie trzeba nigdy widzieć, ponieważ są kopiowane do schowka.
- Mogą być generowane hasła losowe.
- Można zapamiętać rozmiar i położenie okna oraz szerokości kolumn.
- Hasła pozostają zaszyfrowane aż do chwili kiedy muszą być
  odszyfrowane na poziomie okien dialogowych i plików.
- "Sejf" może być uczyniony aktywnym, tak że jest otwierany przy
  uruchomieniu MyPasswordSafe.
- Obsługuje Unikod w hasłach.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	PREFIX=%{_prefix} \
	QTDIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/locale,%{_desktopdir},%{_pixmapsdir}}

install MyPasswordSafe $RPM_BUILD_ROOT%{_bindir}
install locale/*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/locale

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/manual.html doc/sshots/*.jpg README
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale
%{_datadir}/%{name}/locale/mypasswordsafe_c.qm
%lang(en) %{_datadir}/%{name}/locale/mypasswordsafe_en.qm
%lang(fr) %{_datadir}/%{name}/locale/mypasswordsafe_fr.qm
%{_desktopdir}/*.desktop
