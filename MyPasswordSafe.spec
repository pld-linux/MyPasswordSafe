Summary:	Password Safe - a password database utility
Summary(pl):	Password Safe - narz�dzie do zarz�dzania baz� danych hase�
Name:		MyPasswordSafe
Version:	20050615
Release:	1
License:	GPL v2
Group:		Applications/Databases
Source0:	http://www.semanticgap.com/myps/release/%{name}-%{version}.src.tgz
# Source0-md5:	90106a0c0f07c6e028345357db566be6
Source1:	%{name}.desktop
URL:		http://www.semanticgap.com/myps/
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	qmake
BuildRequires:	qt-linguist
BuildRequires:	rpmbuild(macros) >= 1.129
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

%description -l pl
MyPasswordSafe to prosty, �atwy w u�yciu zarz�dca hase� utrzymuj�cy
kompatybilno�� z plikami Password Safe. MyPasswordSafe ma nast�puj�ce
mo�liwo�ci:
- "Sejfy" z has�ami s� szyfrowane przy zapisie na dysk.
- Hase� nie trzeba nigdy widzie�, poniewa� s� kopiowane do schowka.
- Mog� by� generowane has�a losowe.
- Mo�na zapami�ta� rozmiar i po�o�enie okna oraz szeroko�ci kolumn.
- Has�a pozostaj� zaszyfrowane a� do chwili kiedy musz� by�
  odszyfrowane na poziomie okien dialogowych i plik�w.
- "Sejf" mo�e by� uczyniony aktywnym, tak �e jest otwierany przy
  uruchomieniu MyPasswordSafe.
- Obs�uguje Unikod w has�ach.

%prep
%setup -q

%build
%{__make} \
	CC=%{__cc} \
	PREFIX=/usr \
	QTDIR=/usr

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
%doc doc/manual.html doc/sshots/*.jpg
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale
%{_datadir}/%{name}/locale/mypasswordsafe_c.qm
%lang(en) %{_datadir}/%{name}/locale/mypasswordsafe_en.qm
%lang(fr) %{_datadir}/%{name}/locale/mypasswordsafe_fr.qm
%{_desktopdir}/*.desktop
